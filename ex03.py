# 해시 위장

# clothes 예시 : [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):

    # headgear, eyewear, face 등 옷 종류별로 구분하기
    clothesTypeMap = {}

    for clothe, clothesType in clothes:
        print("clothe : ", clothe)
        print("clothesType : ", clothesType)

        # 옷 종류가 늘어날 때마다 값을 1씩 더하기
        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1  # clothesType이 0이면 0입력
        print("clothesTypeMap : ", clothesTypeMap)

        # 반복문 결과값
        # clothe : yellowhat
        # clothesType : headgear
        # clothesTypeMap : {'headgear': 1}

        # clothe : blue_sunglasses
        # clothesType : eyewear
        # clothesTypeMap : {'headgear': 1, 'eyewear': 1}

        # clothe : green_turban
        # clothesType : headgear
        # clothesTypeMap : {'headgear': 2, 'eyewear': 1}

    # 옷을 하나만 입을 경우 계산하기
    answer = 1
    for clothesType in clothesTypeMap:
        print(clothesType)

        answer *= (clothesTypeMap[clothesType] + 1)
        print(answer)

        # 반복문 결과값
        # headgear
        # 3
        # eyewear
        # 6

    # 옷을 아무것도 입지 않는 경우 빼기(문제 조건에서 최소 하나의 옷은 항상 입는다고 했기 때문)
    return answer - 1
