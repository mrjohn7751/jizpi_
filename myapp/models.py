from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Custom User modeli
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

# Ekran Rasmi
class ekranImages(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Photos/ekran_IMG/')

    class Meta:
        verbose_name = _("Ekran Rasmi")
        verbose_name_plural = _("Ekran Rasmlari")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ekranImages_detail", kwargs={"pk": self.pk})

# Category Yangiliklar (News)
class ArticleNews(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Sarlovha'))
    body = models.TextField(verbose_name=_('Tana qismi'))
    img = models.ImageField(upload_to='Photos/Yangiliklar/')
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    created_at = models.CharField(max_length=10, verbose_name=_('Sana kiritish'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ArticleNews_details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Maqola")
        verbose_name_plural = _("Maqolalar")

class ArticleElon(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Sarlovha'))
    body = models.TextField(verbose_name=_('Tana qismi'))
    img = models.ImageField(upload_to='Photos/Yangiliklar/')
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/')
    created_at = models.CharField(max_length=10, verbose_name=_('Sana kiritish'))


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Elon")
        verbose_name_plural = _("Elonlar")

class ArticleQabul2024(models.Model):
    file1 = models.FileField(upload_to='qabul/')
    file2 = models.FileField(upload_to='qabul/')
    file3 = models.FileField(upload_to='qabul/')
    file4 = models.FileField(upload_to='qabul/')
    file5 = models.FileField(upload_to='qabul/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _("Hujjat")
        verbose_name_plural = _("Hujjatlar")


class Korupsiya(models.Model):
    title = models.CharField(max_length=250)
    title_en = models.CharField(max_length=250, blank=True, null=True)
    title_ru = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField()
    body_en = models.TextField(blank=True, null=True)
    body_ru = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='Photos/Yangiliklar/')
    img1 = models.ImageField(upload_to='Photos/Yangiliklar/')
    img2 = models.ImageField(upload_to='Photos/Yangiliklar/')
    img3 = models.ImageField(upload_to='Photos/Yangiliklar/')
    video = models.CharField(max_length=500)
    publish_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('korupsiya_detail', kwargs={'pk': self.pk})
    
    
    class Meta:
        ordering = ['-publish_time']
        
    

    def __str__(self):
        return self.title