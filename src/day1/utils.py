def read_file() -> list[str]:
    with open("./input.txt") as f:
        return f.read().splitlines()

def parse_move(move: str) -> tuple[int, int]:
    direction = -1 if move[0] == 'L' else 1
    distance = int(move[1:])
    return direction, distance

def execute_move(position: int, direction:int, distance: int) -> int:
    position += direction * distance
    return position

def compute_wrapped(position: int, was_zero: bool) -> tuple[int, int]:
    if position >= 100: 
        return position % 100, position // 100
    elif position < 0:
        if was_zero:
            return position % 100, abs(position // 100 + 1)
        else:
            return position % 100, abs(position // 100)
    else:
        return position, int(position == 0)