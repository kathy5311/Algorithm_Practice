'''
card = ['A','B','C','D']
path =[0]*3
cnt=0
def dfs(start,level):
    global cnt
    cnt+=1
    if level==3:
        print(*path)
        return
    
    for i in range(len(card)):

        path[level]=card[i]
        dfs(i+1,level+1)
        path[level]=0
    
dfs(0,0)
print(cnt)'''
# 중복 조합
# 중복 허용 O, 순서가 달라도 같은 경우의 수

card = ['A', 'B', 'C', 'D']
path = [0]*3

def dfs(level, start):
		# 3장 모두 뽑았으면 출력하고 리턴
    if level == 3:
        print(*path)
        return 
    for i in range(start, 4):
        path[level] = card[i]  # 카드 뽑기
        dfs(level+1, i)  # 직전에 뽑은 카드와 같은 인덱스부터 카드 뽑기
        path[level] = 0  # 리턴 이후 뽑은 카드 초기화

dfs(0, 0)

