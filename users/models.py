from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
import uuid
# Create your models here.

class MyUserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, userid, password=None, **kwargs):
        if not userid:
            raise ValueError('아이디는 필수입니다.')
        user = self.model(userid=userid, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
    
    def create_user(self, userid, password,**kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(userid, password, **kwargs)
    
    def create_superuser(self, userid,password, **kwargs):
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        return self._create_user(userid, password, **kwargs)


class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key = True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='PK'
    )

    email = models.EmailField(verbose_name ='이메일')
    username = models.CharField(max_length = 20, verbose_name = '이름')
    nickname = models.CharField(max_length=20, verbose_name='닉네임')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    modify_datetime = models.DateTimeField(auto_now_add=True, verbose_name='정보 수정일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    is_staff = models.BooleanField(default=False, verbose_name='스태프 권한')
    is_superuser = models.BooleanField(default=False, verbose_name='super유저')
    userid = models.CharField(max_length=20, unique=True, verbose_name = '사용자 ID')

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
