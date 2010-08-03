from django.db import models
from django.contrib import admin

class User(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    IMS_CHOICES = (
        (u'Google', u'Google'),
        (u'Skype', u'Skype'),
        (u'AIM', u'AIM'),
        (u'MSN', u'MSN'),
        (u'Yahoo', u'Yahoo'),
        (u'Jabber', u'Jabber'),
    )
    userId = models.AutoField("UserId",primary_key=True)
    email = models.EmailField("Email",max_length=60,unique=True)
    name = models.CharField("Name",max_length=100)
    passwd = models.CharField("Password",max_length=12)
    twitterId = models.CharField("Twitter Id",max_length=60)
    ims = models.CharField("IMS",max_length=60)
    imsType = models.CharField("IMS Type ",max_length=30)
    openId = models.CharField("Open id", max_length=60)
    birthday = models.DateField("Birthday")
    registeredSince = models.DateField("Registered Since")
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    about = models.CharField("About",max_length=300)
    site = models.CharField("Site",max_length=50)
    
    #class Meta:
    #    db_table = 'user'
    #    app_label = ''

       
class Tag(models.Model): 
    tagId = models.AutoField("TagId",primary_key=True)
    description = models.CharField("Description",max_length=200)
    
    #class Meta:
    #    db_table = 'tag'
    #    app_label = ''

class Item(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField("Name",max_length=100,unique=True)
    link = models.CharField("Link",max_length=200)
    tag = models.ForeignKey(Tag)
    info = models.CharField("Additional Info",max_length=100)
    
    #class Meta:
    #    db_table = 'item'
    #    app_label = ''
# Create your models here.
