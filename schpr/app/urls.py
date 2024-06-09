from django.urls import path, include

from app.views import index, RegisterUser, UserLoginView, logout_user, ApplicationAddView, show_blogs

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),

    path('add/', ApplicationAddView.as_view(), name='addApp'),
    path('blogs/', show_blogs, name='showblog'),

    path('register/', RegisterUser.as_view(), name='regis'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

