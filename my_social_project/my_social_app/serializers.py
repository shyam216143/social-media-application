from rest_framework.serializers import *
from .models import User
from rest_framework import serializers


class UserRegisterationsSerializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    print("hello")

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'username', 'first_name', 'last_name', ]
        extra_kwargs = {
            'password': {'write_only': True, }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirmed Password not matched")
        return attrs

    def create(self, validate_date):
        print(validate_date, "validate data")
        return User.objects.create_user(**validate_date)


class UserLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'username']


# class ProfileInfoSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']
#
#     def validate(self, attrs):
#         firstName = attrs.get('firstName')
#         lastName = attrs.get('lastName')
#         # gender = attrs.get('gender')
#         # intro = attrs.get('intro')
#         # hometown = attrs.get('hometown')
#         # currentCity = attrs.get('currentCity')
#         # workplace = attrs.get('workplace')
#         # eduInstitution = attrs.get('eduInstitution')
#         # countryName = attrs.get('countryName')
#         # birthDate = attrs.get('birthDate')
#         user = self.context.get('user')
#         # if gender == 'male':
#         #     user.gender = 1
#         # elif gender == 'female':
#         #     user.gender = 2
#         # elif gender == 'transgender':
#         #     user.gender == 3
#         user.first_name = firstName
#         user.last_name = lastName
#         # user.intro = intro
#         # user.hometown = hometown
#         # user.current_city = currentCity
#         # user.country = countryName
#         # user.workplace = workplace
#         # user.edu_institution = eduInstitution
#         # user.birth_date = birthDate
#         user.save()
#         return attrs


class ProfileInfoSerializer(ModelSerializer):
    username = serializers.CharField(max_length=225, style={'input_type': 'username'}, write_only=True)
    first_name = serializers.CharField(max_length=225, style={'input_type': 'firstName'}, write_only=True)
    last_name = serializers.CharField(max_length=225, style={'input_type': 'lastName'}, write_only=True)
    intro = serializers.CharField(max_length=225, style={'input_type': 'intro'}, write_only=True)
    hometown = serializers.CharField(max_length=225, style={'input_type': 'hometown'}, write_only=True)
    current_city = serializers.CharField(max_length=225, style={'input_type': 'currentCity'}, write_only=True)
    workplace = serializers.CharField(max_length=225, style={'input_type': 'workplace'}, write_only=True)
    edu_institution = serializers.CharField(max_length=225, style={'input_type': 'eduInstitution'}, write_only=True)
    country = serializers.CharField(max_length=225, style={'input_type': 'countryName'}, write_only=True)
    birth_date = serializers.CharField(max_length=225, style={'input_type': 'birthDate'}, write_only=True)

    gender = serializers.CharField(max_length=225, style={'input_type': 'gender'}, write_only=True)

    # last_name = serializers.CharField(max_length=225, style={'input_type': 'lastName'}, write_only=True)
    # last_name = serializers.CharField(max_length=225, style={'input_type': 'lastName'}, write_only=True)
    # last_name = serializers.CharField(max_length=225, style={'input_type': 'lastName'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'intro', 'hometown', 'current_city', 'workplace',
                  'edu_institution',
                  'birth_date', 'gender', "country"]

    def validate(self, attrs):
        username = attrs.get('username')
        first_name = attrs.get('first_name')
        intro = attrs.get('intro')
        last_name = attrs.get('last_name')
        hometown = attrs.get('hometown')
        currentCity = attrs.get('current_city')
        workplace = attrs.get('workplace')
        eduInstitution = attrs.get('edu_institution')
        country = attrs.get('country')
        birth_date = attrs.get('birth_date')
        gender = attrs.get('gender')

        user = self.context.get('user')

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.hometown = hometown
        user.intro = intro
        user.current_city = currentCity
        user.workplace = workplace
        user.edu_institution = eduInstitution
        user.country = country
        user.birth_date = birth_date
        user.gender = gender
        user.save()
        return attrs


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'intro', 'hometown', 'current_city', 'workplace',
                  'edu_institution',
                  'birth_date', 'gender', "country"]
