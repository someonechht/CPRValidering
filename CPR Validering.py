from datetime import datetime
# cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')
cpr = '1212075600'
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)



def validate(cpr):
    int(cpr)
    if len(cpr) != 10:
        raise Exception("Der skal være 10 tal i dit cpr")
    else:
        listCpr = list(cpr)
        sumCpr = 0
        for x in range (0,10):
            sumCpr += (checkDiget[x]* int(listCpr[x]))

        #modulo 11 kontrol
        if (sumCpr % 11) != 0:
            global modulo
            modulo = False
            print('Ukorrekt CPR!')
        else:
            modulo = True
            print('Dit CPR er godkendt')

        #dato kontrol
        year = int(cpr[4:6])
        month = int(cpr[2:4])
        day = int(cpr[0:2])
        if (cpr[6]) <= 3:
            year = year + 2000
        elif (cpr[6]) == 4 and if :
            year = year + 2000
        elif (cpr[6]) <= 3:
            year = year + 2000
        elif (cpr[6]) <= 3:
            year = year + 2000
        elif (cpr[6]) <= 3:
            year = year + 2000
        elif (cpr[6]) <= 3:
            year = year + 2000
        else (cpr[6]) <= 3:
            year = year + 2000



validate(cpr)
# print(modulo)
