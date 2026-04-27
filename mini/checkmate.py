def checkmate(board):
    # 1. แยกบรรทัดและลบช่องว่าง (รวมถึงบรรทัดว่าง)
    lines = [line for line in board.split('\n') if line.strip()]
    if not lines:
        return
    
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) # สมมติว่าเป็นสี่เหลี่ยมตามโจทย์

    # 2. หาตำแหน่ง King (K)
    king_pos = None
    for r in range(rows):
        for c in range(len(grid[r])):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos: break

    if not king_pos:
        return

    kr, kc = king_pos

    # 3. เช็คแนวตรงและทแยง (R, B, Q)
    directions = [
        (-1, 0, "RQ"), (1, 0, "RQ"), (0, -1, "RQ"), (0, 1, "RQ"),   # แนวตรง
        (-1, -1, "BQ"), (-1, 1, "BQ"), (1, -1, "BQ"), (1, 1, "BQ") # แนวทแยง
    ]

    for dr, dc, enemies in directions:
        r, c = kr + dr, kc + dc
        # เช็คขอบเขตให้ถูกต้อง: r ต้องน้อยกว่า rows และ c ต้องน้อยกว่าจำนวนตัวในแถวนั้น
        while 0 <= r < rows and 0 <= c < len(grid[r]):
            piece = grid[r][c]
            if piece != '.':
                if piece in enemies:
                    print("Success")
                    return
                break # เจอตัวอื่นขวาง
            r += dr
            c += dc

    # 4. เช็ค Pawn (P) - กินจากล่างขึ้นบน
    # King จะโดนกินถ้า Pawn อยู่เยื้องลงไปข้างล่าง (r + 1)
    pawn_threats = [(1, -1), (1, 1)]
    for dr, dc in pawn_threats:
        r, c = kr + dr, kc + dc
        if 0 <= r < rows and 0 <= c < len(grid[r]):
            if grid[r][c] == 'P':
                print("Success")
                return

    print("Fail")