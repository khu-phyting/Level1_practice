# 1. 김씨와 이씨는 각각 몇 명인가요?
names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

count_Kim = 0
count_Lee = 0
for name in names:
    if "김" == name[0]:
        count_Kim += 1
        
for name in names:
    if "이" == name[0]:
        count_Lee += 1
        
print(count_Kim, count_Lee)
        

# 2. "이재영"이란 이름이 몇 번 반복되나요?
names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

count_LJY = 0
for name in names:
    if "이재영" in name:
        count_LJY += 1
        
print(count_LJY)

# 3. 중복을 제거한 이름을 출력하세요.
names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

for name in names:
    if name in names:
        names.remove(name)   # remove()함수 사용. 리스트.remove(값) 의 형태로 사용. 리스트 내부에 값을 지정해서 제거함.
        
print(names)

# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

for name in names:
    if name in names:
        names.remove(name)
        
print(sorted(names, reverse = True))       # sorted() 함수를 이용하여 한글을 사전순으로 오름차순으로 정렬.
                                           # sorted() 함수 내부에 키워드 reverse = True를 하면 내림차순으로 정렬함.
                                           # names.sort() 를 하면 왜 출력이 None이지,,,?
        
print()
print(names.sort(reverse=False))
