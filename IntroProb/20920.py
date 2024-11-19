import sys

N,M = list(map(int, sys.stdin.readline().split()))

word_dict={}
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        pass

    else:
        if word not in word_dict:
            word_dict[word]=1
        elif word in word_dict:
            word_dict[word]+=1


a=sorted(word_dict.items(), key=lambda x :(-x[1], -len(x[0]),x[0]))

for i in a:
    print(i[0])
