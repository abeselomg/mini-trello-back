import graphene
from .types import UserObject, BoardObject, ListObject, TaskObject
from .models import User,Board,List,Task

class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserObject)

    class Arguments:
        name = graphene.String(required=True)


    def mutate(self, info, name):
        user = User(name=name)
        user.save()
        return CreateUserMutation(user=user)


class CreateBoardMutation(graphene.Mutation):
    board = graphene.Field(BoardObject)
    class Arguments:
        name = graphene.String(required=True)
        owner = graphene.UUID(required=True)
        members = graphene.List(graphene.UUID)

    def mutate(self, info, name, owner, members=None):
        board = Board(name=name, owner=owner, members=members)
        board.save()
        return CreateBoardMutation(board=board)


class CreateListMutation(graphene.Mutation):
    class Arguments:
        board_id = graphene.UUID(required=True)
        name = graphene.String(required=True)

    list = graphene.Field(ListObject)

    def mutate(self, info, board_id, name):
        list = List(board_id=board_id, name=name)
        list.save()
        return CreateListMutation(list=list)


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        list_id = graphene.UUID(required=True)
        title = graphene.String(required=True)
        description = graphene.String()
        due_date = graphene.DateTime()
        assigned_users = graphene.List(graphene.UUID)

    task = graphene.Field(TaskObject)

    def mutate(self, info, list_id, title, description=None, due_date=None, assigned_users=None):
        task = Task(list_id=list_id, title=title, description=description, due_date=due_date, assigned_users=assigned_users)
        task.save()
        return CreateTaskMutation(task=task)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    create_board = CreateBoardMutation.Field()
    create_list = CreateListMutation.Field()
    create_task = CreateTaskMutation.Field()

