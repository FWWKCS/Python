for i in range(1,51):
    with open(f"{i}주차.txt",'w',encoding="utf-8") as f:
        f.write(f"- {i}주차 주간보고 -\n")
        f.write("부서 :\n")
        f.write("이름 :\n")
        f.write("업무 요약 :\n")