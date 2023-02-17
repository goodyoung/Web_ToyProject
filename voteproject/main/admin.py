from django.contrib import admin
from .models import Registration_title, Registration_article, UserInfo, Proposal

#UserInfo Admin
admin.site.register(UserInfo)

#Proposal Admin
admin.site.register(Proposal)

# title 검색기능
@admin.register(Registration_title)
class TitleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
#article 제목 기준 정렬 / title-article-count 보여주기
@admin.register(Registration_article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('display_title','article','count')
    def display_title(self, titles):
        return titles.registration_id.title # 
    display_title.short_description = '제목' # display 할 제목
    display_title.admin_order_field  = 'registration_id' #정렬 기능 
