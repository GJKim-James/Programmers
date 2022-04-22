# 에라토스테네스의 체(소수 찾기) 응용

import math


# 입력받은 숫자가 소수인지 판별
# 소수 : true | 소수 아니면 : false
def numberCheck(num):
    # 0, 1은 소수가 아님
    if num == 0 or num == 1:
        return False
    else:

        # 2부터 입력받은 숫자의 제곱값까지 반복
        # 입력받은 값이 10이면 10^2 100번 반복
        # 그러나 100은 2의 배수로 반복 1번하고 종료됨
        for i in range(2, int(math.sqrt(num)) + 1):
            print(i)
            # 입력받은 값이 2부터 시작해서 나눠 떨어지는지 체크
            if num % i == 0:
                return False
    return True


# 10은 1번만 반복하면 결과 나옴
print(numberCheck(10))
print("------------------")

# 값의 크기가 커질수록 연산의 범위가 증가됨
# 239번 반복 발생
print(numberCheck(1111111))
