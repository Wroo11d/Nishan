import uuid

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

from config.utils.models import Entity

User = get_user_model()

class ProductManager(models.Manager):
    def select(self):
        return self.get_queryset().select_related('vendor', 'category', 'label', 'merchant')

class notification(Entity):
    title = models.CharField('title', max_length=255)
    sender = models.CharField('sender', max_length=255)
    time = models.TimeField('time', null=True, auto_now = False, auto_now_add = False, blank=True, max_length=255)
    description = models.TextField('description', null=True, blank=True)
    image = models.ImageField('image', upload_to='notifications/')

    def __str__(self):
        return self.title



class service(Entity):
    name = models.CharField('name', max_length=255)
    description= models.TextField('description',  )
    time = models.TimeField('time',auto_now = False, auto_now_add = True, max_length=255)
    center=models.ForeignKey('center',related_name='services',null=True, blank=True,on_delete=models.CASCADE)
    price = models.DecimalField('price',max_digits=10, decimal_places=2)
    latitude = models.CharField('latitude', max_length=255)
    longitude = models.CharField('longitude', max_length=255)
    location = models.CharField('location', max_length=255)
    is_feature = models.BooleanField('is feature')
    background_image = models.ImageField('background_image', upload_to='service/')
    label = models.ForeignKey('Label', related_name='services', null=True, blank=True,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Service_image(Entity):
    image = models.ImageField('image', upload_to='service/')
    service = models.ForeignKey('service',verbose_name='service', related_name='Service_images', null=True, blank=True,on_delete=models.CASCADE)

    """def __str__(self):
        return str(self.service.images)"""



    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            # print(self.image.path)




class center(Entity):
    name = models.CharField('name',null=True, blank=True, max_length=255)
    open_days = models.DateField('open_days', auto_now = False, auto_now_add = False,null=True, blank=True, max_length=255)
    close_days = models.DateField('close_days', auto_now = False, auto_now_add = False,null=True, blank=True, max_length=255)
    open_time = models.TimeField('open_time',auto_now = False, auto_now_add = False,null=True, blank=True)
    close_time = models.TimeField('close_time',auto_now = False, auto_now_add = False,null=True, blank=True)
    description= models.TextField('description', blank=True, null=True)
    # location = models.CharField('location',null=True, blank=True, max_length=255)
    latitude = models.CharField('latitude', max_length=255)
    longitude = models.CharField('longitude', max_length=255)
    location = models.CharField('location', max_length=255)
    is_feature = models.BooleanField('is feature')

    image = models.ImageField('image', upload_to='centers/')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)



    def __str__(self):
        return self.name

class Center_image(Entity):
    image = models.ImageField('image', upload_to='center/')
    center = models.ForeignKey('center', verbose_name='center', related_name='Center_images', null=True, blank=True,on_delete=models.CASCADE)

    """def __str__(self):
        return self.center.images"""

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            # print(self.image.path)



class advertising(Entity):
    title = models.CharField('title',null=True, blank=True, max_length=255)
    url = models.CharField('url',null=True, blank=True, max_length=255)
    description = models.TextField('description',  blank=True, null=True)
    # center = models.ForeignKey('center', related_name='advertisings', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='advertisings/')

    def __str__(self):
        return self.title

class news(Entity):
    title = models.CharField('name',null=True, blank=True, max_length=255)
    description= models.TextField('description',  blank=True, null=True)
    image = models.ImageField('image', upload_to='service/')


    def __str__(self):
        return self.title

class ServiceOpinion(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='ServiceOpinions', on_delete=models.CASCADE)
    description = models.TextField('description',  blank=True, null=True)
    rating = models.DecimalField('rating',max_digits=1, decimal_places=0)
    service = models.ForeignKey('service', related_name='ServiceOpinions', on_delete=models.CASCADE)
    time = models.TimeField('time',auto_now = False, auto_now_add = False, null=True, blank=True)

    """def __str__(self):
        return str(self.user)"""

class CenterOpinion(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='CenterOpinions', on_delete=models.CASCADE)
    rating = models.DecimalField('rating',max_digits=1, decimal_places=0)

    description = models.TextField('description',  blank=True, null=True)
    center = models.ForeignKey('center', related_name='CenterOpinions', on_delete=models.CASCADE)
    time = models.TimeField('time',auto_now = False, auto_now_add = False, null=True, blank=True)

    """def __str__(self):
        return str(self.user)"""

class reservation(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='reservations', on_delete=models.CASCADE)
    service = models.ForeignKey('service', related_name='reservations', on_delete=models.CASCADE)
    title = models.CharField('name',null=True, blank=True, max_length=255)
    time = models.TimeField('time',auto_now = False, auto_now_add = False,null=True, blank=True)
    is_active = models.BooleanField('is active')

    """def __str__(self):
        return self.title"""


class Label(Entity):
    name = models.CharField('name', max_length=255)

    class Meta:
        verbose_name = 'label'
        verbose_name_plural = 'labels'

    def __str__(self):
        return self.name


class Favorites(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='Favorites', on_delete=models.CASCADE)
    service = models.ForeignKey('service', related_name='Favorites', on_delete=models.CASCADE)
