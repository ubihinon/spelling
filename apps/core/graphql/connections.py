from graphene import Int
from graphene import relay


class BaseConnection(relay.Connection):
    count = Int()

    def resolve_count(self, info):
        return self.iterable.count()

    class Meta:
        abstract = True
