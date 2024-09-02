import sys

dict_ = {'a':3,'b':3,'c':3, 'd':4,'e':4,'f':4, 'g':5,'h':5,'i':5,
         'j':6,'k':6,'l': 6, 'm':7,'n':7,'o':7, 'p':8,'q':8,'r':8,'s':8,
         't':9,'u':9,'v': 9, 'x':10,'y':10,'w':10,'z':10}

input = sys.stdin.readline()

count=0

input=input.lower()

for i in input:
    if i in dict_:
        count+= dict_[i]
print(count)