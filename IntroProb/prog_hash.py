# 전화번호 목록-for문 ver
'''
phone_book = ["119", "97674223", "1195524421"]
phone_book.sort()
print(phone_book)

for idx in range(len(phone_book)-1):
    if phone_book[idx]==phone_book[idx+1][:len(phone_book[idx])]:
        print(False)

print(True)'''

# hasp map ver
phone_book = ["119", "9767", "24421"]

hash={}
for num in phone_book:
    hash[num]=1

for num in phone_book:
    temp=''
    for idx in num:
        temp+=idx
        if temp in hash and temp != num:
            print(False)
            exit()
print(True)
