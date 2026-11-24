"""The Funniest Out-of-Office — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a funny out-of-office auto-reply of at most 140 characters.
"""
import os

LINE = "I'm out of office until Monday. My inbox is on vacation too — it left before I did and took the Wi-Fi with it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
