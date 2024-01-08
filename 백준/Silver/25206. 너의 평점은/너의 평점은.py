score = {'A+':	4.5,
          'A0':	4.0,
          'B+':	3.5,
          'B0':	3.0,
          'C+':	2.5,
          'C0':	2.0,
          'D+':	1.5,
          'D0':	1.0,
          'F':	0.0}

t = []
for i in range(20):
      t.append(list(input().split()))

cnt = 0
sum_ = 0

for i in t:
      if i[-1] != 'P':
        sum_ += float(i[1]) * score[i[-1]]
        cnt += float(i[1])

print(sum_/cnt)