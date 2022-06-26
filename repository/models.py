from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)


class Level(models.Model):
    year = models.CharField(max_length=10)


class Material(models.Model):
    name = models.CharField(max_length=100)
