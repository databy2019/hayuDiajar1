#taskmate\taskmate\urls.py
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views
from users_app import views

urlpatterns = [
    path('minda/', admin.site.urls),

    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    #path('hasil', include('todolist_app.urls')),
]
