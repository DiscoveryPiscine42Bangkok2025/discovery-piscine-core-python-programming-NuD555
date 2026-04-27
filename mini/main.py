from checkmate import checkmate

def main():
    # ทดสอบตัวอย่างที่ 1 (Rook เล็งจากข้างบน)
    board1 = """\
R...
.K..
..P.
...."""
    
    # ทดสอบตัวอย่างที่ 2 (Bishop เล็งแนวทแยง)
    board2 = """\
..
.K
B."""

    print("Test 1: ", end="")
    checkmate(board1) # ผลควรเป็น Success
    
    print("Test 2: ", end="")
    checkmate(board2) # ผลควรเป็น Success

if __name__ == "__main__":
    main()
