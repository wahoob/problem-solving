class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue

                box = (i // 3) * 3 + (j // 3)

                if (
                    (c, "row", i) in seen or
                    (c, "col", j) in seen or
                    (c, "box", box) in seen
                ):
                    return False
                
                seen.add((c, "row", i))
                seen.add((c, "col", j))
                seen.add((c, "box", box))

        return True
                