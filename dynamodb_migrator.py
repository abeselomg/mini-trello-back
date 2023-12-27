import os
from app.models import Board, List, Task, User
import uuid


def init_db():
    # Board.delete_table()
    # List.delete_table()
    # Task.delete_table()
    # User.delete_table()

    for model in [Board, List, Task, User]:
        if not model.exists():
            model.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

            if model == Board:
                board = Board(board_id=str(uuid.uuid4()), name="name")
                board.save()

            if model == User:
                for user in [
                    {"name": "Jane Doe", "name": "Kirubel Simachew", "name": "Jhon Doe"}
                ]:
                    user = User(user_id=str(uuid.uuid4()), name=user["name"])
                    user.save()


if __name__ == "__main__":
    init_db()
