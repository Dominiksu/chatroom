from django.contrib import admin
from.models import Chatroom, Messages





class UserAdmin(admin.ModelAdmin):
    search_fields = ('username')



class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    list_per_page = 10
    search_fields = ['name', 'created_by__username']

 

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'chat_room__name', 'create_dt' )
    search_fields = ('user__username', 'chat_room__name')
    list_per_page = 20
    list_filter = ['create_dt', 'user__username', 'chat_room__name']



admin.site.register(Chatroom, ChatroomAdmin)
admin.site.register(Messages, MessagesAdmin)
