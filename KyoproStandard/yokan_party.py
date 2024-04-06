N, L = input().split()
# 切れ目の数
N = int(N)
# 一本の長さ
L = int(L)
# 何本の切れ目を入れるか
K = int(input())
# 切れ目の位置
A = list(map(int, input().split()))

# cutPositions = A + [0,L]
# cutPositions.sort()

# intervals = [cutPositions[i] - cutPositions[i-1] for i in range(1, N+2)]
# intervals.sort()
# score = sum(intervals[:N+2 - K - 1])

# print(score)

cut_points = [0, L] + A
intervals = [0] * (N+1)
result_intervals = [0] * (K+1)
score = 0

cut_points.sort()
for i in range(len(cut_points)-1):
    intervals[i] = cut_points[i+1] - cut_points[i]

# for i in range(intervals.length):
#     for j in range(intervals.length-i+1):
#         result_intervals[i] = sum(intervals[i:i+j])

def divide(target, count):
    for i in range(len(target)):
        result_intervals[count] = sum(intervals[0:i])
        print(sum(intervals[0:i]))
        if(count < K):
            divide(intervals[i:], count+1)
        else:
            score = max([score, min(result_intervals)])
            return
divide(intervals, 0)
print(result_intervals)
# print(score)

