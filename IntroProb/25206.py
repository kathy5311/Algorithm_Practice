import sys

grade_dict ={
    'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5
    ,'D0':1.0, 'F':0.0
}
total=0
total_score=0
for _ in range(20):
    subject, score, grade = list(map(str,sys.stdin.readline().split()))
    if grade in grade_dict:
        total+=float(score)*(grade_dict[grade])
    elif grade == 'P':
        continue
    total_score+=float(score)

total_grade=total/total_score
print(total_grade)

