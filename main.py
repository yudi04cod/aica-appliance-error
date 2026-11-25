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


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
