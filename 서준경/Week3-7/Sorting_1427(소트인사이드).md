```python
import sys
# from collections import deque
# from queue import PriorityQueue
# sys.stdin.readline().strip()
# print = sys.stdout.write

# Using Selection Sort

N = sys.stdin.readline().strip()
numbers = [int(i) for i in N]

for pivot in range(len(numbers)-1):
    maxnum = numbers[pivot]
    maxidx = pivot
    for idx in range(pivot+1, len(numbers)):
        if numbers[idx] > maxnum:
            maxidx = idx
            maxnum = numbers[idx]
    temp = numbers[pivot]
    numbers[pivot] = numbers[maxidx]
    numbers[maxidx] = temp

for i in numbers:
    print(i, end="")
```
