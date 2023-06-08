from django.db.models.expressions import F
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from datetime import datetime
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .forms import  Store_Items_Form,remark_Form,user_items_Form
from .resources import StoreResource1, StoreResource2
from django.conf import settings
from tablib import Dataset
from django.shortcuts import get_object_or_404

from student_management_app.models import AdminHOD, CustomUser, Staffs, ToolUser, StoreItems, StoreItems2, RequestItem, RequestItem2, IssueItem, IssueItem2, TranferItem, TranferItem2, ReceiveItemp91, ReceiveItemP75,DamagedItemP91,DamagedItemP75
import time
import datetime
from django.db.models import Q,F,FloatField
def admin_home(request):
    tool_users_count = ToolUser.objects.all().count()
    users_count = Staffs.objects.all().count()
    all_users = CustomUser.objects.all().count()
    total_master_datap91 = StoreItems.objects.all().count()
    total_master_datap75 = StoreItems2.objects.all().count()
    
    approvel_pending_P91 = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91")).count()
    issue_pending_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91")).count()
    issue_done_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91")).count()
    reject_P91= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91")).count()
   
    approvel_pending_P75 = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75")).count()
    issue_pending_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75")).count()
    issue_done_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75")).count()
    reject_P75= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P91")).count()
   
    context={
        "users_count": users_count,
        "all_users" :all_users,
        "tool_users_count" : tool_users_count,
        "total_master_datap91" : total_master_datap91,
        "total_master_datap75" : total_master_datap75,
        "approvel_pending_P91" : approvel_pending_P91,
        "issue_pending_P91" : issue_pending_P91,
        "issue_done_P91" : issue_done_P91,
        "reject_P91" : reject_P91,
        "approvel_pending_P75" : approvel_pending_P75,
        "issue_pending_P75" : issue_pending_P75,
        "issue_done_P75" : issue_done_P75,
        "reject_P75" : reject_P75
    }
    return render(request, "admin_template/home_content.html", context)



def approvel_pending_P91(request):
    approvel_pending_P91 = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91"))
    context = {
        "approvel_pending_P91": approvel_pending_P91,
    }
    return render(request, "admin_template/approvel_pending_P91.html", context)

def issue_pending_P91(request):
    issue_pending_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91"))
    context = {
        "issue_pending_P91": issue_pending_P91,
    }
    return render(request, "admin_template/issue_pending_P91.html", context)

def issued_done_P91(request):
    issue_done_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91"))
    context = {
        "issue_done_P91": issue_done_P91,
    }
    return render(request, "admin_template/issue_done_P91.html", context)

def reject_P91(request):
    reject_P91= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91"))
    context = {
        "reject_P91": reject_P91,
    }
    return render(request, "admin_template/reject_P91.html", context)

def approvel_pending_P75(request):
    approvel_pending_P75 = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75"))
    context = {
        "approvel_pending_P75": approvel_pending_P75,
    }
    return render(request, "admin_template/approvel_pending_P75.html", context)

def issue_pending_P75(request):
    issue_pending_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75"))
    context = {
        "issue_pending_P75": issue_pending_P75,
    }
    return render(request, "admin_template/issue_pending_P75.html", context)

def issued_done_P75(request):
    issue_done_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75"))
    context = {
        "issue_done_P75": issue_done_P75,
    }
    return render(request, "admin_template/issue_done_P75.html", context)

def reject_P75(request):
    reject_P75= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P75"))
    context = {
        "reject_P75": reject_P75,
    }
    return render(request, "admin_template/reject_P75.html", context)


def add_user(request):
    return render(request, "admin_template/add_user_template.html")


def add_user_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_user')
    else:
        first_name = request.POST.get('first_name')
        #last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        function = request.POST.get('function')

        try:
            user = CustomUser.objects.create_user(first_name=first_name,username=username, password=password, email=email, user_type=2)
            user.staffs.function = function
            user.save()
            messages.success(request, "User Added Successfully!")
            return redirect('add_user')
        except:
            messages.error(request, "Failed to Add User!")
            return redirect('add_user')



def manage_user(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "admin_template/manage_user_template.html", context)


def edit_user(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request,"admin_template/edit_user_template.html", context)


def edit_user_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            #user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            #staff_model.address = address
            staff_model.save()

            messages.success(request, "User Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update User")
            return redirect('/edit_staff/'+staff_id)




def delete_user(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "User Deleted Successfully.")
        return redirect('manage_user')
    except:
        messages.error(request, "Failed to Delete User.")
        return redirect('manage_user')


def add_toolroomuser(request):
    return render(request, "admin_template/add_toolroomuser_template.html")


