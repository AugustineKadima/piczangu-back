from django.contrib import admin
from .models import Photographer,Event,Rating, PhotographerAccount,BoughtPhotos,Portfolio,Photos,PhotoUsers,Client,User

# Register your models here
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Photographer)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(PhotographerAccount)
admin.site.register(BoughtPhotos)
admin.site.register(Portfolio)
admin.site.register(Photos)
admin.site.register(PhotoUsers)