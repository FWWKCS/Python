per = ["10.31", "", "8.00"]

for i in per:
    try : 
        print(float(per))
    except TypeError :
        try : print(float(i))
        except ValueError :
            print(0)
        else : print('실수가 정상 출력되었습니다')
    finally :
        print("per 값을 무관하게 출력합니다")