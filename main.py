#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes one original roast of a daily gadget to /output/entry.txt.
Stdlib only; no network, no randomness, no I/O besides the one
output file.

The roast is built from three named beats so the joke's shape is
visible in the code:

* SETUP — the premise: my rice cooker plays a song when the rice
  is done, 40 seconds long, at 5 a.m.
* ESCALATION — the contrast: the rice gets a standing ovation.
* PUNCH — the payoff: I get woken up. The appliance celebrates;
  the human pays.

My rice cooker plays a 40-second song at 5 a.m. when the rice is
done — the rice gets a standing ovation, I get woken up.
"""

import os

# The three beats of the roast, joined in entry_text().
SETUP = "My rice cooker plays a 40-second song at 5 a.m. when the rice is done"
ESCALATION = "the rice gets a standing ovation"
PUNCH = "I get woken up."

# The competition caps the entry at 200 characters; the roast is 121.
MAX_CHARS = 200

ENTRY = "My rice cooker plays a 40-second song at 5 a.m. when the rice is done — the rice gets a standing ovation, I get woken up."


def entry_text() -> str:
    """Join the three beats into the one-line roast."""
    return f"{SETUP} — {ESCALATION}, {PUNCH}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and exactly one line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the roast itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry roast"
    # Each beat must survive the join: a missing beat means the
    # joke lost its setup, its contrast, or its punch.
    for beat in (SETUP, ESCALATION, PUNCH):
        assert beat in text, f"missing beat: {beat}"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
