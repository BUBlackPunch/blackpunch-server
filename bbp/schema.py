import graphene
from graphene_django import DjangoObjectType
from bbp.models import Post, Answer, Tag, Comment, Catagory, User




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
    answer = graphene.List(AnswerType)
    catagory = graphene.List(CatagoryType)
    comment = graphene.List(CommentType)
    tag = graphene.List(TagType)


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



'''
UserManager' object is not callable
class InputUpdateUser(graphene.InputObjectType):
    username = graphene.String()
    #password = graphene.String()
    #nickname = graphene.String()
    #email = graphene.String()


class UpdateUser(graphene.Mutation):
    class Arguments:
        nickname = graphene.String(required=True)
        data = InputUpdateUser(default_value=False)

    success = graphene.Boolean()

    def mutate(root, info, nickname, data):
        model = get_user_model().objects(
            nickname=nickname
        ).first()

        if data.username is not None:
            model.username = data.username


        model.save()

        return UpdateUser(
            success=True
        )
'''

'''
ca_id 외래키 NOT NULL
class CreatePost(graphene.Mutation):
    class Arguments:
        ca_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    id = graphene.Int()

    def mutate(self, info, title, content, ca_id):
        post = Post(post_title=title, post_content=content),
        catagory = Catagory(id=ca_id),
        post.save(),
        catagory.save()

        return CreatePost(
            id=post.id
        )
'''
class CreatePost(graphene.Mutation):
    class Arguments:
        ca_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, ca_id, title, content, user_id):
        catagory = Catagory.objects.get(id=ca_id)
        user = User.objects.get(id=user_id)
        post = Post.objects.create(catagory=catagory, user=user, post_title=title, post_content=content)
        return CreatePost(
            success=True
        )


class CreateCatagory(graphene.Mutation):
    class Arguments:
        ca_name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, ca_name):
        catagory = Catagory(ca_name=ca_name)
        catagory.save()

        return CreateCatagory(
            success=True
        )


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        content = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, id, title, content):
        post = Post.objects.get(pk=id)
        post.post_title = title if title is not None else post_title
        post.post_content = content if content is not None else post_content
        post.save()
        return UpdatePost(
            success=True
        )


'''
Manager' object is not callable
class InputUpdateCatagory(graphene.InputObjectType):
    ca_name = graphene.String()


class UpdateCatagory(graphene.Mutation):
    class Arguments:
        ca_name = graphene.String(required=True)
        data = InputUpdateCatagory(required=True)

    success = graphene.Boolean()

    def mutate(root, info, ca_name, data):
        model = Catagory.objects(
            ca_name=ca_name
        ).first()

        if data.ca_name is not None:
            model.ca_name = ca_name

        model.save()

        return UpdateCatagory(
            success=True
        )
'''

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_catagory = CreateCatagory.Field()
    update_post = UpdatePost.Field()
#   update_catagory = UpdateCatagory.Field()
#   update_user = UpdateUser.Field()


