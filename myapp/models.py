from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username





# Ekran Rasmi

class ekranImages(models.Model):
    name = models.CharField( max_length=50)
    img = models.ImageField(upload_to='Photos/ekran_IMG/',)

    class Meta:
        verbose_name = "Ekran Rasmi"
        verbose_name_plural ="Ekran Rasmlari"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ekranImages_detail", kwargs={"pk": self.pk})

# Category Yangiliklar (News)

    
class ArticleNews(models.Model):
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleNews_details", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Maqola"
        verbose_name_plural="Maqolalar"
        
    

    
    
class ArticleElon(models.Model):
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Elon"
        verbose_name_plural="Elonlar"
        
        
        
        
class ArticleQabul2024(models.Model):
    file1 = models.FileField( upload_to='qabul/')
    file2 = models.FileField( upload_to='qabul/')
    file3 = models.FileField( upload_to='qabul/')
    file4 = models.FileField( upload_to='qabul/')
    file5 = models.FileField( upload_to='qabul/',null=True, blank=True)
    
    
    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name="Hujjat"
        verbose_name_plural="Hujjatlar"