""" 
[문제]
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

[예제 입력 1]
1 2

[예제 출력 1]
3
"""

print("===[2023-01-24 (화) #02]===")

output = print(sum(map(int, input().split())))


# print("===[2023-01-24 (화) #01]===")

# list = input().split()

# total = 0
# for v in list:
#   total += int(v)
# print(total)