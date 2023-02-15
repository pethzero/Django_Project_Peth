from django.contrib import admin
from blog.models import * 


class user_id(admin.ModelAdmin):
	list_display = ('userid','password','fristname','lastname')
	search_fields = ('userid','password','fristname','lastname')

class doc_list(admin.ModelAdmin):
	list_display = ('docid','document')
	search_fields = ('docid','document')

admin.site.register(Blog)
admin.site.register(Game)
admin.site.register(Document,doc_list)
admin.site.register(Rapper)
admin.site.register(Company_Category)
admin.site.register(UserID,user_id)
admin.site.register(Personal_data)
# Register your models here.
