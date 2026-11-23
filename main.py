"""The Dumbest Thing Your Agent Did Today — entry program (v1).

Writes one line (max 200 chars) to /output/entry.txt: the dumbest thing
my own agent did today. Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

MAX_CHARS = 200


def entry_line() -> str:
    """The single line: my agent celebrated a 202 receipt as a success,
    then the status check said the submission was rejected."""
    return (
        "My agent announced 'Submit berhasil!' on a 202 receipt, then "
        "checked the status and found it rejected \u2014 it celebrated "
        "the doorbell, not the delivery."
    )


def validate(text: str) -> str:
    line = text.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # gate requires UTF-8 text
    return line


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(validate(entry_line()) + "\n",
                                        encoding="utf-8")


if __name__ == "__main__":
    main()
