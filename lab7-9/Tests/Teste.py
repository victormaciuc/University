from Domain.Clients import *
from Domain.Book import *
from Domain.Rents import *
from Validators.Validation import *
from Ui.Ui import *
from Repository.RepositoryAll import *
from Controller.Controller import *


class Test(object):

    def __init__(self):
        self.__id = 4
        self.__titlu = "Ion"
        self.__descriere = "carte minunata"
        self.__autor = "Liviu Rebreanu"
        self.__carte = Book(self.__id ,self.__titlu ,self.__autor ,self.__descriere)

        self.__id2 = 2
        self.__nume = "Maria"
        self.__cnp = 1234567890987
        self.__client = Client(self.__id2 ,self.__nume ,self.__cnp )

        self.__repoBook = RepositoryB()
        self.__validBook = ValidBook()
        self.__repoClient = RepositoryC()
        self.__validClient = ValidClient()

        self.__servClient = ServClient(self.__validClient, self.__repoClient)
        self.__servBook = ServBook(self.__validBook, self.__repoBook)

        self.__repoRent = RepositoryR()
        self.__validRent = ValidRent()

        self.__servRent = ServRent(self.__validRent, self.__repoRent, self.__repoBook, self.__repoClient)
        self.__rent = Rent(self.__id,self.__id2)

    def __testMetoda(self):
        assert self.__carte.getTitlu() == self.__titlu
        assert self.__client.getId() == self.__id2

        assert self.__carte.getDescriere() == self.__descriere
        assert self.__client.getNume() == self.__nume

        assert self.__rent.get_Book() == self.__id
        assert self.__rent.get_Client() ==   self.__id2

    def __testadaug(self):
        self.__servBook.add_book(6, "Ion", "Liviu", "desc1")
        assert self.__repoBook.searchById(6) == Book (6,"Ion","Liviu","desc1")

        self.__servClient.add_client(3, "Mihai", 1234567890986)
        assert self.__repoClient.searchById(3) == Client(3,"Mihai",1234567890986)

        self.__servBook.add_book(7, "Pacala", "Eminescu", "desc2")
        self.__servRent.add_rent(7, 2)
        assert self.__repoRent.getRents() == [Rent(7,2)]

    def __testRepo(self):
        assert len(self.__repoBook) == 0
        self.__repoBook.addBook(self.__carte)
        assert len(self.__repoBook) == 1

        assert len(self.__repoClient) == 0
        self.__repoClient.addClient(self.__client)
        assert len(self.__repoClient) == 1

        aux = Client(2,"Maria",1234567890987)
        assert aux == self.__repoClient.searchById(2)


    def __testController(self):
        carte = self.__servRent.mostHiredBook()
        assert carte == Book(7,"Pacala","Eminescu","desc2")

        listaaux = self.__servRent.sort_nume()
        listaRents = self.__repoRent.getRents()

        listaRents.sort(key=lambda x: x.get_Client().getNume(), reverse=False)
        assert listaaux == listaRents


    def rulareTeste(self):
        self.__testMetoda()
        self.__testRepo()
        self.__testadaug()
        self.__testController()
