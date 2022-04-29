# 정렬 H-Index

# citations 예시 : [3, 0, 1, 6, 5]
def solution(citations):

    print(citations)
    print("'citations' type : ", type(citations))
    citations.sort(reverse=True)

    print("정렬된 citations : ", citations)  # [6, 5, 3, 1, 0]

    # H-Index(H 지수)는 게재된 논문의 수보다 인용자 수가 작아진 값을 의미
    # 3, 0, 6, 1, 5 -> 5편 논문이라면 인용 수는 5 이상 나와야 함
    # 5 이상이 되지 않는 인용 수는 3, 1, 0이며, 그 중 가장 큰 수가 3임
    for idx, citation in enumerate(citations):

        print("idx : ", idx, ", citation : ", citation)

        # 논문 수가 인용 수보다 작으면 값 가져오기
        # idx는 0부터 시작 >= 사용
        if idx >= citation:
            return idx

    return len(citations)
