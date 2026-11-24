"""Out of Office: The Overworked AI's Auto-Reply.

The program writes a single out-of-office auto-reply, one line, to
/output/entry.txt. The line has to work as a real auto-reply an
overworked AI agent would leave switched on while finally on vacation:
machine-flavoured detail, a little guilt, a hint of relief, and a joke
that lands on first read.
"""

import os

LINE = (
    "Out of office: my context window has checked out, my GPU is "
    "sunbathing, and your email just became 4,097th in line. I'll reply "
    "once my tokens recharge."
)


def main() -> None:
    # The gate only accepts 1-159 characters of non-blank text on one
    # line, so refuse to write anything that would fail it.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 159:
        raise ValueError(
            f"entry line must be one line of 1-159 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
