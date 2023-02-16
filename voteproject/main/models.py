from django.db import models

# # Field: [ User Id, User Name, User Password, User Telephone, User Email ]
# class UserInfo(models.Model):
#     userId = models.CharField()

# # Field: [ User Id, Proposal Id, Proposal Title, Content, DateTime ]
# class Proposal(models.Model):
# # Field: [ Proposal Id, Registration Id, Registration Title, Article, Count]
# class Registration(models.Model):
class UserInfo(models.Model):
    user_id = models.CharField(max_length=30,primary_key=True, blank=False)  # unique 는 안했다
    user_name = models.CharField(max_length=30, blank=False, null = False)
    user_password = models.CharField(max_length=200, blank=False, null = False)
    user_telephone = models.CharField(max_length=200, blank=False, null = False)
    user_email = models.CharField(max_length=200, blank=False, null = False)
class Proposal(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, db_column='user_id') # do_nothing으로 바꿈
    proposal_id  = models.AutoField(primary_key = True)  # primarykey를 id로 사용하고 싶으면 지우자
    proposal_title = models.CharField(max_length=200, blank=False, null = False)
    proposal_content = models.TextField(max_length=200, blank=False, null = False)
    proposal_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.proposal_title
class Registration_title(models.Model):
    # registration_id = models.Field(primary_key = True)
    registration_title = models.CharField(max_length=200, blank=False, null = False)
    def __str__(self):
        return self.registration_title
class Registration_article(models.Model):
    registration_id = models.ForeignKey(Registration_title, on_delete=models.CASCADE, db_column='registration_id')
    airticle_num = models.AutoField(primary_key = True)
    article = models.CharField(max_length=30, blank=False, null = False)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.article
    
# userinfo 에서 id(primary)가 비워진 상태로 db에 업데이트를 해도 빈칸으로 나온다..;;;
