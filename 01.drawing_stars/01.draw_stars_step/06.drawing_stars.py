# 별을 그릴 줄의 개수를 입력 받아서 그리기

num_lines = int(input('별의 줄 수를 입력하세요: '))

for i in range(num_lines):
    print((' ' * (num_lines - i - 1)) + '*' * (i*2+1))  