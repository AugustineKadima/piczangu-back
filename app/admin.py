from django.contrib import admin
from .models import Photographer,Event,Rating, PhotographerAccount,BoughtPhotos,Portfolio,Photos,PhotoUsers,Client,User,Watermarks,Homepage

# Register your models here
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Photographer)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(PhotographerAccount)
admin.site.register(BoughtPhotos)
admin.site.register(Portfolio)
admin.site.register(Watermarks)
admin.site.register(Homepage)
admin.site.register(Photos)
admin.site.register(PhotoUsers)