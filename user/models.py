from django.db import models

# Create your models here.
# 유저 정보
class Account(models.Model):
    user = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    account_typ = models.ForeignKey('Account_Type', on_delete=models.CASCADE)
    del_flg = models.CharField(max_length=1, default="0")
    last_update_datetime = models.DateTimeField(auto_now=True)
    last_update_pageId = models.CharField(max_length=100)

    def __str__(self):
        return self.user + ", "
        + self.user_name + ", "
        + self.nickname + ", "
        + self.password + ", "
        + self.account_typ + ", "
        + self.del_flg + ", "
        + self.last_update_datetime + ", "
        + self.last_update_pageId

class Account_Type(models.Model):
    account_typ_nm = models.CharField(max_length=10)
    del_flg = models.CharField(max_length=1, default="0")
    last_update_datetime = models.DateTimeField(auto_now=True)
    last_update_pageId = models.CharField(max_length=100)

    def __str__(self):
        return self.account_typ_nm + ", "
        + self.del_flg + ", "
        + self.last_update_datetime + ", "
        + self.last_update_pageId