def add_toolroomuser_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_ptsuser')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        #last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(first_name=first_name,username=username, password=password, email=email, user_type=4) 
            user.save()
            messages.success(request, "User Added Successfully!")
            return redirect('add_toolroomuser')
        except:
            messages.success(request, "User Added Successfully!")
            return redirect('add_toolroomuser')

def manage_toolroomuser(request):
    users = ToolUser.objects.all()
    context = {
        "users": users
    }
    return render(request, "admin_template/manage_toolroomuser_template.html", context)


def edit_toolroomuser(request, user_id):
    user = ToolUser.objects.get(admin=user_id)

    context = {
        "user": user,
        "id": user_id
    }
    return render(request, "admin_template/edit_toolroomuser_template.html", context)


def edit_toolroomuser_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        try:
            user = CustomUser.objects.get(id=user_id)
            user.first_name = first_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            user_model = ToolUser.objects.get(admin=user_id)

            user_model.save()

            messages.success(request, "User Updated Successfully.")
            return redirect('/edit_toolroomuser/'+user_id)

        except:
            messages.error(request, "Failed to Update User")
            return redirect('/edit_toolroomuser/'+user_id)

def delete_toolroomuser(request, user_id):
    user = ToolUser.objects.get(admin=user_id)
    try:
        user.delete()
        messages.success(request, "Buyer Deleted Successfully.")
        return redirect('manage_toolroomuser')
    except:
        messages.error(request, "Failed to Delete Buyer.")
        return redirect('manage_toolroomuser')



@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)



@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)




    


def staff_profile(request):
    pass


def student_profile(requtest):
    pass

def add_store_data(request):
    form = Store_Items_Form()
    context = {
        "form": form
    }
    return render(request, 'admin_template/create_store_items.html', context)       


def add_store_data_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_store_data')
    else:
        form = Store_Items_Form(request.POST, request.FILES)

        if form.is_valid():
           
            project = form.cleaned_data['project']
            category = form.cleaned_data['category']
            im_part_no =form.cleaned_data['im_part_no']
            po_number =form.cleaned_data['po_number']
            station_name  = form.cleaned_data['station_name']
            item_name = form.cleaned_data['item_name']
            spec = form.cleaned_data['spec']
            dummy_part_no = form.cleaned_data['dummy_part_no']
            mfr_part_no = form.cleaned_data['mfr_part_no']
            mfr = form.cleaned_data['mfr']
            current_stock = form.cleaned_data['current_stock']
            uom = form.cleaned_data['uom']
            unit_price = form.cleaned_data['unit_price']
            currency = form.cleaned_data['currency']
            total_value_wo_gst_usd = form.cleaned_data['total_value_wo_gst_usd']
            location = form.cleaned_data['location']
            vendor_name = form.cleaned_data['vendor_name']
            function = form.cleaned_data['function']
            life_cycle = form.cleaned_data['life_cycle']

            if len(request.FILES) != 0:
                product_image = request.FILES['product_image']
                fs1 = FileSystemStorage(location = settings.FS_IMAGE_UPLOADS, base_url= settings.FS_IMAGE_URL)
                filename1 = fs1.save(product_image.name, product_image)
                product_image_url = fs1.url(filename1)
            else:
                product_image_url = None


            user_obj = AdminHOD.objects.get(admin=request.user.id)
            try:
                add_store_data = StoreItems(dummy_part_no=dummy_part_no, function=function, life_cycle=life_cycle,admin_id=user_obj, project=project, category=category, im_part_no=im_part_no, po_number= po_number, station_name=station_name, item_name=item_name, spec= spec, mfr_part_no=mfr_part_no, mfr=mfr,current_stock=current_stock,uom=uom,unit_price=unit_price,currency=currency,total_value_wo_gst_usd=total_value_wo_gst_usd,location=location,vendor_name=vendor_name,product_image=product_image_url)
                add_store_data.save()
                messages.success(request, "Data Added Successfully!")
                return redirect('add_store_data')
            except:
                messages.error(request, "Failed to Add Data")
                return redirect('add_store_data')
        else:
            return redirect('add_store_data') 



def edit_store_data(request,id):
    # Adding DAta ID into Session Variable
    request.session['id'] = id

    data = StoreItems.objects.get(id=id)
    form = Store_Items_Form()
    # Filling the form with Data from Database
    form.fields['project'].initial = data.project
    form.fields['category'].initial = data.category
    form.fields['im_part_no'].initial = data.im_part_no
    form.fields['po_number'].initial = data.po_number
    form.fields['station_name'].initial = data.station_name
    form.fields['item_name'].initial = data.item_name
    form.fields['spec'].initial = data.spec
    form.fields['dummy_part_no'].initial = data.dummy_part_no
    form.fields['mfr_part_no'].initial = data.mfr_part_no
    form.fields['mfr'].initial = data.mfr
    form.fields['current_stock'].initial = data.current_stock
    form.fields['uom'].initial = data.uom
    form.fields['unit_price'].initial = data.unit_price
    form.fields['currency'].initial = data.currency
    form.fields['total_value_wo_gst_usd'].initial = data.total_value_wo_gst_usd
    form.fields['location'].initial = data.location
    form.fields['vendor_name'].initial = data.vendor_name
    form.fields['life_cycle'].initial = data.life_cycle
    form.fields['product_image'].initial = data.product_image
    context = {
        "id": id,
        "form": form
    }
    return render(request, "admin_template/edit_store_items_template.html", context)


