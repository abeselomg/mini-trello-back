import graphene
from app import (
    mutations as trello_mutations,
    schema as trello_schema,
)
# from graphene.types.generic import GenericScalar


class Query(
    trello_schema.Query,

):
    pass



class Mutations(
    trello_mutations.Mutation,

):
    pass



schema = graphene.Schema(query=Query, mutation=Mutations)
