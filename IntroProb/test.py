n=4
name='JAAN'
move = n - 1
for idx in range(n):
    next_idx = idx + 1
    while (next_idx < n) and (name[next_idx] == 'A'):
        next_idx += 1
    distance = min(idx, n - next_idx)
    move = min(move, idx + n - next_idx + distance)
