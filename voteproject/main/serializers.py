from rest_framework import serializers
from .models import Registration_title,Registration_article

class Registerizer(serializers.ModelSerializer):
    class Meta:
        model = Registration_title
        fields = ('title','id')  # 모든 필드 포함: '__all__'

class RegisterizerArticle(serializers.ModelSerializer):
    class Meta:
        model = Registration_article
        fields = ('registration_id','id','article','count')