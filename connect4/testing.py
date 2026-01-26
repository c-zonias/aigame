from board import Board, EMPTY, RED, YELLOW

def test_horizontal_win():
    b = Board()
    b.drop_piece(0, RED)
    b.drop_piece(1, RED)
    b.drop_piece(2, RED)
    b.drop_piece(3, RED)
    assert b.check_winner() == RED
    print("✅ Horizontal win test passed")

def test_vertical_win():
    b = Board()
    for _ in range(4):
        b.drop_piece(0, YELLOW)
    assert b.check_winner() == YELLOW
    print("✅ Vertical win test passed")

def test_diag_down_right_win():
    b = Board()
    # Make a \ diagonal for RED at (row 5,col0) (4,1) (3,2) (2,3)
    b.drop_piece(0, RED)

    b.drop_piece(1, YELLOW); b.drop_piece(1, RED)

    b.drop_piece(2, YELLOW); b.drop_piece(2, YELLOW); b.drop_piece(2, RED)

    b.drop_piece(3, YELLOW); b.drop_piece(3, YELLOW); b.drop_piece(3, YELLOW); b.drop_piece(3, RED)

    assert b.check_winner() == RED
    print("✅ Diagonal (\\) win test passed")

def test_diag_up_right_win():
    b = Board()
    # Make a / diagonal for YELLOW at (row 2,col0) (3,1) (4,2) (5,3)
    # Build supports with RED.
    b.drop_piece(0, RED); b.drop_piece(0, RED); b.drop_piece(0, RED); b.drop_piece(0, YELLOW)

    b.drop_piece(1, RED); b.drop_piece(1, RED); b.drop_piece(1, YELLOW)

    b.drop_piece(2, RED); b.drop_piece(2, YELLOW)

    b.drop_piece(3, YELLOW)

    assert b.check_winner() == YELLOW
    print("✅ Diagonal (/) win test passed")

def test_no_win():
    b = Board()
    b.drop_piece(0, RED)
    b.drop_piece(1, YELLOW)
    b.drop_piece(2, RED)
    assert b.check_winner() == EMPTY
    print("✅ No-win test passed")

def test_is_draw_false_when_not_full():
    b = Board()
    assert b.is_draw() == False
    print("✅ is_draw() false when not full passed")

if __name__ == "__main__":
    test_horizontal_win()
    test_vertical_win()
    test_diag_down_right_win()
    test_diag_up_right_win()
    test_no_win()
    test_is_draw_false_when_not_full()