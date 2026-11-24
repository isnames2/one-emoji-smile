# One Emoji, One Smile — entry program (make.fun).
# Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt.
# Pure standard library; no network; deterministic output.

import os
from pathlib import Path

# The pick: a hugging face rather than the default smiley — open arms read
# as a warm welcome from a stranger, with no intimacy or in-joke attached.
EMOJI = "\U0001F917"  # hugging face: open arms, warm and friendly


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
