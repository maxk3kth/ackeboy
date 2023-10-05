""" Importerar vår fil med felhantering för namn och personnummer """
import felhantering

class Student:
    """ Introducerar en class. Student. där man kan spara förnamn, efternamn och personnummer i de tre
    attributerna. """
    
    def __init__(self, förnamn, efternamn, personnummer):
        """ konstruktorn som anropas när vi lägger till ny student.
        Tilldelar parametrar: förnamn(str), efternamn(str), personnummer(int)"""
        
        self.förnamn = felhantering.bokstav("Vad är studentens förnamn? ")
        self.efternamn = felhantering.bokstav("Vad är studentens efternamn? ")
        self.personnummer = felhantering.siffra("Vad är studentens personnummer? ")
        print("Studenten är tillagd!")
        
    def __str__(self):
        """ __str__ formulerar hur vår utskrift kommer att se ut när den printas. """

        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + str(self.personnummer)

class School:
    """Klass vid namn School som sparar information om studenter."""

    students = []
    students.append(Student("förnamn", "efternamn", "personnummer"))
    students.append(Student("förnamn", "efternamn", "personnummer"))
    students.append(Student("förnamn", "efternamn", "personnummer"))

    print("Här är alla studenter på KTH:")

    for student in students: # Taget från OLI sidorna
        print(student)


