import csv
from datetime import datetime, timedelta

# Keuzemenu voor stap 9
Keuzemenu = "Keuzemenu:\n 0. Stoppen\n 1. Boek lenen\n 2. Boek terugbrengen"

CatalogusFile = "Bijlage 3 - Catalogus.csv"
LedenFile = "Bijlage 2 - Leden.csv"

def uitlezenDB(fn,st): #fn = filename, st = scheidingsteken
    tempList = []
    with open(fn,mode='r',newline='') as temp:
        tempCSV = csv.reader(temp, delimiter=st)
        for line in tempCSV:
            tempList.append(line)
    return tempList

def updatenDB(fn,st,data): #fn = filename, st = scheidingsteken
    with open(fn,mode='w',newline='') as temp:
        tempCSV = csv.writer(temp, delimiter=st)
        tempCSV.writerows(data)

while True:
    #stap 1 - Inladen van de databases Catalogus en Leden en het maken van variabelen pogingen
    Catalogus = uitlezenDB(CatalogusFile,';')
    Leden = uitlezenDB(LedenFile,';')
    pogingen = 0

    #Stap 2 - De gebruiker vragen op gebruikersnaam
    gebruikersnaam = input("Wat is uw gebruikersnaam? ")

    #Stap 3/4 - For loop om door de database Leden te loopen
    for line in Leden:
        #Stap 5 - Controleren of de gebruikersnaam voorkomt
        if gebruikersnaam in line:
            volledigeNaam = line[0] + " " + line[1]
            #Stap 7.1 - Pogingen mag niet groter worden dan 3
            while pogingen < 3:
                #Stap 6 - Vraag de gebruiker om een wachtwoord
                wachtwoord = input("Wat is uw wachtwoord? ")
                pogingen += 1
                #Stap 7 - Komt het wachtwoord overeen met het wachtwoord in de database Leden
                if wachtwoord == line[2]:
                    break
                #Stap 7.2 - Wachtwoord klopt niet, probeer opnieuw.
                else:
                    print("Wachtwoord komt niet overeen, probeer het opnieuw.")
            #Stap 7.3 - Wachtwoord klopt niet, gebruiker wordt afgemeld.
            else:
                print("Het wachtwoord klopt niet binnen 3 pogingen, u wordt afgemeld.")
                break

            #Stap 8 - Toon de geleende boeken
            if line[4] == "":
                print("U heeft nog geen geleende boeken.")
            else:
                line = line[4].split(',')
                print("U de volgende boeken heeft u al in bruikleen.")
                for i in range(len(line)):
                    print(" - "+line[i])

            while True:
                #Stap 9 - Toon het keuzemenu
                print(Keuzemenu)
                #Stap 10 - Vraag de gebruiker om een keuze:
                keuze = int(input("Wat is uw keuze? "))

                #Stap 11 - Als de keuze 0 is (stoppen):
                if keuze == 0:
                    #Terug naar stap 2
                    break

                #Stap 12 - Als de keuze 1 is (lenen):
                elif keuze == 1:
                    #Stap 12.1 - Vragen om een titel en een schrijver aan de gebruiker
                    titel = input("Geef de titel van het boek wat je wilt lenen: ")
                    schrijver = input("Geef de schrijver van het boek wat je wilt lenen: ")

                    deadline = (datetime.now() + timedelta(days=60)).strftime("%d-%m-%Y")

                    #Stap 12.2 - In de database Catalogus de gebruikersnaam noteren bij het boek
                    for i,line in enumerate(Catalogus):
                        if titel in line:
                            Catalogus[i][2] = volledigeNaam
                            Catalogus[i][3] = deadline
                            break
                    #Stap 12.3 - In de database Leden het juiste boek met deadline noteren bij het lid.
                    for j,line in enumerate(Leden):
                        if gebruikersnaam in line:

                            boekMetDeadline = titel + "|" + deadline
                            if line[4] == "":
                                Leden[j][4] += boekMetDeadline
                            else:   
                                Leden[j][4] += "," + boekMetDeadline
                            break

                #Stap 13 - Als de keuze 2 is (terugbrengen):
                elif keuze == 2:
                    #Stap 13.1 - Vragen welk boek de gebruiker wilt terugbrengen
                    titel = input("Geef de titel van het boek wat je wilt terugbrengen: ")
                    for i,line in enumerate(Leden):
                        #Stap 13.2 - Wordt het boek ook echt door deze persoon geleend?
                        if gebruikersnaam in line and titel in line[4]:
                            break
                    #Stap 13.3 - De gebruiker leent dit boek niet   
                    else:
                        print("Het boek wordt niet door u geleend.")
                        break

                    """
                    OPDRACHT: Voeg stap 13.4 t/m 13.6 hier toe (oranje)

                    """

                    #Stap 13.7 - Het lid uit de database Catalogus halen van het boek
                    for i,line in enumerate(Catalogus):
                        if titel in line:
                            Catalogus[i][2] = "-"
                            Catalogus[i][3] = "-"
                            break
                    #Stap 13.8 - Het verwijderen van het boek + deadline uit de database Leden
                    for j,line in enumerate(Leden):
                        if gebruikersnaam in line:
                            geleendeBoeken = line[4].split(',')
                            index = None
                            for x,boek in enumerate(geleendeBoeken):
                                if titel in boek:
                                    index = x
                            geleendeBoeken.pop(x)
                            Leden[j][4] = geleendeBoeken
                            break

                """
                OPDRACHT: Voeg alles toe wat hoort bij stap 14 (blauw)
                """

                """
                OPDRACHT: Voeg alles toe wat hoort bij stap 15 (rood)
                """

                #Stap 10.1 - Updaten bijde databases
                updatenDB(CatalogusFile,';',Catalogus)
                updatenDB(LedenFile,";",Leden)