# 정렬 k번째 수

# 예시 : array [1, 5, 2, 6, 3, 7, 4]	/ commands [[2, 5, 3], [4, 4, 1], [1, 7, 3]] / return [5, 6, 3]

def solution(array, commands):
    answer = []

    # commands 갯수 세기
    cmd_length = len(commands)
    print("cmd_length : ", cmd_length)  # cmd_length : 3

    # commands 갯수만큼 반복
    for i in range(cmd_length):  # range(3) : 0, 1, 2

        # 첫 번째 배열값과 두 번째 배열값에 해당되는 범위를 commands에서 가져오기
        # 인덱스는 0부터 생성되기 때문에 첫 번째 인덱스 값을 -1 해준다
        arr_list = array[commands[i][0] - 1:commands[i][1]]
        print([i+1], "arr_list : ", arr_list)

        # 결과값
        # [1] arr_list: [5, 2, 6, 3]
        # [2] arr_list: [6]
        # [3] arr_list: [1, 5, 2, 6, 3, 7, 4]

        # 가져온 배열을 정렬
        arr_list.sort()
        print([i+1], "정렬된 arr_list : ", arr_list)
        print("----------------------------------")

        # 정렬된 데이터의 k번째 값 가져오기
        answer.append(arr_list[commands[i][2] - 1])
        print("answer : ", answer)

    return answer
