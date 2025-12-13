"""Day 1 Tests."""
from src.day1.utils import parse_move, execute_move, compute_wrapped

def test_parse_move():
    """Test the parse_move function."""
    assert parse_move("L10") == (-1, 10)
    assert parse_move("R5") == (1, 5)
    assert parse_move("R1000") == (1, 1000)
    assert parse_move("L352") == (-1, 352)

def test_execute_move():
    """Test the execute_move function."""
    assert execute_move(50, -1, 10) == 40
    assert execute_move(50, -1, 68) == -18
    assert execute_move(82, -1, 30) == 52
    assert execute_move(52, 1, 48) == 100
    assert execute_move(0, -1, 5) == -5
    assert execute_move(95, 1, 60) == 155
    assert execute_move(55, -1, 55) == 0
    assert execute_move(0, -1, 1) == -1
    assert execute_move(99, -1, 99) == 0
    assert execute_move(0, 1, 14) == 14
    assert execute_move(14, -1, 82) == -68
    assert execute_move(50, 1, 1000) == 1050
    assert execute_move(50, -1, 1000) == -950

def test_compute_wrapped():
    """Test the compute_wrapped function."""
    assert compute_wrapped(40, False) == (40, 0)
    assert compute_wrapped(-18, False) == (82, 1)
    assert compute_wrapped(52, False) == (52, 0)
    assert compute_wrapped(100, False) == (0, 1)
    assert compute_wrapped(-5, True) == (95, 0)
    assert compute_wrapped(155, False) == (55, 1)
    assert compute_wrapped(0, False) == (0, 1)
    assert compute_wrapped(-1, True) == (99, 0)
    assert compute_wrapped(0, False) == (0, 1)
    assert compute_wrapped(14, True) == (14, 0)
    assert compute_wrapped(-68, False) == (32, 1)
    assert compute_wrapped(1050, False) == (50, 10)
    assert compute_wrapped(-950, False) == (50, 10)