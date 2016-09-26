cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)

def validate(cpr):
    int(cpr)
    if len(cpr) != 10:
        raise Exception("Der skal være 10 tal i dit cpr")
    else:
        listCpr = list(cpr)
        for x in range (0,11):
            test = (checkDiget[x]* listCpr[x])
            print(test)


validate(cpr)


