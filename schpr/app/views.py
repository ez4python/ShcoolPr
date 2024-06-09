from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Applications, Blog
from app.serializers import BlogModelSerializer


def index(request):
    return render(request, 'app/index.html')


class RegisterUser(CreateView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('app:login')


class UserLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('app:index')


def logout_user(request):
    logout(request)
    return redirect('app:index')


class ApplicationAddView(CreateView):
    model = Applications
    form_class = modelform_factory(Applications, fields=['name', 'surname', 'phone'])
    template_name = 'app/addApplications.html'
    success_url = reverse_lazy('app:index')


def show_blogs(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'app/show_blogs.html', context)


# API Views
class BlogListAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
