from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Category, Item, Staff, Branch, Transaction

admin.site.site_header = 'Warehouse Management System'
admin.site.index_title = 'Admin Panel'                
admin.site.site_title = 'administration pane'

admin.site.unregister(Group)
admin.site.unregister(User)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['approval', 'item_id', 'name', 'category', 'quantity', 'start_date', 'exp_date']
	list_filter = ['approval', 'category', 'quantity', 'start_date', 'exp_date']
	search_fields = ['name',]

class StaffAdmin(admin.ModelAdmin):
	list_display = ['staff_id', 'staff_name', 'staff_phone', 'staff_join', 'staff_out']
	list_filter = ['staff_join', 'staff_out']
	search_fields = ['staff_name',]

class BranchAdmin(admin.ModelAdmin):
	list_display = ['place', 'description', 'address']
	list_filter = ['address']
	search_fields = ['place', 'address',]

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['trans_id', 'quantity', 'time', 'item', 'client']
	list_filter = ['time', 'quantity', 'client', 'item']
	search_fields = ['items',]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Transaction, TransactionAdmin)