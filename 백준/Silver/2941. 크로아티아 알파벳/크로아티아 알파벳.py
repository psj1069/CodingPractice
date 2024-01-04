a = input()
cr_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cr_a:
    a = a.replace(i, "*")

print(len(a))