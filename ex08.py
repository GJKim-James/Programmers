# 에라토스테네스의 체(소수 찾기)

import math

# 순서대로 정렬되어 있음을 가정
# pn(prime number; 소수)
pn = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# 최댓값
max_pn = max(pn)
print("max_pn : ", max_pn)

for i in pn:
    # 비교 숫자의 제곱근이 최댓값보다 작은 경우에만 소수 찾기 진행
    if math.sqrt(i) < max_pn:
        # 배수 삭제를 위해 전체 반복
        for j in pn:
            # 자기 자신을 제외하고, 배수인 항목 제거
            if j > i and j % i == 0:
                print("i : ", i, " / j : ", j)

                # 삭제하기
                pn.remove(j)
                print("pn : ", pn)
                print("---------------------------------------------------")

print("소수 : ", pn)
