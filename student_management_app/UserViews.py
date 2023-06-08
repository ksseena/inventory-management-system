from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core import serializers
import json
from .import adminViews,ToolView

from tablib import Dataset

from django.conf import settings

from django.db.models import Q
from datetime import date, datetime

from student_management_app.models import CustomUser, Staffs, ToolUser, StoreItems, StoreItems2, RequestItem ,IssueItem,RequestItem2,IssueItem2
from .forms import  user_items_Form,remark_Form


def user_home(request):
    return render(request, "user_template/user_home_template.html")

def notification(request):
    approvel_pending_P91 = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91")).count()
    issue_pending_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91")).count()
    issue_done_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91")).count()
    reject_P91= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91")).count()
   
    approvel_pending_P75 = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75")).count()
    issue_pending_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75")).count()
    issue_done_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75")).count()
    reject_P75= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P91")).count()
    context={
        "approvel_pending_P91" : approvel_pending_P91,
        "issue_pending_P91" : issue_pending_P91,
        "issue_done_P91" : issue_done_P91,
        "reject_P91" : reject_P91,
        "approvel_pending_P75" : approvel_pending_P75,
        "issue_pending_P75" : issue_pending_P75,
        "issue_done_P75" : issue_done_P75,
        "reject_P75" : reject_P75
    }
    return render(request, "user_template/user_notification_template.html",context)



def user_approvel_pending_P91(request):
    user_summary = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)


def user_issue_pending_P91(request):
    user_summary= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_issued_done_P91(request):
    user_summary= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_reject_P91(request):
    user_summary= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_approvel_pending_P75(request):
    user_summary = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_issue_pending_P75(request):
    user_summary= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_issued_done_P75(request):
    user_summary= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)

def user_reject_P75(request):
    user_summary= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P75"))
    context = {
        "user_summary": user_summary,
    }
    return render(request, "user_template/user_summary.html", context)








def user_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)

    context={
        "user": user,
        "staff": staff
    }
    return render(request, 'user_template/user_profile.html', context)


def user_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('user_profile')
    else:
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            staff = Staffs.objects.get(admin=customuser.id)
            staff.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('user_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('user_profile')


def manage_user_data(request):
    user_obj = Staffs.objects.get(admin=request.user.id)
    user_data = RequestItem.objects.filter(user_id=user_obj)
    context = {
        "user_data":user_data
    }
    return render(request, 'user_template/manage_user_data.html',context)

def manage_user_data2(request):
    user_obj = Staffs.objects.get(admin=request.user.id)
    user_data = RequestItem2.objects.filter(user_id=user_obj)
    context = {
        "user_data":user_data
    }
    return render(request, 'user_template/manage_user_data2.html',context)

#user_obj = Staffs.objects.get(admin=request.user.id)
#user_data = Data.objects.filter(user_id=user_obj)

def request_item(request,item_id):
    store_item = get_object_or_404(StoreItems, pk=item_id)
    context = {
        "store_item": store_item
    }
    return render(request,'user_template/request_data.html', context)


def request_item_save(request,item_id):
    store_item = StoreItems.objects.get(pk=item_id)
    req_qty = request.POST.get("req_qty")
    line = request.POST.get("line")
    iw_oow = request.POST.get("iw_oow")
    machine_sl_no = request.POST.get("machine_sl_no")
    machine_name = request.POST.get("machine_name")
    station = request.POST.get("station")
    purpose = request.POST.get("purpose")
    user_obj = Staffs.objects.get(admin=request.user.id)
    request = RequestItem(purpose=purpose, station=station, machine_name=machine_name, machine_sl_no=machine_sl_no, user_id=user_obj,date=datetime.now(),item_id=store_item,req_qty=req_qty,line=line,iw_oow=iw_oow)
    request.save()
   
    return redirect('manage_user_data')


def request_item2(request,item_id):
    store_item = get_object_or_404(StoreItems2, pk=item_id)
    context = {
        "store_item": store_item
    }
    return render(request,'user_template/request_data2.html', context)


def request_item2_save(request,item_id):
    store_item = StoreItems2.objects.get(pk=item_id)
    #shift = request.POST.get("shift")
    req_qty = request.POST.get("req_qty")
    line = request.POST.get("line")
    iw_oow = request.POST.get("iw_oow")
    purpose = request.POST.get("purpose")
    user_obj = Staffs.objects.get(admin=request.user.id)
    request = RequestItem2(purpose=purpose, user_id=user_obj,date=datetime.now(),item_id=store_item,req_qty=req_qty,line=line,iw_oow=iw_oow)
    request.save()
   
    return redirect('manage_user_data2')



def add_user_data(request):
    form = user_items_Form()
    context = {
        "form": form
    }
    return render(request, 'user_template/add_user_data.html', context)       


def add_user_data_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_user_data')
    else:
        form = user_items_Form(request.POST, request.FILES)

        if form.is_valid():
            shift =form.cleaned_data['shift']
            item =form.cleaned_data['item']
            req_qty  = form.cleaned_data['req_qty']
            category = form.cleaned_data['category']
            line = form.cleaned_data['line']
            iw_oow = form.cleaned_data['iw_oow']
            user_obj = Staffs.objects.get(admin=request.user.id)
            item_obj = store_items.objects.get(id = item)
            try:
                add_user_data = Users(date=datetime.now(),user_id=user_obj,item=item_obj,shift=shift,user_mi_id=user_obj.admin.username,user_name=user_obj.admin.first_name,function=user_obj.function, req_qty=req_qty,category=category,line=line,iw_oow=iw_oow)
                add_user_data.save()
                messages.success(request, "Data Added Successfully!")
                return redirect('add_user_data')
            except:
                messages.error(request, "Failed to Add Data")
                return redirect('add_user_data')
        else:
            return redirect('add_user_data') 

def manage_store_data_user(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    store_data = StoreItems.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'user_template/manage_store_data.html',context)

def manage_store_data2_user(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    store_data = StoreItems2.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'user_template/manage_store_data2.html',context)
def manage_transaction_user(request):
    user_obj = Staffs.objects.get(admin=request.user.id)
    trasfer_data = IssueItem.objects.filter(request_id__user_id=user_obj)
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'user_template/manage_transaction_user.html',context)

def manage_transaction2_user(request):
    user_obj = Staffs.objects.get(admin=request.user.id)
    trasfer_data = IssueItem2.objects.filter(request_id__user_id=user_obj)
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'user_template/manage_transaction_user.html',context)