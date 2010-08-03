from sites.portal.models import User
from sites.portal.models import Item
from sites.portal.models import Tag
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
	
     fieldsets = [
        ('Login', 	{'fields': ['email','passwd']}),
        ('Detalhes',  	{'fields': ['name','birthday','gender','registeredSince','about'], 'classes': ['collapse']}),
        ('Contatos',  	{'fields': ['twitterId','ims','imsType','openId','site'], 'classes': ['collapse']})
   
     ]
     
     list_display = ('userId','name','email','registeredSince')

admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(Tag)
