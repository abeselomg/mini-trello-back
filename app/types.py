import graphene

class UserObject(graphene.ObjectType):
    user_id = graphene.UUID()
    name = graphene.String()

class BoardObject(graphene.ObjectType):
    board_id = graphene.UUID()
    name = graphene.String()
    owner = graphene.UUID()
    members = graphene.List(graphene.UUID)

class ListObject(graphene.ObjectType):
    list_id = graphene.UUID()
    board_id = graphene.UUID()
    name = graphene.String()

class TaskObject(graphene.ObjectType):
    task_id = graphene.UUID()
    list_id = graphene.UUID()
    title = graphene.String()
    description = graphene.String()
    due_date = graphene.DateTime()
    completed = graphene.Boolean()
    assigned_users = graphene.List(graphene.UUID)
