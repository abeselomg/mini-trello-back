import graphene
import uuid
from .types import UserObject, BoardObject, ListObject, TaskObject
from .models import User, Board, List, Task, BoardMember
from datetime import datetime, timezone


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserObject)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        user = User(user_id=str(uuid.uuid4()), name=name)
        user.save()
        return CreateUserMutation(user=user)


class CreateBoardMutation(graphene.Mutation):
    board = graphene.Field(BoardObject)

    class Arguments:
        name = graphene.String(required=True)
        members = graphene.List(graphene.ID)

    def mutate(self, info, name, members=None):
        users = [User.get(user_id) for user_id in members]
        all_members = [
            BoardMember(user_id=user.user_id, name=user.name) for user in users
        ]
        board = Board(board_id=str(uuid.uuid4()), name=name, members=all_members)
        board.save()
        return CreateBoardMutation(board=board)


class CreateListMutation(graphene.Mutation):
    class Arguments:
        board_id = graphene.ID(required=True)
        name = graphene.String(required=True)

    list = graphene.Field(ListObject)

    def mutate(self, info, board_id, name):
        list = List(list_id=str(uuid.uuid4()), board_id=board_id, name=name)
        list.save()
        return CreateListMutation(list=list)


class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        list_id = graphene.ID(required=True)
        title = graphene.String(required=True)
        description = graphene.String()
        due_date = graphene.String()
        assigned_users = graphene.List(graphene.ID)

    task = graphene.Field(TaskObject)

    def mutate(
        self, info, list_id, title, description=None, due_date=None, assigned_users=None
    ):
        users = [User.get(user_id) for user_id in assigned_users]
        all_members = [
            BoardMember(user_id=user.user_id, name=user.name) for user in users
        ]
        date_value = datetime.strptime(due_date, "%Y-%m-%d")

        date_object = datetime.combine(
            date_value, datetime.now().time(), datetime.now().tzinfo
        )

        task = Task(
            task_id=str(uuid.uuid4()),
            list_id=list_id,
            title=title,
            description=description,
            due_date=date_object,
            assigned_users=all_members,
        )
        task.save()
        return CreateTaskMutation(task=task)


class MoveToListMutation(graphene.Mutation):
    task = graphene.Field(TaskObject)

    class Arguments:
        task_id = graphene.ID(required=True)
        list_id = graphene.ID(required=True)
        new_list_id = graphene.ID(required=True)


    def mutate(self, info, list_id, task_id,new_list_id):
        task = Task.get(hash_key=task_id,range_key=list_id)
        task.list_id = new_list_id
        task.save()
        return MoveToListMutation(task=task)


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    create_board = CreateBoardMutation.Field()
    create_list = CreateListMutation.Field()
    create_task = CreateTaskMutation.Field()
    move_task_to_list = MoveToListMutation.Field()
