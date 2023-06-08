from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, ToolUser,StoreItems,StoreItems2
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserModel(UserAdmin):
    pass


@admin.register(StoreItems)
class DataAdmin1(ImportExportModelAdmin):
    pass

@admin.register(StoreItems2)
class DataAdmin2(ImportExportModelAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(ToolUser)

