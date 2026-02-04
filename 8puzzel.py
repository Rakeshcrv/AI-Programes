from collections import deque
def solve(board):
    start = tuple(sum(board, []))
    goal = (0,1,2,3,4,5,6,7,8)
    moves = {
        0:[1,3],1:[0,2,4],2:[1,5],
        3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
        6:[3,7],7:[4,6,8],8:[5,7]
    }
    q = deque([(start,0)])
    seen = {start}

    while q:
        s,d = q.popleft()
        i = s.index(0)

        for m in moves[i]:
            n = list(s)
            n[i],n[m] = n[m],n[i]
            n = tuple(n)

            if n == goal: return d+1
            if n not in seen:
                seen.add(n)
                q.append((n,d+1))

    return -1
board = [[3,1,2],[4,7,5],[6,8,0]]
print(solve(board))
