from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Если в пути указать админ, то откроется админская панель
    path('admin/', admin.site.urls),
    # Тут отправляет нас в файл main.urls, где все доступные ссылки есть
    path('', include('main.urls'))
    
]
#python manage.py runserver