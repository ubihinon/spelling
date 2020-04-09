from graphene import Connection
from graphene import Int
# from graphene import relay


class BaseConnection(Connection):
    count = Int()

    def resolve_count(self, info):
        return self.iterable.count()

    class Meta:
        abstract = True
