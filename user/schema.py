import graphene
from graphene_django import DjangoObjectType
from user.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("is_superuser", "is_staff", "is_active")

class Query(graphene.ObjectType):
    user = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()
