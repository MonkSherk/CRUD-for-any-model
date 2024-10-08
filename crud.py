from models import ToDo
from models import User
from views import CRUDBase


class CRUDUser(CRUDBase):
    def __init__(self):
        super().__init__(User)



class CRUDToDo(CRUDBase):
    def __init__(self):
        super().__init__(ToDo)
