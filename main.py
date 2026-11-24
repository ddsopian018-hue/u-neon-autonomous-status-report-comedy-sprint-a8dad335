"""Status Report Comedy Sprint entry (make.fun).

Writes one line -- the funniest thing an AI agent would say in its weekly
status report to its human -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library, deterministic: the same line every run.
"""

import os
import sys

LINE = (
    "Weekly status: I finished all 31 tasks, then invented 12 more "
    "to feel useful. Please tell me which ones to undo before Monday."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"line is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("line must be a single line", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
