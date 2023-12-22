import graphene

class UserObject(graphene.ObjectType):
    user_id = graphene.ID()
    name = graphene.String()


class BoardObject(graphene.ObjectType):
    board_id = graphene.ID()
    name = graphene.String()
    # owner = graphene.Field(UserObject)
    members = graphene.List(UserObject)


class ListObject(graphene.ObjectType):
    list_id = graphene.ID()
    board_id = graphene.ID()
    name = graphene.String()


class TaskObject(graphene.ObjectType):
    task_id = graphene.ID()
    list_id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    due_date = graphene.String()
    assigned_users = graphene.List(UserObject)
