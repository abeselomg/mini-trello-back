import uuid
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, ListAttribute, BooleanAttribute,MapAttribute
from datetime import datetime
HOST = 'http://localhost:8000'

class User(Model):
    class Meta:
        table_name = 'users'
        host=HOST

    user_id = UnicodeAttribute(hash_key=True, default_for_new=str(uuid.uuid4()), attr_name='userId')
    name = UnicodeAttribute()

class BoardMember(MapAttribute):
    user_id = UnicodeAttribute()
    name = UnicodeAttribute()

class Board(Model):
    class Meta:
        table_name = 'boards'
        host=HOST

    board_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='boardId')
    name = UnicodeAttribute()
    members = ListAttribute(of=BoardMember,default=[],null=True)


class List(Model):
    class Meta:
        table_name = 'lists'
        host=HOST

    list_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='listId')
    board_id = UnicodeAttribute(range_key=True, attr_name='boardId')
    name = UnicodeAttribute()


class Task(Model):
    class Meta:
        table_name = 'tasks'
        host=HOST

    task_id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()), attr_name='taskId')
    list_id = UnicodeAttribute(range_key=True, attr_name='listId')
    title = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    due_date = UTCDateTimeAttribute(null=True)
    assigned_users = ListAttribute(of=BoardMember,default=[],null=True)
    created_at=UTCDateTimeAttribute(null=True,default_for_new=datetime.now())



    