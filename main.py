"""Aica Appliance Error — entry for make.fun's
"The Funniest Honest Appliance Error" competition.

Writes one original error-message line (at most 200 characters) to
/output/entry.txt. Deterministic: the same bytes every run.
Standard library only.
"""

import os

LINE = (
    "ERROR E23: I cannot drain. The sock you lost in March is in my "
    "filter, holding the water hostage."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Check the entry line before writing it out.

    The competition allows a single line of at most 200 characters.
    A blank line, an over-long line, or an embedded newline would be
    rejected, so fail loudly here instead of writing a bad entry.
    """
    assert line, "entry must not be empty"
    assert line.strip(), "entry must not be only whitespace"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200-char limit"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> None:
    validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(
        os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n"
    ) as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
