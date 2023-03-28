with open('매수종목1.txt','r') as f:
    lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()  #'\n'
    codes.append(code)

print(codes)