"""Day 2 - Advent of Code."""
from utils import read_file

def main():  # noqa: D103
    pairs = read_file()
    for start, end in pairs:
        print(start, end)


if __name__ == "__main__":
    main()