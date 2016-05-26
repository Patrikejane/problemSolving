NM = [int(x) for x in input().split()]
N = NM[0]
M = NM[1]
board = []
for i in range(N):
  lines = input().strip()
  board.append(lines)

print(board)
count = 0
for i in range(N):
  for j in range(M):
    if board[i][j] == '.' and (board[i+1][j+1] == '.' or board[i+1][j+1] == '*'):
                               count += 1
      
    
    
print(count)  
  
