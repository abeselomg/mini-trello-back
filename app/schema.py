import graphene
from .types import UserObject, BoardObject, ListObject, TaskObject
from .models import User, Board, List, Task
from mini_trello.utils import GrapheneException


class Query(graphene.ObjectType):
    users = graphene.List(UserObject)
    boards = graphene.List(BoardObject)
    lists = graphene.List(ListObject)
    tasks = graphene.List(TaskObject)
    tasks_by_listid = graphene.List(
        TaskObject,
        list_id=graphene.ID(),
    )

    def resolve_users(self, info):
        return User.scan()

    def resolve_boards(self, info):
        return Board.scan()

    def resolve_lists(self, info):
        allList = [alist.attribute_values for alist in List.scan()]
        for l in allList:
            l["tasks"] = Task.scan(Task.list_id == l.get("list_id"))

        return allList

    def resolve_tasks(self, info):
        return Task.scan()

    def resolve_tasks_by_listid(self, info, **kwargs):
        if not kwargs.get("list_id"):
            raise GrapheneException("list_id is required!")
        list_id = kwargs["list_id"]
        range_key_condition = Task.list_id.__eq__(list_id)
        return Task.scan(Task.list_id == list_id)
