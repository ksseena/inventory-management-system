from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (4, "Buyer"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
   

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Used as User Type
class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE,blank=False,null=False)
    function = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Used  as Tool Room
class ToolUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return "%s" % (self.admin.first_name)

class StoreItems(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    project = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    im_part_no = models.CharField(max_length=100)
    po_number = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100)
    item_name  = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/%Y/%m/%d/', blank=True, default = 'product_images/no_attach.png', null=True)
    mfr_part_no = models.CharField(max_length=100)
    dummy_part_no = models.CharField(max_length=100)
    mfr  = models.CharField(max_length=100)
    current_stock = models.CharField(max_length=100)
    uom  = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    total_value_wo_gst_usd = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    function = models.CharField(max_length=20)
    dri_name = models.CharField(max_length=100)
    life_cycle = models.CharField(max_length=100)
    def __str__(self):
        return  self.item_name
    
    @property
    def Total_cost(self):
        u = int(self.unit_price)
        c = int(self.current_stock)
        return round(float(u* c))

class StoreItems2(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    project = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    im_part_no = models.CharField(max_length=100)
    po_number = models.CharField(max_length=100)
    station_name = models.CharField(max_length=100)
    item_name  = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/%Y/%m/%d/',  blank=True, default = 'product_images/no_attach.png', null=True)
    mfr_part_no = models.CharField(max_length=100)
    dummy_part_no = models.CharField(max_length=100)
    mfr  = models.CharField(max_length=100)
    current_stock = models.CharField(max_length=100)
    uom  = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    total_value_wo_gst_usd = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    function = models.CharField(max_length=20)
    dri_name = models.CharField(max_length=100)
    life_cycle = models.CharField(max_length=100)
    def __str__(self):
        return  self.item_name
    @property
    def Total_cost(self):
        u = int(self.unit_price)
        c = int(self.current_stock)
        return round(float(u* c))
 

 
class RequestItem(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Staffs, on_delete=models.DO_NOTHING)
    date =  models.CharField(max_length=255)
    item_id = models.ForeignKey(StoreItems, on_delete=models.DO_NOTHING)
    req_qty = models.IntegerField(default=1)
    line = models.CharField(max_length=50)
    iw_oow = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    approved_date = models.CharField(max_length=100)
    approved_dri_name = models.CharField(max_length=100)
    machine_sl_no  = models.CharField(max_length=200, default= "NA")
    machine_name  = models.CharField(max_length=200, default = "NA")
    station  = models.CharField(max_length=200, default= "NA")
    remark = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    issued_status = models.CharField(max_length=100,default="")
    def __str__(self):
	    return self.item_id.item_name

class RequestItem2(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Staffs, on_delete=models.DO_NOTHING)
    date =  models.CharField(max_length=255)
    item_id = models.ForeignKey(StoreItems2, on_delete=models.DO_NOTHING)
    req_qty = models.IntegerField(default=1)
    line = models.CharField(max_length=50)
    iw_oow = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    approved_date = models.CharField(max_length=100)
    approved_dri_name = models.CharField(max_length=100)
    machine_sl_no  = models.CharField(max_length=200, default= "NA")
    machine_name  = models.CharField(max_length=200, default = "NA")
    station  = models.CharField(max_length=200, default= "NA")
    remark = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)
    issued_status = models.CharField(max_length=100,default="")
    def __str__(self):
	    return self.item_id.item_name

class IssueItem(models.Model):
    id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(RequestItem, on_delete=models.DO_NOTHING)
    #issuer_id = models.ForeignKey(ToolUser, on_delete=models.DO_NOTHING)
    issuer_name = models.CharField(max_length=255)
    issuer_mi_id = models.CharField(max_length=255)
    issue_qty = models.IntegerField()
    issue_time =  models.CharField(max_length=255)
    date =  models.CharField(max_length=255)
    total_cost = models.CharField(max_length=1000)
  
class IssueItem2(models.Model):
    id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(RequestItem2, on_delete=models.DO_NOTHING)
    issuer_name = models.CharField(max_length=255)
    issuer_mi_id = models.CharField(max_length=255)
    issue_qty = models.IntegerField()
    issue_time =  models.CharField(max_length=255)
    date =  models.CharField(max_length=255)
    @property
    def Total_Cost(self):
        return round(float(self.issue_qty) * float(self.request_id__item_id__unit_price),2)

class TranferItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_id1 = models.ForeignKey(StoreItems, on_delete=models.DO_NOTHING)
    item_id2 = models.ForeignKey(StoreItems2, on_delete=models.DO_NOTHING)
    tranfer_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    tranfer_quantity = models.IntegerField()
    tranfer_date = models.CharField(max_length=255)

class TranferItem2(models.Model):
    id = models.AutoField(primary_key=True)
    item_id1 = models.ForeignKey(StoreItems2, on_delete=models.DO_NOTHING)
    item_id2 = models.ForeignKey(StoreItems, on_delete=models.DO_NOTHING)
    tranfer_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    tranfer_quantity = models.IntegerField()
    tranfer_date = models.CharField(max_length=255)


class ReceiveItemp91(models.Model):
    id = models.AutoField(primary_key=True)
    receive_id = models.ForeignKey(StoreItems, on_delete=models.DO_NOTHING)
    receiver_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    receive_qty = models.CharField(max_length=255)
    receive_date = models.CharField(max_length=255)


class ReceiveItemP75(models.Model):
    id = models.AutoField(primary_key=True)
    receive_id = models.ForeignKey(StoreItems2, on_delete=models.DO_NOTHING)
    receiver_id = models.ForeignKey(AdminHOD, on_delete=models.DO_NOTHING)
    receive_qty = models.CharField(max_length=255)
    receive_date = models.CharField(max_length=255)


class DamagedItemP91(models.Model):
    id = models.AutoField(primary_key=True)
    #user_id = models.ForeignKey(ToolUser, on_delete=models.DO_NOTHING)
    user_dri_MI_ID =  models.CharField(max_length=255)
    user_dri_name =  models.CharField(max_length=255)
    issue_id = models.ForeignKey(IssueItem, on_delete=models.DO_NOTHING)
    reason = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    damaged_qty = models.IntegerField()

class DamagedItemP75(models.Model):
    id = models.AutoField(primary_key=True)
    #user_id = models.ForeignKey(ToolUser, on_delete=models.DO_NOTHING)
    user_dri_MI_ID =  models.CharField(max_length=255)
    user_dri_name =  models.CharField(max_length=255)
    issue_id = models.ForeignKey(IssueItem2, on_delete=models.DO_NOTHING)
    reason = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    damaged_qty = models.IntegerField()




@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 4 :
            ToolUser.objects.create(admin=instance)
       
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 4:
        instance.ToolUser.save()





