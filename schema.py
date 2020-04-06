import graphene

import apps.accounts.schema
import apps.cards.schema


class Query(
    apps.accounts.schema.Query,
    apps.cards.schema.Query,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
