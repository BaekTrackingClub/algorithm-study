```python
import sys
# from collections import deque
# from queue import PriorityQueue
# sys.stdin.readline().strip()
# print = sys.stdout.write


N = int(sys.stdin.readline().strip())

nums = [(int(sys.stdin.readline().strip()), i) for i in range(N)]
sortednum = sorted(nums)

maxnum = 0
for i in range(N):
    if maxnum < sortednum[i][1] - i:
        maxnum = sortednum[i][1] - i

print(maxnum + 1)
```
