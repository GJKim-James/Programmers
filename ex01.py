# 해시 완주하지 못한 선수

# 마라톤 미완주자는 무조건 1명
# 해시 값은 값에 따라 중복되지 않는 숫자 값이 생성됨
# 참여자의 해시 값을 모두 합한 값이 1000이라면, 완주자는 1명만 부족하기에 1000보다 작은 값이 나옴
# 참여자 - 완주자 = 100이라면, 해시 값이 100인 사람이 미완주자임

# 이 로직의 문제점? 미완주자가 2명 이상이면, 미완주자를 찾지 못함

def solution(participant, completion):
    # 해시 값의 총 합을 저장할 변수
    tmp = 0

    # 해시 값과 이름이 저장되는 키, 값 구조 cf. dic = {'key':'value', 'key':'value', ...}
    dic = {}

    # 참여자 전체 해시 값 더하기 및 이름(해시 값) 저장하기
    for p in participant:
        # 전체 참여자 이름과 해시 값 저장하기
        dic[hash(p)] = p  # dic['key'] = 'value', 여기서는 dic = {해시 값, 참여자 이름}이 형성된다.

        # 전체 해시 값 저장하기
        tmp += int(hash(p))  # 원래 hash 값은 16진수이기 때문에 int로 변환해주는 것이 좋다.

    # 완주자 전체 해시 값 빼기
    for com in completion:
        # 최종 남은 값이 마지막 1명 남은 미완주자
        tmp -= hash(com)

    # 해시 값으로 미완주자 이름 가져오기
    return dic[tmp]
