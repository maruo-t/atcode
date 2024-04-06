N = input()
N = int(N)
A = []
for i in range(N):
    A.append(int(input()))
A = list(set(A))
print(len(A))
