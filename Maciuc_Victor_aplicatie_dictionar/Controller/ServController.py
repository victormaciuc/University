from Domain.Traduceri import *

class Controller:

    def __init__(self,repo,validation):
        self.repo = repo
        self.validation = validation

    def adauga_cuvant(self,sursa,cuvant,destinatie,traducere):
        '''

        Valideaza datele si creeaza obiectul pentru a l adauga in dictionar

        '''
        trad = text(sursa,cuvant,destinatie,traducere)
        self.validation.valideaza_traducere(trad)
        self.repo.adauga(trad)

    def traduceri_list(self,limba):
        '''

        :param limba: Limba de traducere
        :return: Lista de afisare in Ui
        '''
        final = []
        traducerii = self.repo.get_all()
        traducerii.sort(key=lambda x: x.get_sursa(), reverse=True)
        for trad in traducerii:
            if limba == trad.get_sursa():
                final.append(trad)
        return final

    def tradu_text(self,intrare,limba1,limba2,iesire):
        '''

        :param intrare: Numele fisierului de intrare
        :param limba1: Limba de intrare
        :param limba2: Limba de iesire
        :param iesire: Numele fisierului de iesire
        :return: textul tradus in iesire
        '''
        sursa = open(intrare,'r')
        final = open(iesire,'a')

        incercare = self.repo.get_all()

        for line in sursa:
            comp = line.strip().split(" ")
            for i in comp:
                gasit = 0
                for dictie in incercare:
                    if limba1 == dictie.get_sursa() and i == dictie.get_cuvant() and limba2 == dictie.get_destinatie():
                        gasit = 1
                        sal=dictie.get_traducere()
                    elif limba1 == dictie.get_destinatie() and i == dictie.get_traducere() and limba2 == dictie.get_sursa():
                        gasit = 2
                        sal2=dictie.get_cuvant()
                if gasit ==1 :
                    final.write(sal)
                elif gasit ==2:
                    final.write(sal2)
                else:
                    final.write("{" + i + "}" + " ")
            final.write("\n")
        sursa.close()
        final.close()

    def tranzitiv(self,cuv,limba1,limba2):
        '''

        Functia cauta traducerile in toate combinatiile posibile
        cuv = cuvantul ce trebuie tradus
        limba1 = limba care se da cuv
        limba2 = limba in care se cere traducere
        '''
        dictionar = self.repo.get_all()
        aux = []
        for dictie in dictionar:
            if limba1 == dictie.get_sursa() and limba2 == dictie.get_destinatie() and cuv == dictie.get_cuvant():
                aux.append(dictie.get_traducere())
            elif limba1 == dictie.get_destinatie() and limba2 == dictie.get_sursa() and cuv == dictie.get_traducere():
                aux.append(dictie.get_cuvant())
            else:
                if limba1 == dictie.get_sursa() and cuv == dictie.get_cuvant():
                    gasit = self.repo.cauta(dictie.get_traducere(),dictie.get_destinatie(),dictionar,limba2)
                    aux.append(gasit)
                elif limba1 == dictie.get_destinatie and cuv == dictie.get_traducere():
                    gasit = self.repo.cauta(dictie.get_cuvant(), dictie.get_sursa(), dictionar, limba1)
                    aux.append(gasit)
        return aux




