import graphql_jwt

from apps.accounts.graphql.mutations.activate_user import ActivateUserMutation
from apps.accounts.graphql.mutations.change_user_password import ChangeUserPasswordMutation
from apps.accounts.graphql.mutations.delete_user import DeleteUserMutation
from apps.accounts.graphql.mutations.reset_user_password import ResetUserPasswordMutation
from apps.accounts.graphql.mutations.update_user import UpdateUserMutation
from apps.accounts.graphql.mutations.user import UserMutation


class AccountMutations:
    create_user = UserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
    change_password = ChangeUserPasswordMutation.Field()
    reset_password = ResetUserPasswordMutation.Field()
    activate_user = ActivateUserMutation.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
