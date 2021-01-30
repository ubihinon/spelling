from typing import Any

from graphql import ResolveInfo


class AllowAuthenticated:
    def has_node_permission(self, info: ResolveInfo, obj_id: str) -> bool:
        return info.context.user.is_authenticated

    def has_mutation_permission(self, root: Any, info: ResolveInfo, **kwargs) -> bool:
        return info.context.user.is_authenticated

    def has_filter_permission(self, info: ResolveInfo) -> bool:
        return info.context.user.is_authenticated
