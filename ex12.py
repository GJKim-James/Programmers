# 데큐(Deque) 예제

from collections import deque

# 데큐(Deque) 데이터 생성하기
myDeque = deque([(1, "첫 번째"), (2, "두 번째"), (3, "세 번째"), (4, "네 번째"), (5, "다섯 번째")])

print("전체 데큐 : ", myDeque)

# 가장 왼쪽 내용 가져오기, 가져오면 현재 데큐에서 삭제됨
firstData = myDeque.popleft()

# 삭제된 데이터
print("왼쪽 첫 번째 데이커(데큐에서 삭제됨) : ", firstData)

print("현재 데큐 : ", myDeque)

# 방금 가져온 첫 번째 데이터 추가하기
myDeque.append(firstData)

# firstData가 데큐 가장 뒤에 추가됨
print("현재 데큐 : ", myDeque)
