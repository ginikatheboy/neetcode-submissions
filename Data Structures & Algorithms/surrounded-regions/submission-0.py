from collections import deque
from typing import List


class Solution:

  def solve(self, board: List[List[str]]) -> None:
    if not board or not board[0]:
      return

    m, n = len(board), len(board[0])
    stk = deque()

    for j in range(n):
      if board[0][j] == "O":
        stk.append((0, j))
      if m > 1 and board[m - 1][j] == "O":
        stk.append((m - 1, j))

    for i in range(1, m - 1):
      if board[i][0] == "O":
        stk.append((i, 0))
      if n > 1 and board[i][n - 1] == "O":
        stk.append((i, n - 1))

    while stk:
      i, j = stk.popleft()
      if board[i][j] == "T":
        continue
      board[i][j] = "T"

      for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r, c = i + i_off, j + j_off
        if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
          stk.append((r, c))

    for i in range(m):
      for j in range(n):
        if board[i][j] == "O":
          board[i][j] = "X"
        elif board[i][j] == "T":
          board[i][j] = "O"