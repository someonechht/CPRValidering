#cpr test digits
#1010174003 fremtiden
#3213982159 invalid dato
#1234567890 invalid modulu 11
#2902982135 valid cpr
from datetime import datetime
cpr = 0
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)

moduloCheck = True #modulu 11 check
dateCheck = True   #date existen check
cpr10Check = True  #10 diget check
futureCheck = True #birthday not from future check
intCheck = True    #enter digtet check

timeDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
year = 2000
month = 12
day = 30
d = datetime(year, month, day)

run = True  #While loop for validate
Run = True  #Bool for moduleCheck and dateCheck to run
error = False

def validate(cpr):
    cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')

    #Quit commands
    if cpr == 'quit' or cpr == 'exit' or cpr == 'kill':
        global run
        run = False
        print('I quit')
        exit()

    #log commands
    if cpr == 'new log' or cpr == 'clear log' or cpr == 'clear' or cpr == 'log clear':
        f = open('log', 'w')
        f.write('ERROR LOG\n')
        f.close()
        print('Clear log successful')
        return

    if '-' or '/' or ' ' in cpr:
        cpr = cpr.replace('-', '')
        cpr = cpr.replace('/', '')
        cpr = cpr.replace(' ', '')

    if len(cpr) != 10:
        global cpr10Check
        global error
        global Run
        print('Der skal være 10 cifre i dit CPR nummer')
        error = True
        cpr10Check = False
        Run = False

#       raise Exception("Der skal være 10 tal i dit CPR")
    try:
        int(cpr)
    except:
        global intCheck
        Run = False
        intCheck = False
        error = True
        print('Dit cpr skal bestå af tal')


    #køre validering
    if Run == True:
        int(cpr)
        listCpr = list(cpr)
        sumCpr = 0
        for x in range (0,10):
            sumCpr += (checkDiget[x]* int(listCpr[x]))

        #modulo 11 kontrol
        if (sumCpr % 11) != 0:
            global moduloCheck
            moduloCheck = False
            error = True
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
            global d
            d = datetime(year, month, day)
            dateCheck = True
        except:
            error = True
            dateCheck = False

        if d.date() > datetime.today().date():
            global futureCheck
            futureCheck = False
            error = True





        if moduloCheck == True:
            if dateCheck == True:
                if futureCheck == True:
                    print('Fødselsdato: ' + str(day) + '-' + str(month) + '-' + str(year))

                    #køn
                    if int(cpr[-1]) % 2 == 0:
                        print('Køn: Kvinde')
                    else:
                        print('Køn: Mand')
                    print('CPR godkend')

                else:
                    print('Invalid CPR')
            else:
                print('Invalid CPR')
        else:
            print('Invalid CPR')
    #write log file
    if error == True:
        f = open('log', 'a')
        f.write('\n' + str(timeDate))
        if cpr10Check == False:
            f.write('\n' + 'CPR length error \nThe CPR does not contain 10 digit\n')
        if intCheck == False:
            f.write('\n' + 'integer error  \nThe CPR is not a integer\n')
        if dateCheck == False:
            f.write('\n' + 'dateCheck error \nThe date does not exist\n')
        if moduloCheck == False:
            f.write('\n' + 'moduloCheck error \nThe modulo does not mach up with modulo 11\n')
        if futureCheck == False:
            f.write('\n' + 'futureCheck error \nThe time entered is from the future\n')
        f.close()

while run == True:
    validate(cpr)


# print(modulo)
