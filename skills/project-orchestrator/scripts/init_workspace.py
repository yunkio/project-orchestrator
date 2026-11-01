#!/usr/bin/env python3
"""Create five run documents without overwriting existing files. Standard library only."""

import argparse
from pathlib import Path
from urllib.parse import urlsplit


DOCUMENTS = ("QNA.md", "USER_INTENT.md", "REQUIREMENTS.md", "WORKLOG.md", "CHECKLIST.md")


def source_ref(value, project):
    if urlsplit(value).scheme in ("http", "https"):
        return value
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = project / path
    path = path.resolve()
    if not path.is_file():
        raise ValueError(f"Source is not a file: {path}")
    return str(path)


def initialize(project_dir, artifact_dir, sources, stakeholders=(), time_budget=None):
    project = Path(project_dir).expanduser().resolve()
    target = Path(artifact_dir).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    if target.exists() and not target.is_dir():
        raise ValueError(f"Artifact directory is not a directory: {target}")
    conflicts = [str(target / name) for name in DOCUMENTS if (target / name).exists()]
    if conflicts:
        raise ValueError("Existing run documents found; resume them instead of overwriting: " + ", ".join(conflicts))
    source_paths = [source_ref(value, project) for value in sources]
    stakeholder_paths = [source_ref(value, project) for value in stakeholders]
    assets = Path(__file__).resolve().parent.parent / "assets"
    contents = {name: (assets / name).read_text(encoding="utf-8") for name in DOCUMENTS}
    manifest = [f"- 작업 경로: `{project}`", f"- 기록 경로: `{target}`",
                f"- 시간·자원: {time_budget or '미지정 — 필요한 값은 QNA로 확인'}",
                "- 요구사항 자료:"]
    manifest.extend(f"  - `{value}`" for value in source_paths)
    manifest.append("- 현업 자료:")
    manifest.extend(f"  - `{value}`" for value in stakeholder_paths)
    if not stakeholder_paths:
        manifest.append("  - 미지정 — 없음인지, 별도 질의 채널이 있는지 확인")
    manifest.extend(["", "이 목록은 호출 인자다. 자료 열람·요구 확정·사용자 동의를 의미하지 않는다."])
    marker = "<!-- INVOCATION_MANIFEST -->"
    if marker not in contents["WORKLOG.md"]:
        raise ValueError("WORKLOG template is missing its invocation marker")
    contents["WORKLOG.md"] = contents["WORKLOG.md"].replace(marker, "\n".join(manifest), 1)
    target.mkdir(parents=True, exist_ok=True)
    written = []
    for name, content in contents.items():
        path = target / name
        # Exclusive creation protects against another writer appearing after preflight.
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        written.append(path)
    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-dir", required=True)
    parser.add_argument("--artifact-dir", required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--stakeholder-source", action="append", default=[])
    parser.add_argument("--time-budget")
    args = parser.parse_args()
    try:
        paths = initialize(args.project_dir, args.artifact_dir, args.source,
                           args.stakeholder_source, args.time_budget)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Initialization stopped: {error}\nExisting files were not overwritten.\n")
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
