from rest_framework import serializers
from .models import Student_Profile, School, Teacher_Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

from rest_framework import status, generics, permissions


# Email verification
# from django.contrib.auth import authenticate, get_user_model
# from djoser.conf import settings
# from djoser.serializers import TokenCreateSerializer

# User = get_user_model()

# class CustomTokenCreateSerializer(TokenCreateSerializer):

#     def validate(self, attrs):
#         password = attrs.get("password")
#         params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
#         self.user = authenticate(
#             request=self.context.get("request"), **params, password=password
#         )
#         if not self.user:
#             self.user = User.objects.filter(**params).first()
#             if self.user and not self.user.check_password(password):
#                 self.fail("invalid_credentials")
#         # We changed only below line
#         if self.user: # and self.user.is_active: 
#             return attrs
#         self.fail("invalid_credentials")

#-------------------------------------------------------#



class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    usertype = serializers.CharField()

    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        password=make_password(validated_data['password'])
        )
        if validated_data['usertype']=="School":
            profile = School.objects.create(username=user)

        elif validated_data['usertype']=="Teacher":
            profile = Teacher_Profile.objects.create(username=user)

        elif validated_data['usertype']=="Student":
            profile = Student_Profile.objects.create(username=user)
        return validated_data

        # return Response(profile, status=status.HTTP_201_CREATED)


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Student_Profile
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = School
        fields = '__all__'

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Teacher_Profile
        fields = '__all__'


    
# class UserSerializer(serializers.Serializer):
#     username = serializer.CharField()
#     email = serializer.EmailField()
#     password = serializer.PasswordField()
#     password2 = serializer.PasswordField()
#     usertype = serializer.CharField()
#     def validate(self, data):
#             if not data.get('password') or not data.get('password2'):
#                 raise serializers.ValidationError("Please enter a password and "
#                     "confirm it.")
#             if data.get('password') != data.get('password2'):
#                 raise serializers.ValidationError("Those passwords don't match.")
#             return data
    




# class UserSerializer(serializers.ModelSerializer):
    
#     #usertype = serializers.CharField(max_length = 20, write_only=True, allow_blank=False)
#     confirm_password = serializers.CharField(allow_blank=False, write_only=True)
    
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email','password','confirm_password']

#         def validate(self, data):
#             if not data.get('password') or not data.get('password2'):
#                 raise serializers.ValidationError("Please enter a password and "
#                     "confirm it.")
#             if data.get('password') != data.get('password2'):
#                 raise serializers.ValidationError("Those passwords don't match.")
#             return data

        # def create(self, validated_data):
        #     user = User.objects.create(
        #         username=validated_data['username'],
        #         email=validated_data['email'],
        #         password=make_password(validated_data['password'])
        #         # is_superuser=validated_data['is_superuser'],
        #     )

            # if validated_data['usertype']=="School":
            #     profile = School.objects.create(username=user)

            # elif validated_data['usertype']=="Teacher":
            #     profile = Teacher_Profile.objects.create(username=user)

            # elif validated_data['usertype']=="Student":
            #     profile = Student_Profile.objects.create(username=user)

           # return user