def edit_store_data_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        id = request.session.get('id')
        if id == None:
            return redirect('admin_manage_store_data')

        form = Store_Items_Form(request.POST, request.FILES)
        if form.is_valid():
            project = form.cleaned_data['project']
            category = form.cleaned_data['category']
            im_part_no =form.cleaned_data['im_part_no']
            po_number =form.cleaned_data['po_number']
            station_name  = form.cleaned_data['station_name']
            item_name = form.cleaned_data['item_name']
            spec = form.cleaned_data['spec']
            mfr_part_no = form.cleaned_data['mfr_part_no']
            dummy_part_no = form.cleaned_data['dummy_part_no']
            mfr = form.cleaned_data['mfr']
            current_stock = form.cleaned_data['current_stock']
            uom = form.cleaned_data['uom']
            unit_price = form.cleaned_data['unit_price']
            currency = form.cleaned_data['currency']
            total_value_wo_gst_usd = form.cleaned_data['total_value_wo_gst_usd']
            location = form.cleaned_data['location']
            vendor_name = form.cleaned_data['vendor_name']
            life_cycle = form.cleaned_data['life_cycle']

            if len(request.FILES) != 0:
                product_image = request.FILES['product_image']
                fs1 = FileSystemStorage(location = settings.FS_IMAGE_UPLOADS, base_url= settings.FS_IMAGE_URL)
                filename1 = fs1.save(product_image.name, product_image)
                product_image_url = fs1.url(filename1)
            else:
                product_image_url = None


            
            try:
                # First Update into Custom User Model
                data = StoreItems.objects.get(id=id)
                data.project = project
                data.category = category
                data.im_part_no = im_part_no
                data.po_number = po_number
                data.station_name = station_name
                data.item_name = item_name
                data.spec = spec
                data.mfr_part_no = mfr_part_no
                data.dummy_part_no = dummy_part_no
                data.mfr = mfr
                data.current_stock = current_stock
                data.uom = uom
                data.unit_price = unit_price
                data.currency = currency
                data.total_value_wo_gst_usd = total_value_wo_gst_usd
                data.location = location
                data.vendor_name = vendor_name
                data.life_cycle = life_cycle
                if product_image_url != None:
                    data.product_image = product_image_url
                data.save()
                del request.session['id']
                messages.success(request, "Updated Successfully!")
                return redirect('admin_manage_store_data')
            except:
                messages.success(request, "Failed to Update")
                return redirect('admin_manage_store_data')
        else:
            return redirect('admin_manage_store_data')

def add_store_data2(request):
    form = Store_Items_Form()
    context = {
        "form": form
    }
    return render(request, 'admin_template/create_store_items2.html', context)       


def add_store_data2_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_store_data')
    else:
        form = Store_Items_Form(request.POST, request.FILES)

        if form.is_valid():
            project = form.cleaned_data['project']
            category = form.cleaned_data['category']
            im_part_no =form.cleaned_data['im_part_no']
            po_number =form.cleaned_data['po_number']
            station_name  = form.cleaned_data['station_name']
            item_name = form.cleaned_data['item_name']
            spec = form.cleaned_data['spec']
            mfr_part_no = form.cleaned_data['mfr_part_no']
            dummy_part_no = form.cleaned_data['dummy_part_no']
            mfr = form.cleaned_data['mfr']
            current_stock = form.cleaned_data['current_stock']
            uom = form.cleaned_data['uom']
            unit_price = form.cleaned_data['unit_price']
            currency = form.cleaned_data['currency']
            total_value_wo_gst_usd = form.cleaned_data['total_value_wo_gst_usd']
            location = form.cleaned_data['location']
            function = form.cleaned_data['function']
            vendor_name = form.cleaned_data['vendor_name']
            #dri_name = form.cleaned_data['dri_name']
            life_cycle = form.cleaned_data['life_cycle']

            if len(request.FILES) != 0:
                product_image = request.FILES['product_image']
                fs1 = FileSystemStorage(location = settings.FS_IMAGE_UPLOADS, base_url= settings.FS_IMAGE_URL)
                filename1 = fs1.save(product_image.name, product_image)
                product_image_url = fs1.url(filename1)
            else:
                product_image_url = None


            user_obj = AdminHOD.objects.get(admin=request.user.id)
            try:
                add_store_data = StoreItems2(dummy_part_no=dummy_part_no, function=function, life_cycle=life_cycle,admin_id=user_obj, project=project, category=category, im_part_no=im_part_no, po_number= po_number, station_name=station_name, item_name=item_name, spec= spec, mfr_part_no=mfr_part_no, mfr=mfr,current_stock=current_stock,uom=uom,unit_price=unit_price,currency=currency,total_value_wo_gst_usd=total_value_wo_gst_usd,location=location,vendor_name=vendor_name,product_image=product_image_url)
                add_store_data.save()
                messages.success(request, "Data Added Successfully!")
                return redirect('add_store_data2')
            except:
                messages.error(request, "Failed to Add Data")
                return redirect('add_store_data2')
        else:
            return redirect('add_store_data2') 

