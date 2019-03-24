class Book:

    def __init__(self, id, titlu, autor, descriere):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor


    def getId (self):
        return self.__id

    def getTitlu(self):
        return self.__titlu

    def setTitlu(self, value):
        self.__titlu = value

    def getDescriere(self):
        return self.__descriere

    def setDescriere(self, value):
        self.__descriere = value

    def getAutor(self):
        return self.__autor

    def setAutor(self, value):
        self.__autor = value

    def __str__(self):
        return str(self.__id)+" "+str(self.__titlu)+" "+str(self.__autor)+" "+str(self.__descriere)

    def __eq__(self, value):
        if type(value)==str:
            return self.__titlu == value
        if type(value)==int:
            return self.__id == value
        return self.__id == value.id

    id = property(getId, None, None, None)
    titlu = property(getTitlu, setTitlu, None, None)
    autor = property(getAutor, setAutor, None, None)
    descriere = property(getDescriere, setDescriere, None, None)
