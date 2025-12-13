"""Utils for day 2 advent of code."""
import math

def read_file() -> list[tuple[int, int]]:
    """Reads the input file and returns a list of tuples containing pairs of integers."""
    with open("./input.txt") as f:
        lines: list[tuple[int, int]] = []
        for line in f.read().split(","):
            line = tuple([int(x) for x in line.split("-")])
            lines.append(line) # type: ignore
        return lines
    
def count_digits(number: int) -> int:
    """Returns the number of digits in the given integer."""
    return len(str(abs(number)))

def find_factors(number: int) -> list[int]:
    """Returns a list of factors of the given integer."""
    factors: list[int] = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return sorted(factors)