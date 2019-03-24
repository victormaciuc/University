class ValidError(Exception):
    pass

class ValidBook(object):

    def __init__(self):
        pass

    def validareCarte(self, carte):
        '''
        Functia are rolul de a valida obiectul carte si de a ridica o eroare in caz contrar validarii
        Input: carte
                carte - Book
        '''
        errors = ""
        if carte.getId()<0:
            errors += 'Invalid id\n'
        if carte.getTitlu()[0].islower():
            errors += 'Titlu invalid\n'
        if carte.getAutor()[0].islower():
            errors += 'Autor Invalid\n'
        if len(errors)>0:
            raise ValidError(errors)

class ValidClient(object):

    def __init__(self):
        pass

    def validareClient(self, client):
        '''
        Functia are rolul de a valida obiectul client si de a ridica o eroare in caz contrar validarii
        Input: client
                client - Client
        '''
        errors = ""
        if client.getId()<0:
            errors += 'Invalid id\n'
        if client.getNume()[0].islower():
            errors += 'Nume invalid\n'
        if len(str(client.getCnp()))!=13:
            errors += 'Lungime cnp necorespunzatoare\n'
        if len(errors)>0:
            raise ValidError(errors)

class ValidRent(object):

    def __init__(self):
        pass

    def validareRent(self, rent):
        errors = ""
        if len(errors)>0:
            raise ValidError(errors)