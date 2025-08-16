from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField

class Advertisement(models.Model):
    adsImage = models.ImageField(upload_to='ads')
    adsAlt = models.CharField(max_length=60)
    adsUrl = models.CharField(max_length=260)
    adsUploadDate = models.DateField()
    adsEndingDate = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.adsAlt
    
class Basement(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=30, unique=True)
    content = HTMLField()
    strip = models.TextField(blank=True)
    seo = models.TextField()
    advertisement = models.ManyToManyField(Advertisement, blank=True)
    active = models.BooleanField(default=True)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Scheme(Basement):
    def get_absolute_url(self):
        return reverse('scheme', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Scheme'
        verbose_name_plural = 'Scheme'

class Scholarship(Basement):
    def get_absolute_url(self):
        return reverse('docs', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Scholarship'
        verbose_name_plural = 'Scholarships'

class Article(Basement):
    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Counselor(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return 'Counselor'
    
    class Meta:
        verbose_name = 'Counselor'
        verbose_name_plural = 'Counselor'
    
class Storage(models.Model):
    title = models.CharField(max_length=260)
    file = models.FileField(upload_to='file')
    uploadDate = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storage'
    
class Setting(models.Model):
    favicon = models.ImageField(upload_to='')
    facebook = models.CharField(max_length=120)
    quote = models.TextField()

    def __str__(self):
        return 'Setting'
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email} - {self.date}'
    
class Student(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=16)
    collegeName = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=12, blank=True)
    cunselor = models.CharField(default='Mama Shree', editable=False)
    note = models.TextField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name