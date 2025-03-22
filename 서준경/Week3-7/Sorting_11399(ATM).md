For practicing Sorting Algorithm
```python
import sys
# from collections import deque
# from queue import PriorityQueue
# sys.stdin.readline().strip()
# print = sys.stdout.write

# Using Insertion Sort

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

if N > 1:
    # Using binary search
    for pivot in range(1, N):
        start = 0
        end = pivot - 1
        while start <= end:
            mid = (start + end) // 2
            if numbers[pivot] > numbers[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        targetnum = numbers[pivot]
        for j in range(pivot, start, -1):
            numbers[j] = numbers[j - 1]
        numbers[start] = targetnum

# print(numbers)

result = 0
for i in range(len(numbers)):
    result += numbers[i] * (N-i)
print(result)
```
