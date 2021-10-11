# 세탁소 사장 동혁

changes = [25, 10, 5, 1]  # 거슬러줄 동전들

num = int(input())  # 반복 횟수
coin_list = []
exchange_list = []
# coin_list.append(exchange_list)

# for j in range(money):
for i in range(num):
    money = int(input())  # 반복 횟수만큼 입력받음
    # for j in changes:

    for j in range(len(changes)):  # 4번 거슬러준다
        coin_list.append(money // changes[j])
        money %= changes[j]
        # print(coin_list)

        # ZeroDivisionError: integer division or modulo by zero
        # coin_list.append(money // i)

        # print(ex)
        # coin_list.append(ex)
        # # money %= i

for i in range(num):
    for j in coin_list:
        print(j, end=' ')
