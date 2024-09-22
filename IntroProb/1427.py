import sys

N= str(sys.stdin.readline())
Nl=[N[i] for i in range(len(N)-1)]


Nl.sort()
Nl=list(reversed(Nl))

for i in Nl:
    print(i, end='')