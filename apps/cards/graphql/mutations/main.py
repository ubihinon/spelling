from apps.cards.graphql.mutations.answer import AnswerMutation
from apps.cards.graphql.mutations.learning_session import LearningSessionMutation


class LearningSessionMutations:
    session = LearningSessionMutation.Field()
    answer = AnswerMutation.Field()
