A = input()
B = input()
C = input()
X = input()
count = 0
for a in range(int(A)+1):
    for b in range(int(B)+1):
        for c in range(int(C)+1):
            if a * 500 + b * 100 + c * 50 == int(X):
                count += 1
print(count)
