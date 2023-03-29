per = ["10.31","","8.00"]
newPer = []

for i in per:
    try : print(float(per))
    except TypeError :
        try : 
            print(float(i))
            newPer.append(float(i))
        except ValueError :
            print(0)
            newPer.append(0)

    
print(newPer)
    
    






