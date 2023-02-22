from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=30, primary_key=True, blank=False, unique=True) # unique 는 안했다
    name = models.CharField(max_length=30, blank=False, null = False)
    password1 = models.CharField(max_length=200, blank=False, null = False)
    password2 = models.CharField(max_length=200, blank=False, null=False)
    telephone = models.CharField(max_length=200, blank=False, null = False)
    email = models.CharField(max_length=200, blank=False, null = False)
    
class Proposal(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, db_column='user_id') # do_nothing으로 바꿈
    id  = models.AutoField(primary_key = True)  # primarykey를 id로 사용하고 싶으면 지우자
    title = models.CharField(max_length=200, blank=False, null = False)
    content = models.TextField(max_length=200, blank=False, null = False)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title
    
class Registration_title(models.Model):
    title = models.CharField(max_length=200, blank=False, null = False)
    id = models.AutoField(primary_key = True)
    def __str__(self):
        return self.title
    
class Registration_article(models.Model):
    registration_id = models.ForeignKey(Registration_title, on_delete=models.CASCADE, db_column='registration_id')
    id = models.AutoField(primary_key = True)
    article = models.CharField(max_length=30, blank=False, null = False)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.article
    
# userinfo 에서 id(primary)가 비워진 상태로 db에 업데이트를 해도 빈칸으로 나온다..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
