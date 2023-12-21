import graphene
from .types import UserObject, BoardObject, ListObject, TaskObject
from .models import User,Board,List,Task

class Query(graphene.ObjectType):
    users = graphene.List(UserObject)
    boards = graphene.List(BoardObject)
    lists = graphene.List(ListObject)
    tasks = graphene.List(TaskObject)

    def resolve_users(self, info):
        return User.scan()

    def resolve_boards(self, info):
        return Board.scan()

    def resolve_lists(self, info):
        return List.scan()

    def resolve_tasks(self, info):
        return Task.scan()


