from Error import *


class Console:
    def __init__(self, serv):
        self.serv = serv

    def __cerinta1(self,params):
        if len(params) != 4:
            print('numar invalid de parametri!')
            return
        self.serv.adauga_cuvant(params[0],params[1],params[2],params[3])

    def __cerinta2(self,params):
        if len(params) != 1:
            print('numar invalid de parametrii!')
            return
        ui_print(self.serv.traduceri_list(params[0]))

    def __cerinta3(self,params):
        if len(params) != 4:
            print('numar invalid de parametrii!')
            return
        self.serv.tradu_text(params[0],params[1],params[2],params[3])

    def __cerinta4(self,params):
        if len(params) != 3:
            print('numar gresit de parametrii')
            return
        ui_print(self.serv.tranzitiv(params[0],params[1],params[2]))

    def run(self):
        comands = {"cerinta1": self.__cerinta1,
                   "cerinta2": self.__cerinta2,
                   "cerinta3": self.__cerinta3,
                   "cerinta4": self.__cerinta4
                }
        while True:
            print("Comanda: ")
            cmd = input('>>')
            if cmd == 'exit':
                return
            params = cmd.strip().split(" ")
            if params[0] in comands:
                try:
                    comands[params[0]](params[1:])
                except ValueError as ve:
                    print('ValueError!')
                    print(ve)
                except ValidError as vee:
                    print('ValidationError!')
                    print(vee)
                except RepoError as re:
                    print('RepoError!')
                    print(re)
            else:
                print('comanda invalida!')


def ui_print(li):
    for i in li:
        print(i)
