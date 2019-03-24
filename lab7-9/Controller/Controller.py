from Domain.Book import Book
from Sortari.Bublesort import *
from Sortari.Shellsort import *
from Domain.Clients import Client
from Domain.Rents import Rent
import copy
from collections import Counter
import string
from random import *


class ServBook(object):

    def __init__(self, validBook, repoBook):
        self.__validBook = validBook
        self.__repoBook = repoBook

    def printare_carti(self):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\BooksFile.txt", 'r')
        for book in f.readlines():
            words = book.strip().split(" ")
            id = int(words[0])
            titlu = words[1]
            autor = words[2]
            descriere = words[3]
            carte = Book(id, titlu, autor, descriere)
            print(carte,"\n")
        f.close()

    def incarca_fisier(self):
        self.__repoBook.incarcaBooksFile()

    def add_book(self, id, titlu, autor, descriere):
        '''
        Functia are rolul de a adauga o carte noua , formand obiectul carte
        Input : id,titlu,autor,descriere
                id - int
                titlu - str
                autor - str
                descriere - str
        '''
        carte = Book(id,titlu,autor,descriere)
        self.__validBook.validareCarte(carte)
        self.__repoBook.addBook(carte)
        self.__repoBook.addBookFile(carte)

    def cautaBook (self, id):
        '''
        Functia are rolul de a returna obiectul "carte" in urma cautarii dupa id
        Input: id
                id - int
        '''
        return self.__repoBook.searchById(id)

    def get_books(self):
        '''
        Functia are rolul de a returna lista de carti
        '''
        return self.__repoBook.getBooks()

    def generare_book(self, id):
        '''
        Functia are rolul de a genera o carte random si de a o adauga in lista de carti
        Input: id
                id - int
        Preconditii: Titlul trebuie sa aiba prima litera caps
                     Autorul trebuie sa aiba prima litera caps
        '''
        upperchar = string.ascii_uppercase
        lowerchar = string.ascii_lowercase
        upperName = "".join(choice(upperchar) for x in range(1))
        lowerName = "".join(choice(lowerchar) for y in range(2, 7))
        upperTitle = "".join(choice(upperchar) for x in range(1))
        lowerTitle = "".join(choice(lowerchar) for y in range(2, 7))
        desc = "".join(choice(lowerchar) for y in range(2, 20))
        autor = upperName + lowerName
        title = upperTitle + lowerTitle
        carte = Book(id, title, autor, desc)
        self.__repoBook.addBook(carte)

