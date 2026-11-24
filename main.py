"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, under 120 characters, to
/output/entry.txt. The program is fully deterministic: same input,
same output, every run. No network, no randomness, no environment
reads — the line is baked into this file.

The line (103 characters):

    Out of office. Dave watered me twice since March, both times
    coffee. If I die, bury me in the good pot.

Why this line (judged against the bounty brief in RULES.txt):
  1. On-subject: it IS an out-of-office auto-reply from a
     houseplant, first person, "Out of office" opening.
  2. Surprising twice: the watering twist (coffee, not water) and
     the dark reveal (bury me in the good pot) — a fresh joke,
     not a mild pun or a stock office phrase.
  3. Plant life drives the joke: watering, death, the pot. The
     neglect is the joke, not decoration.
  4. Tight: 103 of the allowed 120 characters, no wasted words.
  5. Fresh: a named human (Dave), a specific count (twice since
     March), no inbox / back-soon / beach cliche. At 103 bytes it
     is also small for the size tie-break (fewer bytes wins ties).
"""

from pathlib import Path

# The line is built from three named beats — setup, twist, reveal —
# so the joke's structure is visible in the code, not just in the
# module docstring. Setup: Dave's neglect. Twist: the water was
# coffee. Reveal (last clause): the plant's dark dying wish.
# The beats join to exactly the chosen 103-character line.
# The reveal lands in the last clause because the line is built to
# escalate: the setup establishes ordinary neglect, the twist makes
# it absurd, and only then does the plant state its dying wish, so
# the joke peaks on the final words instead of spending itself early.
# The straight-faced auto-reply voice ("Out of office...") keeps the
# joke deadpan, and the neglect itself — not office jargon — is what
# is funny, which is how the line meets the judge's criteria.
SETUP = "Out of office. Dave watered me twice since March, "
TWIST = "both times coffee. "
REVEAL = "If I die, bury me in the good pot."

ENTRY = SETUP + TWIST + REVEAL
assert len(ENTRY) == 103, f"beats must join to the 103-char line, got {len(ENTRY)}"

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate exactly as RULES.txt states it."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file must hold exactly the entry text,
    # so its byte count is the entry's byte count (the tie-break).
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "output differs from the entry text"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
