```python
import sys
# from collections import deque
from queue import PriorityQueue
# sys.stdin.readline().strip()
print = sys.stdout.write

N = int(sys.stdin.readline().strip())
result = PriorityQueue()

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if not result.empty():
            print(str(((result.get())[1]))+'\n')
        else:
            print("0\n")
        continue
    else:
        result.put((abs(num), num))
```