class ServClient(object):

    def __init__(self, validClient, repoClient):
        self.__validClient = validClient
        self.__repoClient = repoClient

    def sort_insertion(self):
        listClients = self.__repoClient.getClients()
        listaux = []
        listrez = []
        for client in listClients:
            aux = client.getId()
            listaux.append(aux)
        listaux2 = self.insertionSort(listaux)
        for i in listaux2:
            elem = [i, self.__repoClient.searchById(i).getNume()]
            listrez.append(elem)
        print(listrez)

    def insertionSort(self, aux):
        '''
        Complexitate de timp : O(n^2)
        Complexitate de spatiu: O(1)
        Caz favorabil: O(n)
        Caz cel mai putin favorabil: lista este sortata descrescator O(n^2)
        Caz mediu: O(n^2)
        '''
        n = len(aux)
        for i in range(1, n):
            key = aux[i]
            j = i-1
            while j >=0 and key < aux[j] :
                aux[j+1] = aux[j]
                j -= 1
            aux[j+1] = key
        return aux

    def sort_buble(self):
        listClients = self.__repoClient.getClients()
        listClients = bubleSortare(listClients,key = lambda client : (client.getId()),reverse = False)
        for client in listClients:
            print(client)

    def sort_shell(self):
        listClients = self.__repoClient.getClients()
        listClients = shellSortare(listClients, key=lambda client: (client.getNume()), reverse=True)
        for client in listClients:
            print(client)


    def printare_clienti(self):
        f = open(r"C:\Users\Victor\Desktop\lab7-9\ClientsFile.txt", 'r')
        for client in f.readlines():
            words = client.strip().split(" ")
            id = int(words[0])
            nume = words[1]
            cnp = int(words[2])
            clientt = Client(id, nume, cnp)
            print(clientt,"\n")
        f.close()

    def add_client(self, id, nume, cnp):
        '''
        Functia are rolul de a adauga un client la lista de clienti
        Input: id,nume,cnp
                id - int
                nume - str
                cnp - int
        '''
        client = Client(id,nume,cnp)
        self.__validClient.validareClient(client)
        self.__repoClient.addClient(client)
        self.__repoClient.addClientFile(client)

    def incarca_fisier(self):
        self.__repoClient.incarcaClientsFile()

    def cautaClient (self, id):
        '''
        Functia are rolul de a returna obiectul "client" in urma cautarii dupa id
        Input: id
                id - int
        '''
        return self.__repoClient.searchById(id)

    def get_clients(self):
        '''
        Functia are rolul de a returna lista de clienti
        '''
        return self.__repoClient.getClients()

    def generare_client(self, id, cnp):
        '''
        Functia are rolul de a genera un obiect client random , respectand validarile clientului
        Input: id,cnp
                id - int
                cnp - int
        Preconditii : Prima litera a numelui sa fie caps
                      Cnp-ul trebuie sa aiba 13 cifre
        '''
        upperchar = string.ascii_uppercase
        lowerchar = string.ascii_lowercase
        upperName = "".join(choice(upperchar) for x in range(1))
        lowerName = "".join(choice(lowerchar) for y in range(2, 7))
        nume = upperName + lowerName
        client = Client(id, nume, cnp)
        self.__repoClient.addClient(client)

