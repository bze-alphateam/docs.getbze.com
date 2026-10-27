#!/usr/bin/env python3
"""Checks the docs for things that break the GitBook view.

- every SUMMARY.md entry points to an existing file
- every page is listed in SUMMARY.md and starts with the GitBook `layout:` frontmatter
- relative links, images and content-ref cards point to existing files
- GitBook blocks ({% hint %}, {% content-ref %}, {% tabs %}, ...) are opened and closed
- code fences are balanced and table rows have the same number of columns

old-docs/ is deprecated and left untouched, so only its SUMMARY entries are checked.
Usage: validate-docs.py [docs root, default: current directory]
"""
import os
import re
import sys

PAIRED_BLOCKS = ["hint", "content-ref", "tabs", "tab", "stepper", "step", "columns", "column", "code"]
SINGLE_BLOCKS = ["include", "file", "embed"]  # embed may or may not have an endembed
SKIP_DIRS = {"old-docs"}
EXTERNAL = re.compile(r"^(https?:|mailto:|#)")


def links_in(text):
    md = re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text)
    refs = re.findall(r'content-ref url="([^"]+)"', text)
    imgs = re.findall(r'<img[^>]*\ssrc="([^"]+)"', text)
    return md + refs + imgs


def check_page(root, rel, errors):
    path = os.path.join(root, rel)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")

    parts = text.split("---\n", 2)
    if not text.startswith("---\n") or len(parts) < 3 or "layout:" not in parts[1]:
        errors.append(f"{rel}: missing the GitBook `layout:` frontmatter")

    in_fence = False
    table_cols = None
    for n, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        if stripped.startswith("|"):
            cols = len(re.findall(r"(?<!\\)\|", re.sub(r"`[^`]*`", "", stripped)))
            if table_cols is None:
                table_cols = cols
            elif cols != table_cols:
                errors.append(f"{rel}:{n}: table row has {cols} pipes, the header has {table_cols}")
        else:
            table_cols = None
    if in_fence:
        errors.append(f"{rel}: unclosed code fence")

    tags = re.findall(r"\{%\s*([\w-]+)", text)
    for tag in tags:
        name = tag[3:] if tag.startswith("end") else tag
        if name not in PAIRED_BLOCKS and name not in SINGLE_BLOCKS:
            errors.append(f"{rel}: unknown GitBook block `{{% {tag} %}}`")
    for name in PAIRED_BLOCKS:
        opened, closed = tags.count(name), tags.count("end" + name)
        if opened != closed:
            errors.append(f"{rel}: {opened} `{{% {name} %}}` but {closed} `{{% end{name} %}}`")

    for link in links_in(text):
        if EXTERNAL.match(link):
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), link.split("#")[0]))
        if not os.path.exists(target):
            errors.append(f"{rel}: broken link `{link}`")


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    errors = []

    with open(os.path.join(root, "SUMMARY.md"), encoding="utf-8") as f:
        summary = f.read()
    listed = set()
    for link in re.findall(r"\]\(([^)]+)\)", summary):
        rel = os.path.normpath(link.split("#")[0])
        listed.add(rel)
        if not os.path.exists(os.path.join(root, rel)):
            errors.append(f"SUMMARY.md: entry points to a missing file `{link}`")

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS)
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            if rel == "SUMMARY.md":
                continue
            if rel not in listed:
                errors.append(f"{rel}: page is not listed in SUMMARY.md")
            check_page(root, rel, errors)

    for e in errors:
        print(f"::error::{e}" if os.environ.get("GITHUB_ACTIONS") else e)
    if errors:
        print(f"{len(errors)} problem(s) found")
        return 1
    print("Docs OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
