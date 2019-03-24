from Validators.Validation import ValidError
from Repository.RepositoryAll import RepoError
import random

class Ui(object):

    def __init__(self, servBook, servClient, servRent):
        self.__servBook = servBook
        self.__servClient = servClient
        self.__servRent = servRent
        self.__commands = {
            "addBook": self.__ui_add_book,
            "printBooks": self.__ui_print_books,
            "addClient": self.__ui_add_client,
            "printClients": self.__ui_print_client,
            "addRent": self.__ui_add_rent,
            "printRents": self.__ui_print_rent,
            "removeBook": self.__ui_remove_book,
            "removeClient": self.__ui_remove_client,
            "cautaBook": self.__ui_cauta_book,
            "cautaClient": self.__ui_cauta_client,
            "eliminBookClient": self.__ui_elim_book_client,
            "mostHired": self.__ui_most_hired_book,
            "genBook": self.__ui_gen_book,
            "genClient": self.__ui_gen_client,
            "rap20": self.__ui_rap20,
            "rapNume": self.__ui_ord_nume,
            "rapNr": self.__ui_ord_nrBooks,
            "rapbonus": self.__ui_rap_bonus,
            "incarca": self.__ui_incarca_fisier,
            "printBooksf": self.__ui_print_booksf,
            "printClientsf": self.__ui_print_clientsf,
            "removeBookf": self.__ui_remove_bookf,
            "sortShell": self.__ui_sort_shell,
            "sortBuble": self.__ui_sort_buble,
            "sortInsert": self.__ui_sort_insertion
        }

    def __ui_sort_insertion(self,params):
        if len(params)!=0:
            print("Numar gresit de parametrii")
            return
        self.__servClient.sort_insertion()

    def __ui_sort_buble(self,params):
        if len(params)!=0:
            print("Numar gresit de parametrii")
            return
        self.__servClient.sort_buble()

    def __ui_sort_shell(self,params):
        if len(params)!=0:
            print("Numar gresit de parametrii")
            return
        self.__servClient.sort_shell()

    def __ui_remove_bookf(self,params):
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id = int(params[0])
        self.__servRent.remove_bookf(id)


    def __ui_print_clientsf(self,params):
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        self.__servClient.printare_clienti()

    def __ui_print_booksf(self,params):
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        self.__servBook.printare_carti()

    def __ui_incarca_fisier(self,params):
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        self.__servBook.incarca_fisier()
        self.__servClient.incarca_fisier()
        self.__servRent.incarca_fisier()

    def __ui_rap_bonus(self,params):
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        rents = self.__servRent.rap_bonus()
        for rent in rents:
            print(rent,sep='\n')

    def __ui_ord_nume (self,params):
        '''
        Functia are rolul de a apela functia de sortare dupa nume a inchirierilor si de a afisa rezultatul
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        print("Clientii sortati in ordinea numelui acestora sunt:")
        rents = self.__servRent.sort_nume()
        for rent in rents:
            print(rent,sep='\n')

    def __ui_ord_nrBooks (self,params):
        '''
        Functia are rolul de a apela functia de sortare dupa nume a inchirierilor si de a afisa rezultatul
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        print("Clientii sortati in ordinea numarului de carti inchiriate sunt:")
        rents = self.__servRent.sort_nrBooks()
        print (*rents,sep='\n')

    def __ui_rap20 (self,params):
        '''
        Functia are rolul de a apela functia de cautare a top 20% cei mai activi clienti si de a afisa rezultatul
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        print("Primii 20% cei mai activi clienti sunt: ")
        carti = self.__servRent.rap20rent()
        print (carti)

    def __ui_gen_client (self,params):
        '''
        Functia are rolul de a apela functia de generare a unui client random si de a-l adauga in lista de clienti
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id = int(params[0])
        cnp = random.randint(1000000000000,9999999999999)
        self.__servClient.generare_client(id, cnp)

    def __ui_gen_book (self,params):
        '''
        Functia are rolul de a apela functia de generare a unei carti random si de a o adauga in lista de carti
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id = int(params[0])
        self.__servBook.generare_book(id)

    def __ui_most_hired_book (self,params):
        '''
        Functia are rolul de a afisa cea mai inchiriata carte
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print("Numar gresit de parametrii")
            return
        carte = self.__servRent.mostHiredBook()
        print ("Cea mai inchiriata carte este: ",carte)

    def __ui_elim_book_client(self,params):
        '''
        Functia are rolul de a apela functia de stergere a unei inchirieri de la un client
        Input: params
        Cerinte: len(params)==2
        '''
        if len(params)!=2:
            print("Numar gresit de parametrii")
            return
        idBook = int (params[0])
        idClient = int (params[1])
        self.__servRent.elim_book_client(idBook, idClient)

    def __ui_cauta_book (self,params):
        '''
        Functia are rolul de a apela functia de cautare a unei carti dupa id
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id = int (params[0])
        carte = self.__servBook.cautaBook(id)
        print(carte)

    def __ui_cauta_client (self,params):
        '''
        Functia are rolul de a apela functia de cautare a unui client dupa id
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id = int (params[0])
        client = self.__servClient.cautaClient(id)
        print(client)

    def __ui_remove_client (self,params):
        '''
        Functia are rolul de a apela functia de stergere a unui client
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id= int (params[0])
        self.__servRent.remove_client(id)

    def __ui_remove_book (self,params):
        '''
        Functia are rolul de a apela functia de stergere a unei carti
        Input: params
        Cerinte: len(params)==1
        '''
        if len(params)!=1:
            print("Numar gresit de parametrii")
            return
        id= int (params[0])
        self.__servRent.remove_book(id)

    def __ui_add_book (self,params):
        '''
        Functia are rolul de a apela functia de adaugare a unei carti
        Input: params
        Cerinte: len(params)==4
        '''
        if len(params)!=4:
            print("Numar gresit de parametrii")
            return
        id = int (params[0])
        titlu = params[1]
        autor = params[2]
        descriere = params[3]
        self.__servBook.add_book(id, titlu, autor, descriere)

    def __ui_print_books (self,params):
        '''
        Functia are rolul de a afisa lista de carti
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print ("Numar gresit de parametrii")
            return
        carti = self.__servBook.get_books()
        for carte in carti:
            print(carte)

    def __ui_add_client (self,params):
        '''
        Functia are rolul de a apela functia de adaugare a unui client
        Input: params
        Cerinte: len(params)==3
        '''
        if len(params)!=3:
            print ("Numar gresit de parametrii")
            return
        id = int (params[0])
        nume = params[1]
        cnp = int (params[2])
        self.__servClient.add_client(id, nume, cnp)

    def __ui_print_client (self,params):
        '''
        Functia are rolul de a afisa lista de clienti
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print ("Numar gresit de parametrii")
            return
        clienti = self.__servClient.get_clients()
        for client in clienti:
            print(client)

    def __ui_add_rent (self,params):
        '''
        Functia are rolul de a apela functia de adaugare a unei inchirieri
        Input: params
        Cerinte: len(params)==2
        '''
        if len(params)!=2:
            print ("Numar gresit de parametrii")
            return
        idBook = int(params[0])
        idClient = int(params[1])
        self.__servRent.add_rent(idBook, idClient)

    def __ui_print_rent (self,params):
        '''
        Functia are rolul de a afisa lista de inchirieri
        Input: params
        Cerinte: len(params)==0
        '''
        if len(params)>0:
            print ("Numar gresit de parametrii")
            return
        rents = self.__servRent.get_rents()
        for rent in rents:
            print(rent)

    def run(self):
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            if cmd == "exit":
                return
            elif params[0] in self.__commands:
                try:
                    self.__commands[params[0]](params[1:])
                except ValueError:
                    print("invalid numerical value!")
                except ValidError as ve:
                    print("Validation error!")
                    print(ve)
                except RepoError as re:
                    print("Repository error!")
                    print(re)
            else:
                print("invalid command!")


