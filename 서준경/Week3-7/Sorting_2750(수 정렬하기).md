For practicing Sorting Algorithm, 
```python
import sys
# from collections import deque
# from queue import PriorityQueue
# sys.stdin.readline().strip()
# print = sys.stdout.write

# Using BubbleSort
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)


N = int(sys.stdin.readline().strip())

nums = [int(sys.stdin.readline().strip()) for i in range(N)]
for i in range(N):
    if N == 1:
        break
    for j in range(N-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = swap(nums[j], nums[j+1])
for i in nums:
    print(i)
```
