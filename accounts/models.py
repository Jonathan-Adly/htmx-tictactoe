from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db import models


"""
Our Board should look like this initially = [[0,0,0],[0,0,0],[0,0,0]]
Then as players play, it should look like this = [[x,0,y], [x,y,0], [0,0,0]]
"""


class CustomUser(AbstractUser):
    def get_default():
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    player = models.CharField(max_length=1, default="X")
    board = ArrayField(ArrayField(models.IntegerField()), default=get_default)
