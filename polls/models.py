from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser


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


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓直接继承AbstractUser能够有效运行↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 创建一个自定义的用户模型
class MyUser(AbstractUser):

    score = models.IntegerField('积分', default=0)

    # Give your model metadata(元数据) by using an inner class Meta
    # Model metadata is “anything that’s not a field”,
    # such as ordering options, database table name,
    # or human-readable singular(单数) and plural(复数) names.
    # None are required, and adding class Meta to a model is completely optional.
    # 子类：元数据，设置一些属性。
    # 数据库中显示的名称
    class Meta(AbstractUser.Meta):
        db_table = 'Myuser'

    # Shell中实例显示的名称
    def __str__(self):
        return self.username

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑直接继承AbstractUser能够有效运行↑↑↑↑↑↑↑↑↑↑↑↑↑↑


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓继承AbstractBaseUser↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 这个类少了username, email，需要自己定制，直接拿源码会报错，username = AbstractUser.username,也会报错

# class Myuser(AbstractBaseUser):
    # objects = UserManager()

    # 要继承AbstractBaseUser, 一定要有两个属性：identifier、 USERNAME_FIELD
    # you model must be have a single unique field that can be used for identification purposes.
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'
    #
    # 源码的username
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

    # email = models.EmailField(_('email address'), blank=True)

    # EMAIL_FIELD = 'email'
    #
    # class Meta(AbstractUser.Meta):
    #     db_table = 'Myuser'
    #
    # # Shell中实例显示的名称
    # def __str__(self):
    #     return self.username

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑继承AbstractBaseUser↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓继承AbstractUser↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 这个用户模型有多余的Field，重写直接赋值None，报错...

# class Myuser(AbstractUser):
    # first_name = None
    # last_name = None
    # is_active = None
    # is_staff = None
    # is_superuser = None

    # class Meta(AbstractUser.Meta):
    #     db_table = 'Myuser'
    #
    # # Shell中实例显示的名称
    # def __str__(self):
    #     return self.username

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑继承AbstractUser↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