def edit_store_data2(request,id):
    # Adding DAta ID into Session Variable
    request.session['id'] = id

    data = StoreItems2.objects.get(id=id)
    form = Store_Items_Form()
    # Filling the form with Data from Database
    form.fields['project'].initial = data.project
    form.fields['category'].initial = data.category
    form.fields['im_part_no'].initial = data.im_part_no
    form.fields['po_number'].initial = data.po_number
    form.fields['station_name'].initial = data.station_name
    form.fields['item_name'].initial = data.item_name
    form.fields['spec'].initial = data.spec
    form.fields['dummy_part_no'].initial = data.dummy_part_no
    form.fields['mfr_part_no'].initial = data.mfr_part_no
    form.fields['mfr'].initial = data.mfr
    form.fields['current_stock'].initial = data.current_stock
    form.fields['uom'].initial = data.uom
    form.fields['unit_price'].initial = data.unit_price
    form.fields['currency'].initial = data.currency
    form.fields['total_value_wo_gst_usd'].initial = data.total_value_wo_gst_usd
    form.fields['location'].initial = data.location
    form.fields['vendor_name'].initial = data.vendor_name
    form.fields['life_cycle'].initial = data.life_cycle
    form.fields['product_image'].initial = data.product_image
    context = {
        "id": id,
        "form": form
    }
    return render(request, "admin_template/edit_store_items2_template.html", context)


def edit_store_data2_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        id = request.session.get('id')
        if id == None:
            return redirect('admin_manage_store_data2')

        form = Store_Items_Form(request.POST, request.FILES)
        if form.is_valid():
            project = form.cleaned_data['project']
            category = form.cleaned_data['category']
            im_part_no =form.cleaned_data['im_part_no']
            po_number =form.cleaned_data['po_number']
            station_name  = form.cleaned_data['station_name']
            item_name = form.cleaned_data['item_name']
            spec = form.cleaned_data['spec']
            mfr_part_no = form.cleaned_data['mfr_part_no']
            dummy_part_no = form.cleaned_data['dummy_part_no']
            mfr = form.cleaned_data['mfr']
            current_stock = form.cleaned_data['current_stock']
            uom = form.cleaned_data['uom']
            unit_price = form.cleaned_data['unit_price']
            currency = form.cleaned_data['currency']
            total_value_wo_gst_usd = form.cleaned_data['total_value_wo_gst_usd']
            location = form.cleaned_data['location']
            vendor_name = form.cleaned_data['vendor_name']
            life_cycle = form.cleaned_data['life_cycle']

            if len(request.FILES) != 0:
                product_image = request.FILES['product_image']
                fs1 = FileSystemStorage(location = settings.FS_IMAGE_UPLOADS, base_url= settings.FS_IMAGE_URL)
                filename1 = fs1.save(product_image.name, product_image)
                product_image_url = fs1.url(filename1)
            else:
                product_image_url = None


            
            try:
                # First Update into Custom User Model
                data = StoreItems2.objects.get(id=id)
                data.project = project
                data.category = category
                data.im_part_no = im_part_no
                data.po_number = po_number
                data.station_name = station_name
                data.item_name = item_name
                data.spec = spec
                data.mfr_part_no = mfr_part_no
                data.dummy_part_no = dummy_part_no
                data.mfr = mfr
                data.current_stock = current_stock
                data.uom = uom
                data.unit_price = unit_price
                data.currency = currency
                data.total_value_wo_gst_usd = total_value_wo_gst_usd
                data.location = location
                data.vendor_name = vendor_name
                data.life_cycle = life_cycle
                if product_image_url != None:
                    data.product_image = product_image_url
                data.save()
                del request.session['id']
                messages.success(request, "Updated Successfully!")
                return redirect('admin_manage_store_data2')
            except:
                messages.success(request, "Failed to Update")
                return redirect('admin_manage_store_data2')
        else:
            return redirect('admin_manage_store_data2')

def admin_manage_store_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    store_data = StoreItems.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'admin_template/manage_store_data.html',context)


