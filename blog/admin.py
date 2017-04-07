from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'modify_date')  # 어드민 페이지의 Post 목록에서 보여질 항목
    list_filter = ('modify_date', )  # 어드민 페이지 오른쪽에 필터로 보여질 항목
    search_fields = ('title', 'content')    # 검색박스를 표시하고 입력된 단어는 title, content 컬럼에서 검색
    prepopulated_fields = {'slug': ('title', )}  # slug 필드는 title 필드를 이용하여 미리 채워짐

admin.site.register(Post, PostAdmin)    # Post 와 PostAdmin 클래스를 Admin 사이트에 등록
