from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactInfo, Client, ClientCard, CallRecord

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)

@admin.register(ClientCard)
class ClientCardAdmin(admin.ModelAdmin):
    list_display = ('client', 'is_primary', 'created_at', 'updated_at')
    list_filter = ('is_primary',)

@admin.register(CallRecord)
class CallRecordAdmin(admin.ModelAdmin):
    list_display = ('client', 'channel', 'state', 'calling_number', 'duration', 'created_at')
    list_filter = ('state', 'created_at')
    search_fields = ('channel', 'calling_number')