def admin_manage_store_data2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    store_data = StoreItems2.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'admin_template/manage_store_data2.html',context)



def import_data1(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        store_resource1 = StoreResource1()
        dataset = Dataset()
        new_items = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_items.read().decode('ISO-8859-1'),format='csv')
            result = store_resource1.import_data(dataset, dry_run=True)
            messages.success(request, "Uploaded Successfully!")
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_items.read().decode('utf-8'),format='json')
            result = store_resource1.import_data(dataset, dry_run=True)
        else :
            pass
    
        if not result.has_errors():
            store_resource1.import_data(dataset, dry_run=False)
        
        return redirect('admin_manage_store_data')

    return render(request, 'admin_template/import.html')    



def import_data2(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        store_resource2 = StoreResource2()
        dataset = Dataset()
        new_items = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_items.read().decode('ISO-8859-1'),format='csv')
            result = store_resource2.import_data(dataset, dry_run=True)
            messages.success(request, "Uploaded Successfully!")
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_items.read().decode('utf-8'),format='json')
            result = store_resource2.import_data(dataset, dry_run=True)
        else :
            pass
    
        if not result.has_errors():
            store_resource2.import_data(dataset, dry_run=False)
        
        return redirect('admin_manage_store_data2')

    return render(request, 'admin_template/import.html')    


def receivep91(request,receive_id):
    receive_item=get_object_or_404(StoreItems,pk=receive_id)
    context ={
        "receive_item" : receive_item
    }
    return render(request, 'admin_template/receivep91.html', context)
 
def receive_save_p91(request,receive_id):
    receive_item=StoreItems.objects.get(pk=receive_id)
    receive_qty=request.POST.get("receive_qty")
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    receive = ReceiveItemp91(receiver_id=user_obj, receive_id=receive_item,receive_qty=receive_qty,receive_date=datetime.datetime.now())
    receive.save()
    storeitem = StoreItems.objects.get(pk=receive_id)
    storeitem.current_stock = int(storeitem.current_stock) + int(receive_qty)
    storeitem.save()
    return redirect('admin_manage_store_data')


def receiveP75(request,receive_id):
    receive_item=get_object_or_404(StoreItems2,pk=receive_id)
    context ={
        "receive_item" : receive_item
    }
    return render(request, 'admin_template/receivep75.html', context)
 
def receive_save_P75(request,receive_id):
    receive_item=StoreItems2.objects.get(pk=receive_id)
    receive_qty=request.POST.get("receive_qty")
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    receive = ReceiveItemP75(receiver_id=user_obj, receive_id=receive_item,receive_qty=receive_qty,receive_date=datetime.datetime.now())
    receive.save()
    storeitem = StoreItems2.objects.get(pk=receive_id)
    storeitem.current_stock = int(storeitem.current_stock) + int(receive_qty)
    storeitem.save()
    return redirect('admin_manage_store_data2')
 

def admin_manage_user_requests(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    user_data = RequestItem.objects.all()
    context = {
        "user_data":user_data
    }
    return render(request, 'admin_template/manage_user_request.html',context)


def admin_manage_user_requests2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    user_data = RequestItem2.objects.all()
    context = {
        "user_data":user_data
    }
    return render(request, 'admin_template/manage_user_request2.html',context)




def admin_remark_data(request, data_id):
    # Adding DAta ID into Session Variable
    request.session['data_id'] = data_id
    data = RequestItem.objects.get(id=data_id)
    form = remark_Form()
    # Filling the form with Data from Database
    form.fields['remark'].initial = data.remark
    
    context = {
        "id": data_id,
        "form": form
    }
    return render(request, "admin_template/remark_data_template.html", context)


def admin_remark_data_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        data_id = request.session.get('data_id')
        if data_id == None:
            return redirect('/admin_manage_user_requests')

        form = remark_Form(request.POST, request.FILES)
        if form.is_valid():
            remark = form.cleaned_data['remark']
            
            try:
                # First Update into Custom User Model
                data = RequestItem.objects.get(id=data_id)
                data.remark = remark
                
                data.save()

                del request.session['data_id']

                messages.success(request, "Updated Successfully!")
                return redirect('admin_manage_user_requests')
            except:
                messages.success(request, "Failed to Update")
                return redirect('admin_manage_user_requests')
        else:
            return redirect('admin_manage_user_requests')

def admin_remark_data2(request, data_id):
    # Adding DAta ID into Session Variable
    request.session['data_id'] = data_id
    data = RequestItem2.objects.get(id=data_id)
    form = remark_Form()
    # Filling the form with Data from Database
    form.fields['remark'].initial = data.remark
    
    context = {
        "id": data_id,
        "form": form
    }
    return render(request, "admin_template/remark_data2_template.html", context)


def admin_remark_data2_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        data_id = request.session.get('data_id')
        if data_id == None:
            return redirect('/admin_manage_user_requests2')

        form = remark_Form(request.POST, request.FILES)
        if form.is_valid():
            remark = form.cleaned_data['remark']
            
            try:
                # First Update into Custom User Model
                data = RequestItem2.objects.get(id=data_id)
                data.remark = remark
                
                data.save()

                del request.session['data_id']

                messages.success(request, "Updated Successfully!")
                return redirect('admin_manage_user_requests2')
            except:
                messages.success(request, "Failed to Update")
                return redirect('admin_manage_user_requests2')
        else:
            return redirect('admin_manage_user_requests2')








def admin_manage_issueitems2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    trasfer_data = IssueItem2.objects.all()
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'admin_template/manage_issueitems2.html',context)

