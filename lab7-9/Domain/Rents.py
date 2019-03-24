class Rent(object):

    def __init__(self, book, client):
        self.__book = book
        self.__client = client


    def __str__(self):
        return str(self.__client)+" "+str(self.__book)

    def __eq__(self, value):
        return self.__book == value.__book and self.__client == value.__client

    def get_Book(self):
        return self.__book

    def get_Client(self):
        return self.__client

    book = property(get_Book, None, None, None)
    client = property(get_Client, None, None, None)
