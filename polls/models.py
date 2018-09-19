from django.db import models
from django.contrib.auth.models import AbstractUser

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

    score = models.IntegerField('积分', default=0)

    # 数据库中显示的名称
    class Meta:
        db_table = 'Myuser'

    # Shell中实例显示的名称
    def __str__(self):
        return self.username

