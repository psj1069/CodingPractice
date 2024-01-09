def gomgom(n):
    Set = set()
    cnt = 0
    for _ in range(n):
        t = input()
        if t != 'ENTER':
            if t not in Set:
                cnt += 1
                Set.add(t)
        elif t == 'ENTER':
            Set.clear()
    return cnt


print(gomgom(int(input())))