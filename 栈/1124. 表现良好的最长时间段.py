hours = [9, 9, 6, 0, 6, 6, 9]

arr = []
for val in hours:
    if val > 8:
        arr.append(1)
    else:
        arr.append(-1)

prefixSum = []  # 前缀和数组
cur_sum = 0
for val in arr:
    prefixSum.append(cur_sum)
    cur_sum += val
prefixSum.append(cur_sum)

stk = []
for i in range(len(prefixSum)):
    if len(stk) == 0 or prefixSum[stk[-1]] > prefixSum[i]:
        stk.append(i)  # 因为最终需要的答案是最长距离,需要下标来计算,所以这里存储下标

print(prefixSum)
print(stk)

res = 0
# 逆向遍历prefixSum
for j in range(len(prefixSum) - 1, -1, -1):
    # 成立的话, (stk[-1], j)是一个候选项
    while len(stk) != 0 and prefixSum[j] > prefixSum[stk[-1]]:
        res = max(res, j - stk[-1])
        stk.pop()

# print(res)
