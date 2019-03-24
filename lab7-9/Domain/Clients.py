class Client(object):

    def __init__(self, id, nume, cnp):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp


    def getId (self):
        return self.__id

    def getNume (self):
        return self.__nume

    def getCnp (self):
        return self.__cnp

    def setNume (self, value):
        self.__nume = value

    def setCnp (self, value):
        self.__cnp = value

    def __str__(self):
        return str(self.__id) + " " + str(self.__nume) + " " + str(self.__cnp)

    def __eq__(self, value):
        if type(value)==int:
            return self.__id == value
        return self.__id == value.__id

    id = property(getId, None, None, None)
    nume = property(getNume, setNume, None, None)
    cnp = property(getCnp, setCnp, None, None)
