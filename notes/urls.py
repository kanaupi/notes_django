#プロジェクトで最初に呼び出される、ここで呼び出されるurls(指示)とどのviews(指示に応じた返答)を返すかを指示

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #admin djangoに最初からついているデータベースなどの管理画面
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
]
