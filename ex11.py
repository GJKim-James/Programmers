# 완전탐색 카펫

# x는 가로 길이, y는 세로 길이
# xy = brown + yellow
# x + y = (brown + 4) / 2

# brown = 2x + 2y - 4
# yellow = (x - 2)(y - 2) => 결국, brown = 2x + 2y - 4

# brown = 10, yellow = 2
def solution(brown, yellow):
    answer = []

    xy = brown + yellow

    # 전체 네모칸 만큼 반복하기
    for y in range(1, xy + 1):

        # x 길이를 구하기 위해 xy를 y로 나눠 떨어지는 것만 계산하기
        if (xy / y) % 1 == 0:

            x = xy / y

            # 문제에서 전제 조건으로 가로 길이(x)가 세로 길이(y)보다 크거나 같다고 함
            if x >= y:

                # brown 구하는 식을 이용해서 x, y 구하기
                if brown == 2 * x + 2 * y - 4:
                    return [x, y]
