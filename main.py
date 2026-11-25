"""Funniest one-line out-of-office reply for make.fun bounty
u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.

Writes one single-line out-of-office auto-reply (at most 160 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib, deterministic: the same line on every run.
"""

import os

LINE = "I'm out of the office until Monday. Anything urgent, please ask someone else; anything else, please also ask someone else."


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars, must be 1-160"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-check the gate the sealed scorer applies: UTF-8, 1-160 chars,
    # single line, not only whitespace, byte-identical to the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
