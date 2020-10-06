import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude = ("is_superuser", "is_staff", "is_active")


class Query(graphene.AbstractType):
    user = graphene.List(UserType)
    verifyuser = graphene.Field(UserType)

    def resolve_user(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_verifyuser(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        nickname = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, username, password, email, nickname, first_name, last_name):
        user = get_user_model()(
            username=username,
            email=email,
            nickname=nickname,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()

        return CreateUser(
            success=True
        )


class UpdateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(default_value=False)
        nickname = graphene.String(default_value=False)
        password = graphene.String(default_value=False)

    success = graphene.Boolean()

    def mutate(self, info, username, email, nickname, password):
        user = User.objects.get(username=username)
        user.email = email if email is not None else email
        user.nickname = nickname if nickname is not None else nickname
        user.password = password if password is not None else password
        user.save()
        return UpdateUser(
            success=True
        )


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        user = User.objects.get(pk=id)
        if user is not None:
            user.delete()

        return DeleteUser(
            success=True
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

