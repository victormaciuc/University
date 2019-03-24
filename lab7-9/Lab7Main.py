from Controller.Controller import *
from Repository.RepositoryAll import *
from Validators.Validation import *
from Ui.Ui import *
from Tests.Teste import *

def main():


    #repoBook = RepositoryB()
    repoBook = FileRepoBook()
    validBook = ValidBook()
    servBook = ServBook(validBook, repoBook)

    #repoClient = RepositoryC()
    repoClient = FileRepoClient()
    validClient = ValidClient()
    servClient = ServClient(validClient, repoClient)

    #repoRent = RepositoryR()
    repoRent = FileRepoRent()
    validRent = ValidRent()
    servRent = ServRent(validRent, repoRent, repoBook, repoClient)

    ui= Ui(servBook, servClient, servRent)
    ui.run()




main()