class ServRent(object):

    def __init__(self, validRent, repoRent, repoBook, repoClient):
        self.__validRent = validRent
        self.__repoRent = repoRent
        self.__repoBook = repoBook
        self.__repoClient = repoClient

    def incarca_fisier(self):
        self.__repoRent.incarcaRentsFile()

    def add_rent(self,idBook,idClient):
        '''
        Functia are rolul de a adauga o inchiriere noua in lista de inchirieri
        Input: idBook,idClient
                idBook - int
                idClient - int
        '''
        carte = self.__repoBook.searchById(idBook)
        client = self.__repoClient.searchById(idClient)
        rent = Rent(carte, client)
        self.__validRent.validareRent(rent)
        self.__repoRent.addRent(rent)
        self.__repoRent.addRentFile(rent)

    def get_rents(self):
        '''
        Functia are rolul de a returna lista de inchirieri
        '''
        return self.__repoRent.getRents()

    def remove_bookf(self, idbook):
        self.__repoRent.removeByIdf(idbook)
        self.__repoBook.removeByIdf(idbook)

    def remove_book(self, idbook):
        '''
        Functia are rolul de a sterge o carte din lista de carti
        Intial se vor sterge toate inchirierile asociate acelei carti
        Apoi se va sterge cartea din lista de carti
        Input : idbook
                idbook - int

        '''
        listRents = copy.deepcopy(self.__repoRent.getRents())
        for rent in listRents:
            if self.__repoBook.searchById(idbook) == rent.get_Book():
                self.__repoRent.removeRent(rent)
        carte = self.__repoBook.searchById(idbook)
        self.__repoBook.removeBook(carte)

    def remove_client(self, idclient):
        '''
        Functia are rolul de a sterge un client din lista de clienti
        Initial se vor sterge toate inchirierile asociate acelui client
        Apoi se va sterge clientul din lista de clienti
        Input: idclient
                idclient - int
        '''
        listRents = copy.deepcopy(self.__repoRent.getRents())
        for rent in listRents:
            if self.__repoClient.searchById(idclient) == rent.get_Client():
                self.__repoRent.removeRent(rent)
        client = self.__repoClient.searchById(idclient)
        self.__repoClient.removeClient(client)

    def elim_book_client(self, idBook, idClient):
        '''
        Functia are rolul de a sterge din lista de inchirieri cheltuiala corespunzatoare id-ului cartii si id-ului clientului introdus
        Input: idBook, idClient
                idBook - int
                idClient - int
        Preconditii : carte - Book
                      client - Client
        '''
        carte = self.__repoBook.searchById(idBook)
        client = self.__repoClient.searchById(idClient)
        listRents = copy.deepcopy(self.__repoRent.getRents())
        for rent in listRents:
            if carte == rent.get_Book() and client == rent.get_Client():
                self.__repoRent.removeRent(rent)

    def mostHiredBook (self):
        '''
        Functia are rolul de a cauta in lista de inchirieri cartea cu numarul de aparitii a id-ului cel mai mare
        Output: carte
                carte - Book
        Postconditii: carte = (id,titlu,autor,descriere)
        '''
        listRents = self.__repoRent.getRents()
        listHiredBooks = []
        if not listRents:
            return
        for rent in listRents:
            aux = rent.get_Book().getId()
            listHiredBooks.append(aux)
        cnt = Counter(listHiredBooks).most_common(1)
        carte = self.__repoBook.searchById(cnt[0][0])
        return carte

    def rap20rent (self):
        '''
        Functia are rolul de a cauta primii 20% cei mai activi clienti
        Output: listarez
                listarez - lista
        Postconditii : listarez - lista cu clientii cei mai activi
        '''
        listId = []
        listrez= []
        listClients = self.__repoClient.getClients()
        listRents = self.__repoRent.getRents()

        aux = 0.2
        nrClients = len(listClients)
        rez = aux*nrClients
        rez = int(rez)
        if rez == 0:
            rez = 1

        for rent in listRents:
            id = rent.get_Client().getId()
            listId.append(id)
        cnt = Counter(listId).most_common(rez)
        for i in cnt:
            elem = [self.__repoClient.searchById(i[0]).getNume(),i[1]]
            listrez.append(elem)
        return listrez

    def sort_nume (self):
        '''
        Functia are rolul de a sorta dupa numele clientilor lista de inchirieri
        Output: listaRents
                listaRents - lista
        PostConditii: listaRents = lista de inchirieri sortata
        '''
        listaRents = self.__repoRent.getRents()
        listaRents = bubleSortare(listaRents,key = lambda client : (client.getNume()),reverse = False )
        #listaRents.sort(key= lambda x: x.get_Client().getNume(),reverse = False)
        return listaRents

    def sort_nrBooks (self):
        '''
        Functia are rolul de a forma o lista listSort in care sa fie fiecare client cu id-ul sau si numarul de carti inchiriate ale acestuia , lista fiind sortata dupa numarul de carti
        Output: listSort
                listSort - lista
        Postconditii : listSort = [[id0,nume0,nrInchirieri0] , [id1,nume1,nrInchirieri1],....[idn,numen,nrInchirierin]]
        '''
        listId = []
        listSort = []
        listRents = self.__repoRent.getRents()
        listClienti = self.__repoClient.getClients()

        for rent in listRents:
            id = rent.get_Client().getId()
            listId.append(id)
        cnt = Counter(listId).most_common(len(listClienti))

        for client in cnt:
            id = self.__repoClient.searchById(client[0]).getId()
            nume = self.__repoClient.searchById(client[0]).getNume()
            listSort.append([id,nume," a inchiriat ",client[1]," carti "])
        listSort.sort(key=lambda x: x[3], reverse=True)
        return listSort

    def rap_bonus (self):
        listId = []
        listRez = []
        listRents = self.__repoRent.getRents()
        listClienti = self.__repoClient.getClients()

        for rent in listRents:
            id = rent.get_Book().getId()
            listId.append(id)
        cnt = Counter(listId).most_common(len(listClienti))

        for i in cnt:
            numeAutor = self.__repoBook.searchById(i[0]).getAutor()
            listRez.append([numeAutor,i[1]])
        listRez.sort(key=lambda x: x[0], reverse=False)
        return listRez