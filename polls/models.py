from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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
class MyUser(AbstractBaseUser):
    # 自定义的 User 要继承AbstractUser。并且一定要有两个属性：identifier、 USERNAME_FIELD
    # you model must be have a single unique field that can be used for identification purposes.
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'

    score = models.IntegerField('积分', default=0)

    # 数据库中显示的名称
    class Meta:
        db_table = 'Myuser'

    # Shell中实例显示的名称
    def __str__(self):
        return self.USERNAME_FIELD

