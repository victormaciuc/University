

class text:

    def __init__(self, sursa, cuvant, destinatie, traducere):
        self.__sursa = sursa
        self.__cuvant = cuvant
        self.__destinatie = destinatie
        self.__traducere = traducere

    def get_sursa(self):
        return self.__sursa

    def get_cuvant(self):
        return self.__cuvant

    def get_destinatie(self):
        return self.__destinatie

    def get_traducere(self):
        return self.__traducere

    def __str__(self):
        return self.get_sursa() + '    ' + self.get_cuvant() + '    ' + self.get_destinatie() + '    ' + self.get_traducere()

    def __eq__(self, other):
        return self.get_cuvant() == other.get_cuvant() and self.get_traducere() == other.get_traducere()