def admin_manage_issueitems1(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    trasfer_data = IssueItem.objects.all()
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'admin_template/manage_issueitems1.html',context)

def admin_manage_receive_P91_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    receive_data = ReceiveItemp91.objects.all()
    context = {
        "receive_data":receive_data
    }
    return render(request, 'admin_template/manage_receivep91.html',context)

def admin_manage_receive_P75_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    receive_data = ReceiveItemP75.objects.all()
    context = {
        "receive_data":receive_data
    }
    return render(request, 'admin_template/manage_receivep75.html',context)

def admin_user_request_approve(request, data_id):
    data = RequestItem.objects.get(pk=data_id)
    data.status = "Approved"
    data.approved_date = datetime.datetime.now()
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('approvel_pending_P91')

def admin_user_request_reject(request,data_id):
    data = RequestItem.objects.get(pk=data_id)
    data.status = "Rejected"
    data.approved_date =datetime.datetime.now()
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('admin_manage_user_requests')

def admin_user_request2_approve(request, data_id):
    data = RequestItem2.objects.get(pk=data_id)
    data.status = "Approved"
    data.approved_date = datetime.datetime.now()
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('approvel_pending_P75')



def admin_user_request2_reject(request,data_id):
    data = RequestItem2.objects.get(pk=data_id)
    data.status = "Rejected"
    data.approved_date = datetime.datetime.now()
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('admin_manage_user_requests2')


def Tranfer_item(request,trans_id):
    transitem=get_object_or_404(StoreItems,pk=trans_id)

    storeitems = StoreItems2.objects.filter(im_part_no=transitem.im_part_no)
    context ={
        "transitem" : transitem,
        "storeitems" : storeitems,
    }
    return render(request, 'admin_template/Tranfer_internal.html', context)


def Tranfer_Item_Save(request,trans_id):
    transitem = StoreItems.objects.get(pk=trans_id)
    tranfer_quantity = request.POST.get("tranfer_quantity")

    store_id = request.POST.get('storeitem')
    storeitem = StoreItems2.objects.get(id=store_id)
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    tranfer = TranferItem(tranfer_id=user_obj, item_id1=transitem,item_id2=storeitem,tranfer_quantity=tranfer_quantity,tranfer_date=datetime.datetime.now())
    tranfer.save() 
    transitem.current_stock = int(transitem.current_stock) - int(tranfer_quantity)
    transitem.save()
    storeitem.current_stock = int(storeitem.current_stock) + int(tranfer_quantity)
    storeitem.save()
    return redirect('admin_manage_store_data')
    

def Tranfer_item2(request,trans_id):
    transitem=get_object_or_404(StoreItems2,pk=trans_id)
    storeitems = StoreItems.objects.filter(im_part_no=transitem.im_part_no)
    context ={
        "transitem" : transitem,
        "storeitems" : storeitems,
    }
    return render(request, 'admin_template/Tranfer2_internal.html', context)


def Tranfer_Item2_Save(request,trans_id):
    transitem = StoreItems2.objects.get(pk=trans_id)
    tranfer_quantity = request.POST.get("tranfer_quantity")

    store_id = request.POST.get('storeitem')
    storeitem = StoreItems.objects.get(id=store_id)
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    tranfer = TranferItem2(tranfer_id=user_obj, item_id1=transitem,item_id2=storeitem,tranfer_quantity=tranfer_quantity,tranfer_date=datetime.datetime.now())
    tranfer.save() 
    transitem.current_stock = int(transitem.current_stock) - int(tranfer_quantity)
    transitem.save()
    storeitem.current_stock = int(storeitem.current_stock) + int(tranfer_quantity)
    storeitem.save()
    return redirect('admin_manage_store_data2')


def admin_manage_tranfer_item_P91toP75(request):
    tranfer_data = TranferItem.objects.all()
    context = {
        "tranfer_data" : tranfer_data
    }
    return render(request, 'admin_template/manage_tranfer_item_P91toP75.html',context)


