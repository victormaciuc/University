from Ui.Consol import *
from teste import *
from Validator import *
from Repository.Repo import *
from Controller.ServController import *

t = Test()
t.run_tests()
validation = Validator()
repo = Repository()
serv = Controller(repo, validation)
c = Console(serv)
c.run()
