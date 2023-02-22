from django.shortcuts import render
from .serializers import Registerizer, RegisterizerArticle
from .models import Registration_title, Registration_article
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import APIView,api_view
def main(request):
    # queryset2 = Registration_article.objects.all()
    # serializer_class2 = RegisterizerArticle(queryset2)
    # print(serializer_class1, serializer_class2)
    return render(request, 'main/main.html')
## api class 기반 1
# class Register_serializer(APIView):
#     def get(self, request):
#         queryset1 = Registration_title.objects.all()            
#         serializer_class1 = Registerizer(queryset1, many = True)  
#         return Response(serializer_class1.data)
## api class 기반 2
class Register_serializer(viewsets.ModelViewSet):
    queryset = Registration_title.objects.all()            
    serializer_class = Registerizer
## api 함수 기반 
# @api_view(['GET','POST'])
# def register_serializer(request):
#     queryset1 = Registration_title.objects.all()
#     serializer_class1 = Registerizer(queryset1, many = True)
#     print('sdgasgasgdsgsdgsdgsgsagsdgasg',serializer_class1)
#     return Response(serializer_class1.data)
