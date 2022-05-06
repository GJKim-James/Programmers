# 스택/큐 - 프린터

from collections import deque


# ex) priorities : [2, 1, 3, 2] / location : 2
def solution(priorities, location):
    # 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 확인할 변수
    answer = 0

    # deque 구조 만들기
    # 키(key) : [2, 1, 3, 2]으로 설정 / 값(value) : location과 매칭할 인덱스
    # myDeque 변수 값 : deque([(2, 0), (1, 1), (3, 2), (2, 3)])
    myDeque = deque([(v, i) for i, v in enumerate(priorities)])  # enumerate() 함수는 (index, '값')으로 형성되기 때문에 i, v

    print("myDeque : ", myDeque, "\n")

    idx = 0
    while myDeque:

        idx += 1

        # 첫 번째 값 가져오고, myDeque에서 삭제하기
        firstData = myDeque.popleft()
        print(idx, " myDeque : ", myDeque)
        print("firstData : ", firstData)

        # myDeque 데이터가 존재하고, 우선 순위가 가장 높은 데이터가 가져온 데이터보다 크다면
        if myDeque and max(myDeque)[0] > firstData[0]:

            # 가져온 데이터를 가장 뒤에 추가하기
            # myDeque 변수 값 : deque([(3, 2), (2, 3), (2, 0), (1, 1)])
            myDeque.append(firstData)

            print("myDeque : ", myDeque, "\n")

        else:
            # 우선 순위가 가장 높은 것을 찾은 상태에서 location에 해당되는 값 찾기
            # 우선 순위 가장 높은 것 찾으면, 추가(append)하기 안하고 멈춤
            # 멈춘 상태 : deque([(2, 3), (2, 0), (1, 1)]) / firstData : (3, 2)

            # 대기열 값 구하기
            answer += 1
            print("answer : ", answer, "\n")

            # 인쇄하고자 하는 문서 찾으면, 더 이상 반복하지 않기
            if location == firstData[1]:
                break

    return answer  # 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 출력
