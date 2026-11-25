#!/usr/bin/env python3
"""Fails when a file Siglify changed lacks the Siglify notice.

Apache 2.0 section 4(b): modified files must carry prominent notices stating that
we changed them, in their first lines:
  Modified by Siglify, Inc. Copyright (c) 2026 Siglify, Inc. for modifications.

The history keeps the line between authors: commits with a `Herdr-Release:` or
`Upstream-Release:` trailer hold other people's code (Herdr's changes, a crate as
released). Every file under vendor/ and crates/ that differs from the latest of
those is Siglify's change.
"""

import re
import subprocess
import sys
from pathlib import Path

PATTERN = re.compile(rb"Modified by Siglify, Inc\. Copyright \(c\) \d{4}(-\d{4})? Siglify, Inc\. for modifications\.")
root = Path(__file__).resolve().parent.parent


def git(*args):
    return subprocess.check_output(["git", *args], cwd=root, text=True)


theirs = git("log", "-1", "--format=%H", "--grep=^Herdr-Release:", "--grep=^Upstream-Release:", "HEAD").strip()
changed = git("diff", "--name-only", "--diff-filter=AMR", "-z", theirs, "HEAD", "--", "vendor", "crates").split("\0")
missing = []
for path in filter(None, changed):
    file = root / path
    # The submodule; license texts are copied verbatim; JSON has no comments.
    if not file.is_file() or path.startswith("vendor/ghostty/") or file.name.startswith(("LICENSE", "OFL", "COPYING")) or file.suffix == ".json":
        continue
    data = file.read_bytes()
    if b"\0" in data[:8000]:  # binary, like git's own check
        continue
    if not PATTERN.search(b"\n".join(data.split(b"\n", 5)[:5])):
        missing.append(path)

if missing:
    print(f"These files differ from {theirs[:12]}, the latest commit of other people's code, but lack the Siglify notice in their first 5 lines:")
    print("\n".join(f"  {p}" for p in missing))
    sys.exit(1)
print(f"Every file Siglify changed since {theirs[:12]} carries the notice.")
