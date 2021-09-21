# 한수


# 한수인지 판단하는 함수


def hansu(num):
    # 1~99

    cnt = 0
    for i in range(1, num + 1):
        #if 를 안써줘서 list index out of range 오류남
        if i<100:
            cnt+=1

        else:
            a = list(map(int, str(i)))
            #if a[2] - a[1] == a[1] - a[0]:
            if a[1]==(a[0]+a[2])/2:
                cnt += 1

    return cnt


'''
       a=num//100
       print(a) # 2

       b=(num//10)%10
       print(b) #1

       c=num%10
       print(c) #0


       if (a-b)==(b-c):
           cnt+=1
       return (cnt)
'''

number = int(input())

##한자리수와 두자리수(1-99)는 자동으로 한수
if number < 100:
    print(number)

else :
    print(hansu(number))