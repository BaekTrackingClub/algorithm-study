```python
import sys
from collections import deque
# sys.stdin.readline().strip()

N, L = list(map(int, sys.stdin.readline().strip().split()))
nums = list(map(int, sys.stdin.readline().strip().split())) # A_i
result = deque()

for i in range(N):
    while result and result[-1][0] > nums[i]:
        result.pop()
    result.append((nums[i], i))
    if result[0][1] <= i - L:
        result.popleft()
    print(result[0][0], end=' ')
```
