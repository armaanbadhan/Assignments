# from pprint import pprint

n, m = map(int, input().strip().split())

cross = []

for i in range(n):
    cross.append(input().strip())

w = int(input())

words = {}

for i in range(w):
    x = input().strip()
    words[len(x)] = x

horizontal_x_y_start = []
horizontal_x_y_cnt = []

for i in range(n):
    cnt = 0
    flag = False
    for j in range(m):
        if cross[i][j] == 'b' or cross[i][j] == 'r':
            cnt += 1
            if not flag:
                horizontal_x_y_start.append([i, j])
                flag = True
            else:
                horizontal_x_y_cnt.append([i, j, cnt])
                cnt = 0
                flag = False
        elif flag and (cross[i][j] == '.' or cross[i][j] == 'c'):
            cnt += 1

# pprint(horizontal_x_y_start)
# pprint(horizontal_x_y_cnt)


for i in range(len(horizontal_x_y_start)):
    horizontal_x_y_start[i].append(horizontal_x_y_cnt[i][2])

# pprint(horizontal_x_y_start)
# pprint(horizontal_x_y_cnt)


'''
transversed = []

for i in range(m):
    temp = []
    for j in range(n):
        temp.append(cross[j][i])
    transversed.append(''.join(temp))

pprint(transversed)
'''

verticle_x_y_start = []
verticle_x_y_cnt = []

for i in range(m):
    cnt = 0
    flag = False
    for j in range(n):
        if cross[j][i] == 'b' or cross[j][i] == 'c':
            cnt += 1
            if not flag:
                verticle_x_y_start.append([j, i])
                flag = True
            else:
                verticle_x_y_cnt.append([j, i, cnt])
                cnt = 0
                flag = False
        elif flag and (cross[j][i] == '.' or cross[j][i] == 'r'):
            cnt += 1



for i in range(len(verticle_x_y_start)):
    verticle_x_y_start[i].append(verticle_x_y_cnt[i][2])


# pprint(verticle_x_y_start)
# pprint(verticle_x_y_cnt)

# pprint(words)

'''
occupiedh = []
occupiedv = []

for i in range(len(horizontal_x_y_start)):
    x, y = horizontal_x_y_start[i]
    while y <= horizontal_x_y_cnt[i][1]:
        occupiedh.append(((x, y), horizontal_x_y_cnt[i][2]))
        y += 1


for i in range(len(verticle_x_y_start)):
    x, y = verticle_x_y_start[i]
    while x <= verticle_x_y_cnt[i][0]:
        occupiedv.append(((x, y), verticle_x_y_cnt[i][2]))
        x += 1

pprint(occupiedh)
pprint(occupiedv)
'''

# print(words)

resh = []


i = 0
while i < n:
    j = 0
    temp = []
    while j < m:
        ele = cross[i][j]
        if ele == '#':
            temp.append('#')
            j += 1
        elif ele == 'b' or ele == 'r':
            for k in horizontal_x_y_start:
                if k[0] == i and k[1] == j:
                    leng = k[2]
                    horizontal_x_y_start.remove([i, j, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        temp.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            temp.append('-')
            j += 1
    resh.append(''.join(temp))
    i += 1

# pprint(resh)
# pprint(cross)

resv = []

i = 0
while i < m:
    j = 0
    temp = []
    while j < n:
        ele = cross[j][i]
        if ele == '#':
            temp.append('#')
            j += 1
        elif ele == 'b' or ele == 'c':
            for k in verticle_x_y_start:
                if k[0] == j and k[1] == i:
                    leng = k[2]
                    verticle_x_y_start.remove([j, i, leng])
                    char_cnt = 0
                    while char_cnt < leng:
                        temp.append(words[leng][char_cnt])
                        j += 1
                        char_cnt += 1
                    del words[leng]
        else:
            temp.append('-')
            j += 1
    resv.append(''.join(temp))
    i += 1

# pprint(resv)

transversed = []

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(resv[j][i])
    transversed.append(''.join(temp))

# pprint(transversed)


res = []

for i in range(n):
    temp_res = []
    for j in range(m):
        hh = resh[i][j]
        vv = transversed[i][j]
        if hh == vv:
            temp_res.append(hh)
        elif (hh == '-') and (vv in "qwertyuiopasdfghjklzxcvbnm"):
            temp_res.append(vv)
        elif (vv == '-') and (hh in "qwertyuiopasdfghjklzxcvbnm"):
            temp_res.append(hh)
        else:
            print('Invalid')
            exit()
    res.append(''.join(temp_res))


for i in res:
    print(i)
