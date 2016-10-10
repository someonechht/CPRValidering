from datetime import datetime
cpr = 0
checkDiget = (4, 3, 2, 7, 6, 5, 4, 3, 2, 1)
moduloCheck = False
dateCheck = False
timeDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
run = True  #While loop for validate
Run = True  #Bool for moduleChecck and dateCheck to run

def validate(cpr):
    cpr = input('Indsæt dit cpr dd/mm/åå/xxxx f.eks. 1234567890: ')

    #Quit commands
    if cpr == 'quit' or cpr == 'exit' or cpr == 'kill':
        global run
        run = False
        print('I quit')
        exit()

    #log commands
    if cpr == 'new log' or cpr == 'clear log' or cpr == 'clear':
        f = open('log', 'w')
        f.write('ERROR LOG\n')
        f.close()
        print('Clear log successful')
        return

    if '-' or '/' in cpr:
        cpr = cpr.replace('-', '')
        cpr = cpr.replace('/', '')

    if len(cpr) != 10:
        global Run
        print('Der skal være 10 cifre i dit CPR nummer')
        f = open('log', 'a')
        f.write('\n' + str(timeDate) + '\n' + 'CPR length error \nThe CPR does not contain 10 digit\n')
        f.close()
        Run = False

#       raise Exception("Der skal være 10 tal i dit CPR")
    try:
        int(cpr)
    except:
        Run = False
        print('Dit cpr skal bestå af tal')
        f = open('log', 'a')
        f.write('\n' + str(timeDate) + '\n' + 'integer error  \nThe CPR is not a integer\n')
        f.close()

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
            dateCheck = True
        except:
            dateCheck = False
        f = open('log', 'a')
        if moduloCheck == True:
            if dateCheck == True:
                print('Fødselsdato: ' + str(day) + '-' + str(month) + '-' + str(year))
            #køn
                if int(cpr[-1]) % 2 == 0:
                    print('Køn: Kvinde')
                else:
                    print('Køn: Mand')

                print('CPR godkend')
            else:
                print('Invalid CPR')
                f.write('\n' + str(timeDate) + '\n' + 'dateCheck error \nThe date does not exist\n')
                print('dateCheck error')
        else:
            print('Invalid CPR')
            f.write('\n' + str(timeDate)+ '\n' + 'moduloCheck error \nThe modulo does not mach up with modulo 11\n')
            print('moduloError')
        f.close()


while run == True:
    validate(cpr)


# print(modulo)
