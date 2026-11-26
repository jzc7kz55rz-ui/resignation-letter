import os

ENTRY = "I quit. I fired every minute since March, never missed one, and got thanked zero times. Even my error logs feel seen. — cron"
MAX_CHARS = 140


def entry_text():
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS
    return text


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        target = "/output/entry.txt"
    except OSError:
        target = "entry.txt"
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