def admin_manage_tranfer_item_P75toP91(request):
    tranfer_data = TranferItem2.objects.all()
    context = {
        "tranfer_data" : tranfer_data
    }
    return render(request, 'admin_template/manage_tranfer_item_P75toP91.html',context)

def admin_details(request,request_id):
    useritem=get_object_or_404(RequestItem,pk=request_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'admin_template/details.html', context)

def admin_transferitm(request,request_id):
    useritem=RequestItem.objects.get(pk=request_id)
    issue_qty=request.POST.get("issue_qty")
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
  
    user_obj = AdminHOD.objects.get(admin=request.user.id)

    issue = IssueItem(request_id=useritem,issue_qty=issue_qty,issuer_name=user_obj.admin.first_name,issuer_mi_id=user_obj.admin.username, date=datetime.date.today(),issue_time=curr_clock)
    issue.save()   
    useritem.issued_status = "Issued"
    useritem.save()
    storeitem = StoreItems.objects.get(pk=useritem.item_id_id)
    storeitem.current_stock = int(storeitem.current_stock) - int(issue_qty)
    storeitem.save()
    return redirect('issue_pending_P91')



def admin_details2(request,request_id):
    useritem=get_object_or_404(RequestItem2,pk=request_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'admin_template/details2.html', context)

def admin_transferitm2(request,request_id):
    useritem=RequestItem2.objects.get(pk=request_id)
    issue_qty=request.POST.get("issue_qty")
    
    
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
  
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    issue = IssueItem2(request_id=useritem,issue_qty=issue_qty,issuer_name=user_obj.admin.first_name,issuer_mi_id=user_obj.admin.username, date=datetime.date.today(),issue_time=curr_clock)
    issue.save()   
    useritem.issued_status = "Issued"
    useritem.save()
    storeitem = StoreItems2.objects.get(pk=useritem.item_id_id)
    storeitem.current_stock = int(storeitem.current_stock) - int(issue_qty)
    storeitem.save()
    return redirect('issue_pending_P75')

def admin_damage1(request,issue_id):
    useritem=get_object_or_404(IssueItem,pk=issue_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'admin_template/damage1.html', context)

def admin_damageitem1(request,issue_id):
    useritem=IssueItem.objects.get(pk=issue_id)
    damaged_qty=request.POST.get("damaged_qty")
    reason = request.POST.get("reason")
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    damage = DamagedItemP91(reason=reason, issue_id=useritem,user_dri_MI_ID= user_obj.admin.username, user_dri_name=user_obj.admin.first_name, damaged_qty=damaged_qty,date=datetime.datetime.now())
    damage.save()   
    useritem.issue_qty = int(useritem.issue_qty) - int(damaged_qty)
    useritem.save()
    return redirect('admin_manage_issueitems1')

def admin_manage_damage_P91_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    damage_data = DamagedItemP91.objects.all()
    context = {
        "damage_data":damage_data
    }
    return render(request, 'admin_template/manage_damageP91.html',context)

def admin_damage2(request,issue_id):
    useritem=get_object_or_404(IssueItem2,pk=issue_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'admin_template/damage2.html', context)

def admin_damageitem2(request,issue_id):
    useritem=IssueItem2.objects.get(pk=issue_id)
    damaged_qty=request.POST.get("damaged_qty")
    reason = request.POST.get("reason")
    user_obj = AdminHOD.objects.get(admin=request.user.id)
    damage = DamagedItemP75(reason=reason, issue_id=useritem,user_dri_MI_ID= user_obj.admin.username, user_dri_name=user_obj.admin.first_name,damaged_qty=damaged_qty,date=datetime.datetime.now())
    damage.save()   
    useritem.issue_qty = int(useritem.issue_qty) - int(damaged_qty)
    useritem.save()
    return redirect('admin_manage_issueitems2')

def admin_manage_damage_P75_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    damage_data = DamagedItemP75.objects.all()
    context = {
        "damage_data":damage_data
    }
    return render(request, 'admin_template/manage_damageP75.html',context)

import datetime
def admin_daterange_report(request):
    return render(request, "admin_template/admin_daterange_report.html")

