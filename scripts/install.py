#!/usr/bin/env python3
"""Install the style skill as a local link without replacing existing content."""
import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, help="Override the personal skills directory")
    parser.add_argument("--check", action="store_true", help="Check installation without changes")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "wsl-ppt-style"
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser()
    target_dir = (args.skills_dir or codex_home / "skills").expanduser().absolute()
    target = target_dir / source.name
    if not (source / "SKILL.md").is_file():
        parser.exit(1, "Missing skill source: " + str(source) + "\n")
    occupied = os.path.lexists(target)
    same_link = target.is_symlink() and target.resolve() == source
    if args.check:
        if same_link and (target / "SKILL.md").is_file():
            print("Installed:", target, "->", source)
            return
        parser.exit(1, "Not linked to this checkout: " + str(target) + "\n")
    if occupied:
        if same_link:
            print("Already installed:", target)
            return
        parser.exit(1, "Existing skill preserved; choose another directory or inspect it first: " + str(target) + "\n")
    target_dir.mkdir(parents=True, exist_ok=True)
    target.symlink_to(source, target_is_directory=True)
    print("Installed:", target, "->", source)


if __name__ == "__main__":
    main()
