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

def compute_wrapped(position: int, start_at_zero: bool) -> tuple[int, int]:
    if position >= 100:
        # If >= 100, we can simply count the hundreds for the number of times around
        num_wrapped = position // 100
    elif position < 0:
        if start_at_zero and position % 100 != 0:
            # If we start at zero and don't land on a multiple of 100, add one to the floor to ensure we don't count the initial zero
            num_wrapped = abs(position // 100 + 1)
        elif position % 100 == 0:
            # If we land on multiple of 100, add one to account for the floor logic
            # e.g., 4 -> -200 = 3 passes of 0, -200 // 100 = 2 + 1 (for passing 0)
            num_wrapped = abs(position // 100) + 1
        else:
            # If we start at zero and don't land on a multiple of 100, the floor will account for passing 0
            # e.g., 4 -> -201 = 3 passes of 0, -201 // 100 = 3
            num_wrapped = abs(position // 100)
    else:
        num_wrapped = int(position == 0)
    
    return position % 100, num_wrapped