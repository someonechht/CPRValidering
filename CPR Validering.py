from datetime import datetime
cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)
moduloCheck = False
dateCheck = False

def validate(cpr):
    int(cpr)
    if len(cpr) != 10:
        print('Der skal være 10 tal i dit CPR')
#        raise Exception("Der skal være 10 tal i dit CPR")
    else:
        listCpr = list(cpr)
        sumCpr = 0
        for x in range (0,10):
            sumCpr += (checkDiget[x]* int(listCpr[x]))

        #modulo 11 kontrol
        if (sumCpr % 11) != 0:
            global moduloCheck
            print('Ukorrekt CPR!')
        else:
            moduloCheck = True

        #dato kontrol
        global dateCheck
        global year
        global month
        global day
        year = int(cpr[4:6])
        month = int(cpr[2:4])
        day = int(cpr[0:2])
        cpr6 = int(cpr[6])
        if cpr6 <= 3:
            year = year + 1900

        elif cpr6 == 4 and year <= 36:
            year = year + 2000

        elif cpr6 == 4 and year > 36:
            year = year + 1900

        elif 4 < cpr6 < 9 and year <= 57:
            year = year + 2000

        elif 4 < cpr6 < 9 and year > 57:
            year = year + 1800

        elif cpr6 == 9 and year <= 36:
            year = year + 2000

        else:
            year = year + 1900

        try:
            datetime(year, month, day)
            print('Fødselsdato:' + str(day) +'-'+ str(month) +'-'+ str(year))
            dateCheck = True
        except:
            print('Ukorrekt CPR!')

        #gender
        if int(cpr[-1]) % 2 == 0:
            print('Køn: Kvinde')
        else:
            print('Køn: Mand')


    if moduloCheck == True:
        if dateCheck == True:
            print('CPR godkend')




validate(cpr)

# print(modulo)
