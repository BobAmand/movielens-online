# from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
#
#
# def Profile()
# import re
from django.db import models
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

# Create your models here.

# def is_valid_twitter_name(value):
#     if not re.match(r'@\w+', value):
#         raise ValidationError(
                                # 'Invalid Twitter username - \
                                # must start with @ and only \
                                # contain alphanumeric characters')


# class Profile(models.Model):
#
#     MALE = 'M'   # Constants for controlled entry
#     FEMALE = 'F'
#     OTHER = 'O'
#     X = 'X'
#
#     GENDER_SELECT = (
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#         (OTHER, 'Other'),
#         (X, 'No Data')
#     )
#
#     user = models.OneToOneField(User, null=True)
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=1, choices=GENDER_SELECT, null=True)
#     occupation = models.IntegerField(default=0)
#     zipcode = models.CharField(max_length=5, null=True)
#
# #    favorite_color = models.CharField(max_length=50, null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)
#     web_address = models.URLField(null=True, blank=True)
#     # twitter_username = \
#     #     models.CharField(max_length=16, null=True, blank=True,
#     #                      validators=[RegexValidator(r'@\w+',
#     #                                  message=
#     #                                  'Twitter names must be composed \
#     #                                  of alphanumeric characters')])
#     # following = models.ManyToManyField('Profile', related_name='followers')
#
#     def __str__(self):
#         return str(self.user)
