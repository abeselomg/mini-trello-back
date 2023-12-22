import os
from app.models import Board,List,Task,User


def init_db():
    # Board.delete_table()
    
    for model in [Board,List,Task,User]:
        if not model.exists():
            model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    print('created!!')

   
if __name__ == '__main__':
    init_db()

