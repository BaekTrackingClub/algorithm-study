```python
import sys
# sys.stdin.readline().strip()

S, P = list(map(int, sys.stdin.readline().strip().split()))
dna = sys.stdin.readline().strip()
# A C G T
base = list(map(int, sys.stdin.readline().strip().split()))
#print(S, P, base, dna)
result = 0
bef = [0,0,0,0]
for idx1 in range(S - P + 1):
    idx2 = idx1 + P
    if idx1 != 0:
        bef[0] += int(dna[idx2-1] == "A") - int(dna[idx1-1] == "A")
        bef[1] += int(dna[idx2-1] == "C") - int(dna[idx1-1] == "C")
        bef[2] += int(dna[idx2-1] == "G") - int(dna[idx1-1] == "G")
        bef[3] += int(dna[idx2-1] == "T") - int(dna[idx1-1] == "T")
    else:
        bef[0] = dna[idx1:idx2].count("A")
        bef[1] = dna[idx1:idx2].count("C")
        bef[2] = dna[idx1:idx2].count("G")
        bef[3] = dna[idx1:idx2].count("T")
    ifpos = all([base[i] <= bef[i] for i in range(4)])
    #print(dna[idx1:idx2].count("A"), dna[idx1:idx2].count("C"), dna[idx1:idx2].count("G"), dna[idx1:idx2].count("T"))
    if ifpos:
        result += 1

print(result)
```
