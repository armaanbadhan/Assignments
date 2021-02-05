for i in range(int(input())):
    if i&1:
        print(*[5*i + 1, 5*i + 2, 5*i + 3, 5*i + 4, 5*i + 5][::-1])
    else:
        print(*[5*i + 1, 5*i + 2, 5*i + 3, 5*i + 4, 5*i + 5])