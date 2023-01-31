from django.contrib import admin
from blog.models import * 


class user_id(admin.ModelAdmin):
	list_display = ('userid','password','fristname','lastname')
	search_fields = ('userid','password','fristname','lastname')


admin.site.register(Blog)
admin.site.register(Game)
admin.site.register(Document)
admin.site.register(Rapper)
admin.site.register(UserID,user_id)

# Register your models here.
