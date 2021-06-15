from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from main_app.models import Transactions, EarnLoviesOrBuy, Comments, Lovies

# Register your models here.
admin.site.register(Transactions)
admin.site.register(EarnLoviesOrBuy)
admin.site.register(Comments)

class LovieInline(admin.StackedInline) :
    model = Lovies
    can_delete = False
    verbose_name_plural = 'Lovie'

class UserAdmin(BaseUserAdmin):
    inlines = (LovieInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)