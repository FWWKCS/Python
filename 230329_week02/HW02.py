class SoldOutError(Exception):
    pass

count = 10
while count != 0 :
    print('몇 마리를 주문할 지 숫자를 입력하세요')
    print(f'앞으로 {count}마리 남았습니다 : ')
    
    val = input()
    try : val = int(val)
    except ValueError as val :
        print('잘못된 값을 입력하였습니다')
        continue
    if (val > count) :
        print("남은 재고량보다 많은 양을 주문해 남은 양 만큼만 주문되었습니다")
        count = 0
    else :
        print('주문이 완료되었습니다')
        count -= val

print('재고가 소진되어 더 이상 주문을 받지 않습니다')
raise SoldOutError()
    