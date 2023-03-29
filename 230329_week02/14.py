try :
    a = 4 / 0
except ZeroDivisionError as a :
    print('0으로 나눌 수 없습니다')

data = [1, 2, 3]

for i in range(5) :
    try : print(data[i])
    except IndexError :
        print('리스트 인덱스 값을 더 출력할 수 없습니다')