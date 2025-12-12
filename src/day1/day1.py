from utils import compute_wrapped, parse_move, execute_move, read_file

START_POSITION = 50

def main():
    position = START_POSITION
    moves = read_file()

    wrapped = 0
    for move in moves:
        direction, distance = parse_move(move)
        was_zero = position == 0
        position = execute_move(position, direction, distance)
        position, num_wrapped = compute_wrapped(position, was_zero)
        wrapped += num_wrapped

    print(f"Number of times position wrapped: {wrapped}")

if __name__ == "__main__":
    main()