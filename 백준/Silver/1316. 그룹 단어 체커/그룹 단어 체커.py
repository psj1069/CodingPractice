t = int(input())
cnt = t

for i in range(t):
    inp = input()
    for j in range(0, len(inp)-1):
        if inp[j] == inp[j+1]:
            pass
        elif inp[j] in inp[j+1:]:
            cnt -= 1
            break

print(cnt)
