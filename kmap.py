# 정사각형의 테두리는 up,down,left,right를 편하게 사용하기위해 임의로 추가했다.
idx_list = [[10, 2, 6, 14, 10, 2],
            [8, 0, 4, 12, 8, 0],
            [9, 1, 5, 13, 9, 1],
            [11, 3, 7, 15, 11, 3],
            [10, 2, 6, 14, 10, 2],
            [8, 0, 4, 12, 8, 0]]

# term이 없으면 0 있으면 1, don't care term은 2로 표현한다.
k_map = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0], ]

#
term_idx = [["A'","B'","C'","D'"],["A'","B'","C'","D",],["A'","B'","C","D'"],["A'","B'","C","D"],
            ["A'","B","C'","D'"],["A'","B","C'","D"],["A'","B","C","D'"],["A'","B","C","D"],
            ["A","B'","C'","D'"],["A","B'","C'","D"],["A","B'","C","D'"],["A","B'","C","D"],
            ["A","B","C'","D'"],["A","B","C'","D"],["A","B","C","D'"],["A","B","C","D"]]

# term의 idx_list의 index를 input으로 받는다.
input_term_list = list(map(int, input().split()))
input_term_list.sort()

# 일반 term은 1로 저장, don't care term은 2로 저장
for idx in input_term_list:
    for i in range(6):
        for j in range(6):
            if idx_list[i][j] == idx: k_map[i][j] = 1

# 짝 지어지는 term들을 모을 리스트
term_list = []
# 첫번째 반복
for i in range(1, 5):
    for j in range(1, 5):
        if k_map[i][j] == 1:

            up = k_map[i - 1][j]
            down = k_map[i + 1][j]
            left = k_map[i][j - 1]
            right = k_map[i][j + 1]

            check_row_idx_head = i
            check_row_idx_tail = i+1
            check_col_idx_head = j
            check_col_idx_tail = j+1

            if up == 1 : check_row_idx_head -= 1
            if down == 1 : check_row_idx_tail += 1
            if up == 1 and down == 1 :
                check_row_idx_head = 0
                check_row_idx_tail = 5

            if left == 1 : check_col_idx_head -= 1
            if right == 1 : check_col_idx_tail += 1
            if left == 1 and right == 1 :
                check_col_idx_head = 0
                check_col_idx_tail = 5

            term = []

            # 상,하,좌,우 모두 0인경우 자기자신만 추가하고 k_map에서 제거한 뒤 term_list에 집어넣는다.
            if up == 0 and down == 0 and left == 0 and right == 0:
                term.append(idx_list[i][j])
                term_list.append(term)
                k_map[i][j] = 2
                continue

            # 위에서 하나라도 주위에 1이 발견될 경우 이 if문은 실행될 수 없다.
            if (check_row_idx_head == (check_row_idx_tail-1) and check_col_idx_head == (check_col_idx_tail-1)) and (up == 2 or down == 2 or left == 2 or right == 2):
                if up == 2 : check_row_idx_head -= 1
                if down == 2 : check_row_idx_tail += 1
                if up == 2 and down == 2 :
                    if check_row_idx_tail == 5:
                        check_row_idx_head -= 1
                    else:
                        check_row_idx_tail += 1

                if left == 2 : check_col_idx_head -= 1
                if right == 2 : check_col_idx_tail += 1
                if left == 2 and right == 2 :
                    if check_col_idx_tail == 5:
                        check_col_idx_head -= 1
                    else:
                        check_col_idx_tail += 1

            # 반복문을 돌면서 해당하는 인덱스가 1이나 2인지를 확인한다. 만약 아니라면 False로 바꾼다.
            all_idx_is_one_or_two = True
            for a in range(check_row_idx_head, check_row_idx_tail):
                for b in range(check_col_idx_head, check_col_idx_tail):
                    if k_map[a][b] == 0:
                        all_idx_is_one_or_two = False

            # 반복문을 모두 돌았음에도 True인 경우, 즉 선택한 인덱스가 모두 1이나 2인 경우 term_list에 추가한다.
            if all_idx_is_one_or_two:
                for a in range(check_row_idx_head, check_row_idx_tail):
                    for b in range(check_col_idx_head, check_col_idx_tail):
                        k_map[a][b] = 2 # 한번 선택됐으니 또다시 꼭 선택될 필요가 없으므로 2로 바꿔준다.(나중에 필요할 수도 있음)
                        if a == 0 : k_map[4][b] = 2
                        if b == 0 : k_map[a][4] = 2
                        term.append(idx_list[a][b])

                term_list.append(term)

                print(term_list)
                for line in k_map: print(line)
                print()


#모든 반복이 끝났으면 해당하는 term들을 출력한다.
final2 = []
for term in term_list:
    result = []
    remove_set = []
    for idx in term:
        for word in term_idx[idx]:
            if word not in result:
                result.append(word)

    if "A" in result and "A'" in result :
        remove_set.append("A")
        remove_set.append("A'")

    if "B" in result and "B'" in result :
        remove_set.append("B")
        remove_set.append("B'")

    if "C" in result and "C'" in result :
        remove_set.append("C")
        remove_set.append("C'")

    if "D" in result and "D'" in result :
        remove_set.append("D")
        remove_set.append("D'")

    final = [i for i in result if i not in remove_set]
    final.sort()
    final2.append(final)

for word in final2[0]:
    print(word,end="")
for words in final2[1:]:
    print('+',end="")
    for word in words:
        print(word,end="")