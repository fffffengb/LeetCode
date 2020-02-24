from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        res = [0 for i in range(n)]
        for item in logs:
            cur = item.split(":")
            cur_id = int(cur[0])
            cur_time = int(cur[2])
            if cur[1] == "start":
                stk.append((cur_id, cur_time))
            else:
                finished_time = cur_time - stk.pop()[1] + 1
                res[cur_id] += finished_time
                if stk:
                    res[stk[-1][0]] -= finished_time

        return res



solution = Solution()
print(solution.exclusiveTime(3, ["2:start:0",
                                 "0:start:1",
                                 "0:start:2",
                                 "0:end:5",
                                 "1:start:6",
                                 "1:end:6",
                                 "0:end:9",
                                 "2:end:12"]))
