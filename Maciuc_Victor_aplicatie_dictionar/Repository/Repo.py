from Error import RepoError
from Domain.Traduceri import *

class Repository:

    def adauga(self,trad):
        '''

        Functia are rolul de a adauga in lista noul obiect cuvant , numit "trad"
        '''
        dictionar = open('dictionar.txt','r')
        for line in dictionar:
            comp = line.strip().split(' ')
            if comp[2] == trad.get_destinatie() and comp[3] != trad.get_traducere() and comp[1] == trad.get_cuvant():
                raise RepoError('cuvant deja existent!')
            if comp[2] == trad.get_destinatie() and comp[3] == trad.get_traducere() and comp[1] == trad.get_cuvant():
                raise RepoError('cuvant deja existent!')
        dictionar.close()
        cuv = trad.get_sursa() + ' ' + trad.get_cuvant() + ' ' + trad.get_destinatie() + ' ' + trad.get_traducere() + '\n'
        dictionar = open('dictionar.txt', 'a')
        dictionar.write(cuv)
        dictionar.close()

    def get_all(self):
        '''
        Functia returneaza lista cu toate cuvintele din dictionar
        :return:
        '''
        lista = []
        dictionar = open('dictionar.txt', 'r')
        for line in dictionar:
            comp = line.strip().split()
            lista.append(text(comp[0], comp[1], comp[2], comp[3]))
        dictionar.close()
        return lista

    def cauta(self,par2,par1,dict,limba2):
        '''

        Functia cauta cuvinte in dictionar dupa cuvantul par2
        '''
        for dictie in dict:
            if par1 == dictie.get_sursa() and limba2 == dictie.get_destinatie() and par2 == dictie.get_cuvant():
                return dictie.get_traducere()
            elif par1 == dictie.get_destinatie() and limba2 == dictie.get_sursa() and par2 == dictie.get_traducere():
                return dictie.get_cuvant()
