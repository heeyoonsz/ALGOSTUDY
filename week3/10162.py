# 전자레인지

sec = [300, 60, 10]
time = int(input())
#count
count_list = []
# while True:

for i in sec:
    if time % 10 == 0:
        count_list.append(time//i) # 130을 300으로 나눈 몫
        time%=i # 130을 300으로 나눈 나머지

    # count += time // i
    # namoji = time // i
    # print('count=', count)
    # print('나머지=', namoji)

    # time=time%i
    # print('time=', time)
    # count.append(count_list)
    # print(count,end=' ')
    # if time % 10 != 0:

    else:
        print('-1')
        exit(0)

#print(count_list,end='')

for i in count_list:
    # print(count_list[i],end=' ')
    print(i,end=' ')


# count += time // a  # 나머지 없는 몫
# time = time % a
# print(count)
# print(time)
# time = time % b  # 나머지
# count += time // b
# print(count)
# print(time)
#
# time = time % c  # 나머지
# count += time // c
# print(count)
# print(time)
