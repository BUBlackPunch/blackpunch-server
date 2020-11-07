import graphene
from graphene_django import DjangoObjectType
from bbp.models import (Post,Catagory,Answer,Comment,Tag,Like)


class CatagoryType(DjangoObjectType):
    class Meta:
        model = Catagory

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class LikeType(DjangoObjectType):
    class Meta:
        model = Like

class Query(object):
    all_catagory=graphene.List(CatagoryType)
    catagory=graphene.Field(CatagoryType, id=graphene.Int())
    all_post=graphene.List(PostType)
    post=graphene.Field(PostType, id=graphene.Int())
    all_answer=graphene.List(AnswerType)
    answer=graphene.Field(AnswerType, id=graphene.Int())
    all_comment=graphene.List(CommentType)
    comment=graphene.Field(CommentType, id=graphene.Int())
    all_tag=graphene.List(TagType)
    tag=graphene.Field(TagType, id=graphene.Int())
    all_like=graphene.List(LikeType)
    like=graphene.Field(LikeType, id=graphene.Int())

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Post.objects.get(pk=id)
        
        return None
    
    def resolve_all_post(self, info, **kwargs):
        return Post.objects.all()
    
    def resolve_answer(self, ifo, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Answer.objectcs.get(pk=id)
        
        return None


    def resolve_all_answer(self, info, **kwargs):
        return Answer.objects.all()

    def resolve_tag(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Tag.objects.get(pk=id)
        
        return None
    
    def resolve_all_tag(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_comment(self,info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

    def resolve_all_comment(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_cataogry(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Catagory.objects.get(pk=id)
        
        return None
    
    def resolve_all_catagory(self, info, **kwargs):
        return Catagory.objects.all()


    def resolve_like(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Like.objects.get(pk=id)
        
        return None
    def resolve_all_like(self, info, **kwargs):
        return Like.objects.all()
    
class CreatePost(graphene.Mutation):

        class Arguments:
            title = graphene.String()
            content = graphene.String()
            date = graphene.DateTime()

        post = graphene.Field(PostType)

        def mutate(self, info, title, content, date):
            post = Post.objects.create(
                post_title = title,
                post_content = content,
                post_datatime = date,
            )
            post.save()

            return CreatePost(post=post)

class UpdatePost(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        content = graphene.String()
        modify_date = graphene.DateTime()

    post = graphene.Field(PostType)
    
    def mutate(self, info, id, title, content, modify_date):
        post = Post.objects.get(pk=id)
        post_title = title if title is not None else post_title
        post_content = content if content is not None else post_content
        post_modify_datatime = modify_date if modify_date is not None else post_modify_datatime

        post.save()

        return UpdatePost(post=post)
    
class DeletePost(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
    
    post = graphene.Field(PostType)

    def mutate(self, info, id):
        post = Post.objects.get(pk=id)
        if post is not None:
            post.delete()
        
        return DeletePost(post=post)


class CreateAnswer(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        date = graphene.DateTime()
    
    answer = graphene.Field(AnswerType)

    def mutate(self, info, content, date):
        answer = Answer.objects.create(
            answer_content = content,
            as_datetime = date
        )

        answer.save()

        return CreateAnswer(answer=answer)

class UpdateAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        content = graphene.String()
        modify_date = graphene.DateTime()
    
    answer = graphene.Field(AnswerType)

    def mutate(self, info, id, content, modify_date):
        answer = Answer.objects.get(pk=id)
        answer_content = content if content is not None else answer_content
        as_modify_datetim = modify_date if modify_date is not None else as_modify_datetim

        answer.save()

        return UpdateAnswer(answer=answer)

class DeleteAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    answer = graphene.Field(AnswerType)

    def mutate(self, info, id):
        answer = Answer.objects.get(pk=id)
        if answer is not None:
            answer.delete()

        return DeleteAnswer(answer=answer) 

class CreateComment(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        date = graphene.DateTime()
    
    comment = graphene.Field(CommentType)

    def mutate(self, info, content, date):
        
        comment = Comment.objects.create(
            cm_content21 = content,
            cm_datetime = date
        )

        comment.save()

        return CommentType(comment=comment)

class UpdateComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        content = graphene.String()
        modify_date = graphene.DateTime()
    
    comment = graphene.Field(CommentType)

    def mutate(self, info, id, content, modify_date):
        id =Comment.objects.get(pk=id)
        cm_content = content if content is not None else cm_content
        cm_modify_datetime = modify_date if modify_date is not None else cm_modify_datetime

        comment.save()

        return UpdateComment(comment=comment)

class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    comment = graphene.Field(CommentType)

    def mutate(self, info, id):
        comment = Comment.objects.get(pk=id)

        if comment is not None:
            comment.delete()
    
        return DeleteComment(comment=comment)

class CreateTag(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    tag = graphene.Field(TagType)

    def mutate(self, info, name):
        tag = Tag.objects.create(
            tag_name = name
        )

        tag.save()

        return CreateTag(tag=tag)

class UpdateTag(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
    
    tag = graphene.Field(TagType)

    def mutate(self, info, id, name):
        tag = Tag.get(pk=id)
        tag_name = name if name is not None else tag_name

        tag.save()

        return UpdateTag(tag=tag)

class DeleteTag(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    tag = graphene.Field(TagType)

    def mutate(self, info, id):
        tag = Tag.objects.get(pk=id)
        if tag is not None:
            tag.delete()
        
        return DeleteTag(tag=tag)

class CreateLike(graphene.Mutation):
        id = graphene.ID()
        date = graphene.DateTime()
        ip = graphene.String()

        class Arguments:
            date = graphene.DateTime()
            ip = graphene.String()
        
        def mutate(self, info, date, ip):
            like = Like(lk_datetime=date, li_ip=ip)
            like.save()

            return CreateLike(
                id = like.id,
                ip = like.li_ip,
            )

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    create_answer = CreateAnswer.Field()
    update_answer = UpdateAnswer.Field()
    delete_answer = DeleteAnswer.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
    create_tag = CreateTag.Field()
    update_tag = UpdateTag.Field()
    delete_tag = DeleteTag.Field()
    create_like = CreateLike.Field()    