from django.urls import path

from app.views import index, RegisterUser, UserLoginView, logout_user, ApplicationAddView, show_blogs, \
    BlogListAPIView, BlogRetrieveUpdateDestroyAPIView, ApplicationCreateAPIView

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),

    path('add/', ApplicationAddView.as_view(), name='addApp'),
    path('blogs/', show_blogs, name='showblog'),
    path('register/', RegisterUser.as_view(), name='regis'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

urlpatterns += [
    path('api-blogs/', BlogListAPIView.as_view(), name='lc_api_view'),
    path('api-blog/<int:pk>', BlogRetrieveUpdateDestroyAPIView.as_view(), name='rud_api_view'),
    path('api-add/', ApplicationCreateAPIView.as_view(), name='app_list_create_api_view')
]
