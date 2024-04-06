N,A,B = input().split()
N = int(N)
A = int(A)
B = int(B)
total = 0
for i in range(1,N+1):
    if A <= sum(list(map(int, list(str(i))))) <= B:
        total += i
print(total)
