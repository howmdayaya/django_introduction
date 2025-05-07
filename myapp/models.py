from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    #主键id会自动生成，可以不写
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=11)
    addtime = models.DateTimeField(default=datetime.now)

#class Meta:
#    db_table = "users"  # 指定表名，不指定默认表名为：应用名_类名小写，即：myapp_users