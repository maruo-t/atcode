N = int(input())
t = 0
x = 0
y = 0
for i in range(N):
    t_, x_, y_ = map(int, input().split())
    if (t_ - t) < abs(x_ - x) + abs(y_ - y) or (t_ - t) % 2 != (abs(x_ - x) + abs(y_ - y)) % 2:
        print("No")
        exit()
    t = t_
    x = x_
    y = y_
print("Yes")
