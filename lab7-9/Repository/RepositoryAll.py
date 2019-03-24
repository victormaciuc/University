from Domain.Book import *
from Domain.Clients import *
from Domain.Rents import *
import os
from shutil import copyfile

class RepoError(Exception):
    pass

class RepositoryB(object):

    def __init__(self):
        self._listBooks = []


    def eroriRecurs (self,i,book):
        if (i>= len(self._listBooks)):
            return
        if(self._listBooks[i] == book):
            raise RepoError("Carte deja existenta")
        self.eroriRecurs(i+1,book)

    def addBook(self,book):
        '''
        Functia are rolul de adauga obiectul carte in lista de carti
        Input: book
                book - Book
        '''
        self.eroriRecurs(0,book)
        self._listBooks.append(book)

    def searchById(self,idcarte):
        for carte in self._listBooks:
            if carte == idcarte:
                return carte
        raise RepoError("Carte inexistenta")

    def searchByName(self,nume):
        for carte in self._listBooks:
            if carte.getTitlu == nume:
                return carte
        raise RepoError("Carte inexistenta")

    def removeBook(self,value):
        '''
        Functia are rolul de a sterge obiectul value din lista de carti
        Input: value
                value - Book
        '''
        self._listBooks.remove(value)

    def getBooks(self):
        return self._listBooks

    def __len__(self):
        return len(self._listBooks)

class RepositoryC(object):

    def __init__(self):
        self._listClients = []

    def eroriRecurs2 (self,i,client):
        if (i>= len(self._listClients)):
            return
        if(self._listClients[i] == client):
            raise RepoError("Client deja existenta")
        self.eroriRecurs2(i+1,client)

    def addClient(self,client):
        '''
        Functia are rolul de a adauga obiectul client in lista de clienti
        Input: client
                client - Client
        '''
        self.eroriRecurs2(0,client)
        self._listClients.append(client)

    def searchById(self,idclient):
        for client in self._listClients:
            if client == idclient:
                return client
        raise RepoError("Client inexistent")

    def removeClient(self,value):
        '''
        Functia are rolul de a sterge obiectul value din lista de clienti
        Input: value
                value - Client
        '''
        self._listClients.remove(value)

    def getClients(self):
        return self._listClients

    def __len__(self):
        return len(self._listClients)

class RepositoryR(object):

    def __init__(self):
        self._listRents = []

    def addRent (self, value):
        '''
        Functia are rolul de a adauga in lista de inchirieri obiectul value
        Input: value
                value - Rent
        '''
        if value in self._listRents:
            raise RepoError("Inchiriere deja existenta")
        self._listRents.append(value)

    def getRents(self):
        return self._listRents

    def __len__(self):
        return len(self._listRents)

    def removeRent(self,value):
        '''
        Functia are rolul de a sterge din lista de inchirieri obiectul value
        Input: value
                value - Rent
        '''
        self._listRents.remove(value)


class FileRepoBook(RepositoryB):

    def __init__(self):
        super().__init__()

    def addBookFile (self, carte):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile.txt",'a')
        carte = str(carte)
        f.write(carte+"\n")
        f.close()

    def removeByIdf(self,idcarte):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile.txt",'r')
        g = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile2.txt",'a')
        for book in f.readlines():
            words = book.strip().split(" ")
            id = int(words[0])
            if id != idcarte:
                g.write(book+"\n")
        f.close()
        g.close()
        copyfile('BooksFile2.txt', 'BooksFile.txt')
        g = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile2.txt",'r+')
        g.seek(0)
        g.truncate()
        g.close()

    def incarcaBooksFile (self):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile.txt",'r')
        for book in f.readlines():
            words = book.strip().split(" ")
            id = int(words[0])
            titlu = words[1]
            autor = words[2]
            descriere = words[3]
            carte = Book(id,titlu,autor,descriere)
            self._listBooks.append(carte)
        f.close()


class FileRepoClient(RepositoryC):

    def __init__(self):
        super().__init__()

    def addClientFile (self, client):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\ClientsFile.txt", 'a')
        client = str(client)
        f.write(client+"\n")
        f.close()

    def incarcaClientsFile (self):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\ClientsFile.txt", 'r')
        for client in f.readlines():
            words = client.strip().split(" ")
            id = int(words[0])
            nume = words[1]
            cnp = int(words[2])
            clientt = Client(id,nume,cnp)
            self._listClients.append(clientt)
        f.close()

class FileRepoRent(RepositoryR):

    def __init__(self):
        super().__init__()

    def addRentFile (self, rent):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\RentsFile.txt", 'a')
        rent = str(rent)
        f.write(rent+"\n")
        f.close()

    def removeByIdf(self, idrent):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\RentsFile.txt", 'r')
        g = open(r"C:\Users\Victor\Desktop\lab7-9\RentsFile2.txt", 'a')
        for rent in f.readlines():
            words = rent.strip().split(" ")
            id = int(words[3])
            if id != idrent:
                g.write(rent)
        f.close()
        g.close()
        copyfile('RentsFile2.txt', 'RentsFile.txt')
        g = open(r"C:\Users\Victor\Desktop\lab7-9\RentsFile2.txt", 'r+')
        g.seek(0)
        g.truncate()
        g.close()

    def incarcaRentsFile (self):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\RentsFile.txt", 'r')
        for rent in f.readlines():
            words = rent.strip().split(" ")
            idB = int(words[3])
            titlu = words[4]
            autor = words[5]
            descriere = words[6]
            idC = int(words[0])
            nume = words[1]
            cnp = int(words[2])
            book = Book(idB,titlu,autor,descriere)
            client = Client(idC,nume,cnp)
            rentt = Rent(book,client)
            self._listRents.append(rentt)
        f.close()
