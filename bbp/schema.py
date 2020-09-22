import graphene
from graphene_django import DjangoObjectType
from bbp.models import User, Post, Answer, Tag, Comment, Catagory, Like

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("is_superuser", "is_staff", "is_active")


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        exclude = ("post_answer_count", "post_hits")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer


class CatagoryType(DjangoObjectType):
    class Meta:
        model = Catagory


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    post = graphene.List(PostType)
    user = graphene.List(UserType)
    answer = graphene.List(AnswerType)
    catagory = graphene.List(CatagoryType)
    comment = graphene.List(CommentType)
    tag = graphene.List(TagType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()

    def resolve_post(self, info, **kwargs):
        return Post.objects.all()

    def resolve_answer(self, info, **kwargs):
        return Answer.objects.all()

    def resolve_catagory(self, info, **kwargs):
        return Catagory.objects.all()

    def resolve_comment(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_tag(self, info, **kwargs):
        return Tag.objects.all()


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        nickname = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, **kwargs):
        model = User(
            username=kwargs.get("username"),
            password=kwargs.get("password"),
            nickname=kwargs.get("nickname"),
            email=kwargs.get("email"),
            first_name=kwargs.get("first_name"),
            last_name=kwargs.get("last_name")
        )
        model.save()

        return CreateUser(
            success=True
        )

'''
class InputUpdateUser(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()
    nickname = graphene.String()
    email = graphene.String()


class UpdateUser(graphene.Mutation):
    class Arguments:
        nickname = graphene.String(required=True)
        data = InputUpdateUser(default_value=False)

    success = graphene.Boolean()

    def mutate(root, info, nickname, data):
        model = User.objects(
            nickname=nickname
        ).first()

        if data.username is not None:
            model.username = data.username

        if data.password is not None:
            model.password = data.password

        if data.nickname is not None:
            model.nickname = data.nickname

        if data.email is not None:
            model.email = data.email

        model.save()

        return UpdateUser(
            success=True
        )
'''
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
#   update_user = UpdateUser.Field()


