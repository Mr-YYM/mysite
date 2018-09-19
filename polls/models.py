from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    """
    DateField.auto_now
        Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps.
    DateField.auto_now_add
        Automatically set the field to now when the object is first created. Useful for creation of timestamps.
    """
    created_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    content = models.TextField()
    is_show = models.BooleanField()

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title


# 创建一个自定义的用户模型
class MyUser(AbstractUser):
    # 要继承AbstractBaseUser, 一定要有两个属性：identifier、 USERNAME_FIELD
    # you model must be have a single unique field that can be used for identification purposes.
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'
    # username_validator = UnicodeUsernameValidator()
    #
    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )

    first_name = None
    last_name = None
    is_active = None
    is_staff = None
    is_superuser = None

    score = models.IntegerField('积分', default=0)

    # Give your model metadata(元数据) by using an inner class Meta
    # Model metadata is “anything that’s not a field”,
    # such as ordering options, database table name,
    # or human-readable singular(单数) and plural(复数) names.
    # None are required, and adding class Meta to a model is completely optional.
    # 子类：元数据，设置一些属性。
    # 数据库中显示的名称
    class Meta:
        db_table = 'Myuser'

    # Shell中实例显示的名称
    def __str__(self):
        return self.username

