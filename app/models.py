import uuid
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, ListAttribute, BooleanAttribute


class User(Model):
    class Meta:
        table_name = 'users'

    user_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='userId')
    name = UnicodeAttribute()


class Board(Model):
    class Meta:
        table_name = 'boards'

    board_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='boardId')
    name = UnicodeAttribute()
    members = ListAttribute()


class List(Model):
    class Meta:
        table_name = 'lists'

    list_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='listId')
    board_id = UnicodeAttribute(range_key=True, attr_name='boardId')
    name = UnicodeAttribute()


class Task(Model):
    class Meta:
        table_name = 'tasks'

    task_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='taskId')
    list_id = UnicodeAttribute(range_key=True, attr_name='listId')
    title = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    due_date = UTCDateTimeAttribute(null=True)
    completed = BooleanAttribute(default=False)
    assigned_users = ListAttribute()



    