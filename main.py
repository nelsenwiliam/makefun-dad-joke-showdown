"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt (pure stdlib, deterministic:
the same bytes on every run, no randomness, no network).
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "Our Wi-Fi went down, so I told my son we'd have to talk to each "
    "other tonight. He asked, 'What's the password for that?'"
)


def main() -> None:
    # The gate only accepts 1-200 characters of non-blank UTF-8 text;
    # fail loudly here instead of shipping an invalid entry.
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-200")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
