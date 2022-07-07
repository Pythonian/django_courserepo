from django.conf import settings
from django.db import models
from django.urls import reverse


class Level(models.Model):
    year = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10, unique=True)

    def get_absolute_url(self):
        return reverse('level', kwargs={'slug': self.slug})

    def __str__(self):
        return self.year


class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    code = models.CharField(max_length=10)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ResourceType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    document = models.FileField(upload_to='materials')
    resource_type = models.ForeignKey(ResourceType, on_delete=models.PROTECT)
    pages = models.PositiveSmallIntegerField()
    lecturer = models.CharField(max_length=50)
    impressions = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('course_material', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Library(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)

    class Meta:
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return f"{self.user.username} Library"