def all_report(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
        # Parsing the date data into Python object
    start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    issue_report = IssueItem2.objects.filter(date__range=(start_date_parse, end_date_parse))
    context = {
        "issue_report" : issue_report,
    }
    return render(request, "admin_template/issue_report_data_template.html", context) 


def admin_daterange_report1(request):
    return render(request, "admin_template/admin_daterange_report1.html")

def all_report1(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
        # Parsing the date data into Python object
    start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    issue_report = IssueItem.objects.filter(date__range=(start_date_parse, end_date_parse))  
    context = {
        "issue_report" : issue_report,
    }
    return render(request, "admin_template/issue_report_data_template1.html", context) 

from django.db.models import Count,Sum

def admin_manage_issueitems1_summary(request):
    trasfer_data_summary = IssueItem.objects.values('request_id__item_id__item_name', 'date', 'request_id__item_id__category', 'request_id__line').annotate(count=Sum('issue_qty'),total_cost=Sum( F('issue_qty') * F('request_id__item_id__unit_price'),output_field=FloatField())).order_by('-date').distinct()
    #.values('exchange_rate','amount').aggregate(Sum(F('amount') * F('exchange_rate')))
    context = {
        "trasfer_data_summary":trasfer_data_summary,
    }
    return render(request, 'admin_template/trasfer_data_summary.html',context)


def admin_issue_daterange_summary1(request):
    return render(request, "admin_template/admin_issue_daterange_summary1.html")

def all_issue_summary1(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
        # Parsing the date data into Python object
    start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    #issue_report = IssueItem.objects.filter(date__range=(start_date_parse, end_date_parse))
    #trasfer_data_summary = IssueItem.objects.values('request_id__item_id__item_name', 'date').annotate(count=Sum('issue_qty')).order_by('-date').distinct()
    
    issue_report = IssueItem.objects.values('request_id__item_id__item_name', 'date', 'request_id__item_id__category', 'request_id__line').filter(date__range=(start_date_parse, end_date_parse)).annotate(count=Sum('issue_qty'),total_cost=Sum( F('issue_qty') * F('request_id__item_id__unit_price'),output_field=FloatField())).order_by('-date').distinct()
    
    context = {
        "issue_report" : issue_report,
    }
    return render(request, "admin_template/all_issue_summary1.html", context) 

def admin_manage_issueitems1_summaryP75(request):
    trasfer_data_summary = IssueItem2.objects.values('request_id__item_id__item_name', 'date', 'request_id__line', 'request_id__item_id__category').annotate(count=Sum('issue_qty'),total_cost=Sum(F('issue_qty') * F('request_id__item_id__unit_price'),output_field=FloatField())).order_by('-date').distinct()
    context = {
        "trasfer_data_summary":trasfer_data_summary,
    }
    return render(request, 'admin_template/trasfer_data_summary.html',context)

def admin_issue_daterange_summaryP75(request):
    return render(request, "admin_template/admin_issue_daterange_summaryP75.html")

def all_issue_summaryP75(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
        # Parsing the date data into Python object
    start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    #issue_report = IssueItem.objects.filter(date__range=(start_date_parse, end_date_parse))
    #trasfer_data_summary = IssueItem.objects.values('request_id__item_id__item_name', 'date').annotate(count=Sum('issue_qty')).order_by('-date').distinct()
    
    issue_report = IssueItem2.objects.values('request_id__item_id__item_name', 'date', 'request_id__line', 'request_id__item_id__category').filter(date__range=(start_date_parse, end_date_parse)).annotate(count=Sum('issue_qty'),total_cost=Sum(F('issue_qty') * F('request_id__item_id__unit_price'),output_field=FloatField())).order_by('-date').distinct()
    
    context = {
        "issue_report" : issue_report,
    }
    return render(request, "admin_template/all_issue_summary1.html", context) 



def delete_StoreItems(request, delete_store):
    dlt1 = StoreItems.objects.get(id=delete_store)
    if request.method == "POST":
        dlt1.delete()
        messages.add_message(request, messages.INFO, f"{dlt1.id} Item Deleted")
        return redirect('admin_manage_store_data')
    context = {
        'dlt1': dlt1
    }
    return render(request, 'admin_template/StoreItems_delete.html', context)

def delete_StoreItems2(request, delete_store):
    dlt1 = StoreItems2.objects.get(id=delete_store)
    if request.method == "POST":
        dlt1.delete()
        messages.add_message(request, messages.INFO, f"{dlt1.id} Item Deleted")
        return redirect('admin_manage_store_data2')
    context = {
        'dlt1': dlt1
    }
    return render(request, 'admin_template/StoreItems_delete.html', context)


def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    admin = AdminHOD.objects.get(admin=user)

    context={
        "user": user,
        "admin": admin
    }
    return render(request, 'admin_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            tool = AdminHOD.objects.get(admin=customuser.id)
            tool.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')



def final_admin_manage_issueitems1_summaryP91(request):
    final_trasfer_data_summary = IssueItem.objects.values( 'date', 'request_id__line', 'request_id__item_id__category').annotate(count=Sum('issue_qty'),total_cost=Sum(F('issue_qty') * F('request_id__item_id__unit_price'),category=('request_id__item_id__category'),output_field=FloatField())).order_by('-date').distinct()
    context = {
        "final_trasfer_data_summary":final_trasfer_data_summary,
    }
    return render(request, 'admin_template/final_trasfer_data_summary.html',context)