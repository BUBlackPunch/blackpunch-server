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
    post_search = graphene.Field(PostType, id=graphene.Int())
    answer = graphene.List(AnswerType)
    catagory = graphene.List(CatagoryType)
    comment = graphene.List(CommentType)
    tag = graphene.List(TagType)


    def resolve_post(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post_search(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Post.objects.get(id=id)

    def resolve_post_test(self, info, **kwargs):
        ts = kwargs.get("id")
        if id is not None:
            return Post.objects.get(id=id)

    def resolve_answer(self, info, **kwargs):
        return Answer.objects.all()

    def resolve_catagory(self, info, **kwargs):
        return Catagory.objects.all()

    def resolve_comment(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_tag(self, info, **kwargs):
        return Tag.objects.all()




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


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=False)
        content = graphene.String(required=False)

    success = graphene.Boolean()

    def mutate(self, info, id, title, content):
        post = Post.objects.get(pk=id)
        post.post_title = title if title is not None else post_title
        post.post_content = content if content is not None else post_content
        post.save()
        return UpdatePost(
            success=True
        )


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        post = Post.objects.get(pk=id)
        if post is not None:
            post.delete()

        return DeletePost(
            success=True
        )


class CreateAnswer(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        content = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, post_id, content, user_id):
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
        answer = Answer.objects.create(post=post, user=user, as_content=content)
        return CreateAnswer(
            success=True
        )


class UpdateAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        content = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, content):
        answer = Answer.objects.get(pk=id)
        answer.as_content = content if content is not None else as_content
        answer.save()
        return UpdateAnswer(
            success=True
        )


class DeleteAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        answer = Answer.objects.get(pk=id)
        if answer is not None:
            answer.delete()

        return DeleteAnswer(
            success=True
        )


class CreateComment(graphene.Mutation):
    class Arguments:
        answer_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        content = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, answer_id, content, user_id):
        answer = Answer.objects.get(id=answer_id)
        user = User.objects.get(id=user_id)
        comment = Comment.objects.create(answer=answer, user=user, cm_content=content)
        return CreateComment(
            success=True
        )


class UpdateComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        content = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, content):
        comment = Comment.objects.get(pk=id)
        comment.cm_content = content if content is not None else cm_content
        comment.save()
        return UpdateAnswer(
            success=True
        )


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        comment = Comment.objects.get(pk=id)

        if comment is not None:
            comment.delete()

        return DeleteComment(
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


class UpdateCatagory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, name):
        catagory = Catagory.objects.get(pk=id)
        catagory.ca_name = name if name is not None else ca_name
        catagory.save()
        return UpdateAnswer(
            success=True
        )


class DeleteCatagory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        catagory = Catagory.objects.get(pk=id)
        if catagory is not None:
            catagory.delete()

        return DeleteCatagory(
            success=True
        )


class CreateTag(graphene.Mutation):
    class Arguments:
        tag_name = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(root, info, tag_name):
        tag = Tag.objects.create(tag_name=tag_name)
        return CreateTag(
            success=True
        )




class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_answer = CreateAnswer.Field()
    create_comment = CreateComment.Field()
    create_tag = CreateTag.Field()
    create_catagory = CreateCatagory.Field()
    update_post = UpdatePost.Field()
    update_answer = UpdateAnswer.Field()
    update_comment = UpdateComment.Field()
    update_catagory = UpdateCatagory.Field()
    delete_post = DeletePost.Field()
    delete_answer = DeleteAnswer.Field()
    delete_comment = DeleteComment.Field()
    delete_catagory = DeleteCatagory.Field()


