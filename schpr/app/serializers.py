from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from app.models import Blog, Applications


class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'descriptions', 'name', 'date']


class ApplicationModelSerializer(ModelSerializer):
    class Meta:
        model = Applications
        fields = ['name', 'surname', 'phone']

    def validate_name(self, name):
        if not name.isalpha():
            raise ValidationError('Name can only consist of letters!')
        return name

    def validate_surname(self, surname):
        if not surname.isalpha():
            raise ValidationError('Surname can only consist of letters!')
        return surname

    def validate_phone(self, phone):
        if Applications.objects.filter(phone=phone).exists():
            raise ValidationError('This phone number is already registered!')
        return phone
