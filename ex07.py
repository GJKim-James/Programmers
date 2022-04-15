# 완전탐색 모의고사

def solution(answers):
    # 학생별 찍는 방식
    student1 = [1, 2, 3, 4, 5]  # 5개씩 반복
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개씩 반복
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개씩 반복

    # 점수 결과
    # 프로그래머스에서  return 값이 1, 2, 3으로 학생명을 표기했기 때문에 Key 값으로 1, 2, 3 사용
    result = {1: 0, 2: 0, 3: 0}  # Map 구조, {학생 번호(명), 정답 맞춘 수} 형태로 저장

    # 문제 답만큼 반복하기
    for i in range(len(answers)):

        # 학생 1의 찍는 방식은 5개씩 반복이라, % 5 연산을 사용하여 답 제공
        if student1[i % 5] == answers[i]:
            # 맞추면 정답 수 1씩 더하기
            result[1] += 1

        # 학생 2의 찍는 방식은 8개씩 반복이라, % 8 연산을 사용하여 답 제공
        if student2[i % 8] == answers[i]:
            # 맞추면 정답 수 1씩 더하기
            result[2] += 1

        # 학생 3의 찍는 방식은 10개씩 반복이라, % 10 연산을 사용하여 답 제공
        if student3[i % 10] == answers[i]:
            # 맞추면 정답 수 1씩 더하기
            result[3] += 1

    # 가장 많이 맞춘 정답 수 구하기
    top_score = max(result.values())

    answer = []

    # 학생은 3명, 학생 번호는 1번부터 3번까지이므로 range(1, 4)로 선언
    for i in range(1, 4):
        # 가장 많이 맞춘 정답 수와 학생 번호 비교해서
        if result[i] == top_score:
            # answer에 학생 번호 추가
            answer.append(i)

    return answer
