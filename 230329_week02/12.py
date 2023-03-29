# 예외처리

per = ["10.31","","8.00"]

for i in per:
    try : print(float(i))
    except ValueError:
        print('0')

