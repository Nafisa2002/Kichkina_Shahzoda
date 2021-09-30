from classlar import shahzoda, planeta, nuqta


test_case = int(input())

for i in range(test_case):
    x1, y1, x2, y2 = map(int, input().split())
    shahzod = shahzoda(x1, y1, x2, y2)
    sayyora_soni = int(input())
    n=0
    for k in range(sayyora_soni):
        x, y, r = map(int, input().split())
        sayyora = planeta(x, y, r)
        if shahzod.kesib_otadimi(sayyora):
            n+=1
        else: 
            n+=0
        
    print(n)