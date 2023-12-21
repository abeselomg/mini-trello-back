import graphene
from app import (
    mutations as thread_mutations,
    schema as thread_schema,
)
# from graphene.types.generic import GenericScalar


class Query(
    thread_schema.Query,

):
    pass



class Mutations(
    thread_mutations.Mutation,

):
    pass



schema = graphene.Schema(query=Query, mutation=Mutations)
