
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User
from rest_framework import serializers


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

