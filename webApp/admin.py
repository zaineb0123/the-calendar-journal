from django.contrib import admin
from .models import User, Day, Category, TodoList

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class DayAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'date',)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class TodoListAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TodoList, TodoListAdmin)