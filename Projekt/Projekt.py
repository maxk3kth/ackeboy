# Max Karlsson 0302118534, 178 Periodiska systemet

import random
from random import randint
class Grundämne(): 
    """Delar in i filen i en klass med grundämnens namn respektive massa. """
    def __init__(self, grundämne_namn, grundämne_massa):
        self.grundämne_namn = grundämne_namn
        self.grundämne_massa = grundämne_massa
    def __str__(self): #Returnerar klassen i beteckning och massa.
        return f'Beteckning: {self.grundämne_namn} Massa: {self.grundämne_massa}'


def sortera_lista(): 
    """Importerar listan med grundämnen och sorterar efter deras massa. """ #Sorterar efter float och delar upp listan i rader
    grundämnen = []
    y = open("grundamne.txt")
    lines = y.readlines()
    for line in lines:
        temp = line.split(" ")
        if (temp[1] == ""):
            temp = line.split()
        grundämnen.append(Grundämne(temp[0], float(temp[1])))
    y.close()

    grundämnen.sort(key = lambda x: x.grundämne_massa)
    grundämnen[18], grundämnen[17] = grundämnen[17], grundämnen[18] #Manuell flytt av givna grundämnen som hamnat på fel plats.
    grundämnen[27], grundämnen[26] = grundämnen[26], grundämnen[27]
    grundämnen[52], grundämnen[51] = grundämnen[51], grundämnen[52]
    grundämnen[90], grundämnen[89] = grundämnen[89], grundämnen[90]
    grundämnen[92], grundämnen[91] = grundämnen[91], grundämnen[92]
    return grundämnen #returnar en lista som används till andra funktioner.


def print_sorterad_lista(grundämnen):
    """Skriver ut listan med grundämnen sorterad efter deras massa. """ #Skriver ut det som returnerats i klassen.
    for grundämne in grundämnen:
        print(str(grundämne))


def öva_atomnummer(grundämnen):
    """Skriver ut ett grundämnes beteckning och ber användaren mata in rätt atomnummer"""
    försök = 0
    position = randint(0, len(grundämnen))
    värde = grundämnen[position]
    print("Vad är atomnumret till: " + värde.grundämne_namn + "?")
    while försök < 3:
        försök = försök + 1
        try:
            siffra = int(input("Svar: "))
            if siffra == position + 1:
                print("Ja! Rätt svar är:", position + 1)
                break
            elif siffra != position + 1:
                print("Fel! Försök kvar:", 3 - försök)
                continue
        except ValueError:
            print("Fel! Tips använd en siffra, försök kvar:", 3 - försök)
            continue
    else: 
        print("Rätt nummer är:", position + 1)


def öva_namn(grundämnen):
    """Skriver ut ett grundämnes atomnummer och ber användaren mata in rätt beteckning"""
    försök = 0
    position = randint(0, len(grundämnen))
    värde = grundämnen[position]
    print("Vad är beteckningen till grundämnet med atomnumret: " , position + 1 ,"?") 
    while försök < 3:
        siffra = str(input("Svar: " ))
        försök = försök + 1
        if siffra == värde.grundämne_namn:
            print("Ja! Rätt svar är:" , värde.grundämne_namn)
            break
        elif siffra != värde.grundämne_namn:
            print("Fel! Försök kvar:", 3 - försök)
            continue
    else:
        print("Rätt beteckning är:", värde.grundämne_namn)


def öva_massa(grundämnen): 
    """Skriver ut de tre randomiserade altern användaren välja vilket ativen från listan och ber användaren matta in rätt alternativ till den visade beteckningen"""
    rätt_svar , svar_lista = slump_svar(grundämnen)
    print("0. Massan: " , svar_lista[0])
    print("1. Massan: " , svar_lista[1])
    print("2. Massan: " , svar_lista[2])
    answer = input(str("Vilken massa har " + rätt_svar.grundämne_namn + "? Välj ett av de tre alternativen ovan med siffor 0-2: "))
    if answer == str(svar_lista.index(rätt_svar.grundämne_massa)):
        print("Ja! Rätt Svar är alternativet med massan: "+ str(rätt_svar.grundämne_massa))
    else: 
        print("Fel svar! Rätt svar är alternativet med massan: "+ str(rätt_svar.grundämne_massa))


def slump_svar(grundämnen):
    """Väljer ut tre stycken randomiserade alternativ från grundämnen-listan""" #Skriver ut tre random massor från listan där en av dessa är rätt_svar och shufflar dessa.
    rätt_svar = grundämnen[random.randint(0, len(grundämnen))]
    fel_svar1 = grundämnen[random.randint(0, len(grundämnen))]
    fel_svar2 = grundämnen[random.randint(0, len(grundämnen))]
    svar_lista = [rätt_svar.grundämne_massa, fel_svar1.grundämne_massa, fel_svar2.grundämne_massa]
    random.shuffle(svar_lista)
    
    return rätt_svar, svar_lista


def main():
    """Huvudfunktion där användaren blir serverad en meny med olika alternativ som fungerar som genvägar till ovanliggande funktioner. """
    grundämnen = sortera_lista()
    while True:
        print("---------------Meny--------------")
        print("1. Skriv ut listan med grundämnen")
        print("2. Träna på atomnummer ")
        print("3. Träna på atombeteckningar")
        print("4. Träna på atommassa")
        print("5. Avsluta programmet ")
        print("---------------------------------")
        x = input("Vad vill du göra? ")
        if x == "1":
            print_sorterad_lista(grundämnen)
            main()
        elif x == "2":
            öva_atomnummer(grundämnen)
            main()
        elif x == "3":
            öva_namn(grundämnen) 
            main()
        elif x == "4":
            öva_massa(grundämnen)
            main()
        elif x == "5": 
            print("Programmet avslutas!")
            exit()
        else:
            print("Måste välja en siffra mellan 1 och 5!")
            continue 
main()