from typing import ItemsView
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import get_object_or_404
import json
from .import adminViews, UserViews
from django.db.models import Count,Sum

from django.conf import settings

from django.db.models import Q

from tablib import Dataset
from .forms import  Store_Items_Form,remark_Form,user_items_Form
from .resources import StoreResource1, StoreResource2

from student_management_app.models import CustomUser, Staffs,ToolUser,StoreItems,RequestItem, RequestItem2, IssueItem, IssueItem2, StoreItems2, TranferItem, TranferItem2 , ReceiveItemp91, ReceiveItemP75, DamagedItemP91, DamagedItemP75
#from .forms import AddStudentForm, EditStudentForm
from django.contrib.auth.decorators import login_required
import time
    
def add_notifications(request):
    approvel_pending_P91 = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91")).count()
    issue_pending_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91")).count()
    issue_done_P91= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91")).count()
    reject_P91= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91")).count()
   
    approvel_pending_P75 = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75")).count()
    issue_pending_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75")).count()
    issue_done_P75= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75")).count()
    reject_P75= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P75")).count()
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
    return render(request, "tool_template/notifications.html", context)




def tool_approvel_pending_P91(request):
    tool_summary = RequestItem.objects.filter(Q(status="") & Q(item_id__project="P91"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)


def tool_issue_pending_P91(request):
    tool_summary= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P91"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_issued_done_P91(request):
    tool_summary= RequestItem.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P91"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_reject_P91(request):
    tool_summary= RequestItem.objects.filter(Q(status="Rejected") & Q(item_id__project="P91"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_approvel_pending_P75(request):
    tool_summary = RequestItem2.objects.filter(Q(status="") & Q(item_id__project="P75"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_issue_pending_P75(request):
    tool_summary= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="") & Q(item_id__project="P75"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_issued_done_P75(request):
    tool_summary= RequestItem2.objects.filter(Q(status="Approved") & Q(issued_status="Issued") & Q(item_id__project="P75"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)

def tool_reject_P75(request):
    tool_summary= RequestItem2.objects.filter(Q(status="Rejected") & Q(item_id__project="P75"))
    context = {
        "tool_summary": tool_summary,
    }
    return render(request, "tool_template/tool_summary.html", context)






def manage_store_data(request):
    store_data = StoreItems.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'tool_template/manage_store_data.html',context)


def manage_store_data2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    store_data = StoreItems2.objects.all()
    context = {
        "store_data":store_data
    }
    return render(request, 'tool_template/manage_store_data2.html',context)


def manage_user_requests(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    user_data = RequestItem.objects.all()
    context = {
        "user_data":user_data
    }
    return render(request, 'tool_template/manage_user_request.html',context)


def manage_user_requests2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    user_data = RequestItem2.objects.all()
    context = {
        "user_data":user_data
    }
    return render(request, 'tool_template/manage_user_request2.html',context)



def manage_issueitems2(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    trasfer_data = IssueItem2.objects.all()
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'tool_template/manage_issueitems2.html',context)

def manage_transaction(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    trasfer_data = IssueItem.objects.all()
    context = {
        "trasfer_data":trasfer_data
    }
    return render(request, 'tool_template/manage_transaction.html',context)


def remark_data(request, data_id):
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
    return render(request, "tool_template/remark_data_template.html", context)


def remark_data_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        data_id = request.session.get('data_id')
        if data_id == None:
            return redirect('/manage_user_requests')

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
                return redirect('manage_user_requests')
            except:
                messages.success(request, "Failed to Update")
                return redirect('manage_user_requests')
        else:
            return redirect('manage_user_requests')

def remark_data2(request, data_id):
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
    return render(request, "tool_template/remark_data2_template.html", context)


def remark_data2_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        data_id = request.session.get('data_id')
        if data_id == None:
            return redirect('/manage_user_requests2')

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
                return redirect('manage_user_requests2')
            except:
                messages.success(request, "Failed to Update")
                return redirect('manage_user_requests2')
        else:
            return redirect('manage_user_requests2')


def user_request_approve(request, data_id):
    data = RequestItem.objects.get(pk=data_id)
    data.status = "Approved"
    data.approved_date = datetime.now()
    user_obj = ToolUser.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('tool_approvel_pending_P91')

def user_request_reject(request,data_id):
    data = RequestItem.objects.get(pk=data_id)
    data.status = "Rejected"
    data.approved_date = datetime.now()
    user_obj = ToolUser.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('tool_reject_P91')

def user_request2_approve(request, data_id):
    data = RequestItem2.objects.get(pk=data_id)
    data.status = "Approved"
    data.approved_date = datetime.now()
    user_obj = ToolUser.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('tool_approvel_pending_P75')

def user_request2_reject(request,data_id):
    data = RequestItem2.objects.get(pk=data_id)
    data.status = "Rejected"
    data.approved_date = datetime.now()
    user_obj = ToolUser.objects.get(admin=request.user.id)
    data.approved_dri_name = user_obj.admin.first_name
    data.save()
    return redirect('tool_reject_P75')

def details1(request,request_id):
    useritem=get_object_or_404(RequestItem,pk=request_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'tool_template/details.html', context)

def transferitm1(request,request_id):
    useritem=RequestItem.objects.get(pk=request_id)
    issue_qty=request.POST.get("issue_qty")
    date = request.POST.get("date")
    
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
  
    user_obj = ToolUser.objects.get(admin=request.user.id)
    issue = IssueItem(request_id=useritem, issuer_name=user_obj.admin.first_name,issuer_mi_id=user_obj.admin.username,issue_qty=issue_qty,date=date,issue_time=curr_clock)
    issue.save()   
    useritem.issued_status = "Issued"
    useritem.save()
    storeitem = StoreItems.objects.get(pk=useritem.item_id_id)
    storeitem.current_stock = int(storeitem.current_stock) - int(issue_qty)
    storeitem.save()
    return redirect('tool_issue_pending_P91')



def details2(request,request_id):
    useritem=get_object_or_404(RequestItem2,pk=request_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'tool_template/details2.html', context)

def transferitm2(request,request_id):
    useritem=RequestItem2.objects.get(pk=request_id)
    issue_qty=request.POST.get("issue_qty")
    date = request.POST.get("date")
    
    
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
  
    user_obj = ToolUser.objects.get(admin=request.user.id)
    issue = IssueItem2(request_id=useritem,issuer_name=user_obj.admin.first_name,issuer_mi_id=user_obj.admin.username,issue_qty=issue_qty,date=date,issue_time=curr_clock)
    issue.save()   
    useritem.issued_status = "Issued"
    useritem.save()
    storeitem = StoreItems2.objects.get(pk=useritem.item_id_id)
    storeitem.current_stock = int(storeitem.current_stock) - int(issue_qty)
    storeitem.save()
    return redirect('tool_issue_pending_P75')
  




def manage_tranfer_item_P91toP75(request):
    tranfer_data = TranferItem.objects.all()
    context = {
        "tranfer_data" : tranfer_data
    }
    return render(request, 'tool_template/manage_trafer_item_P91toP75.html',context)


def manage_tranfer_item_P75toP91(request):
    tranfer_data = TranferItem2.objects.all()
    context = {
        "tranfer_data" : tranfer_data
    }
    return render(request, 'tool_template/manage_trafer_item_P75toP91.html',context)


 
def manage_receive_p91_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    receive_data = ReceiveItemp91.objects.all()
    context = {
        "receive_data":receive_data
    }
    return render(request, 'tool_template/manage_receivep91.html',context)


def manage_receive_P75_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    receive_data = ReceiveItemP75.objects.all()
    context = {
        "receive_data":receive_data
    }
    return render(request, 'tool_template/manage_receivep75.html',context)

def damage1(request,issue_id):
    useritem=get_object_or_404(IssueItem,pk=issue_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'tool_template/damage1.html', context)

def damageitem1(request,issue_id):
    useritem=IssueItem.objects.get(pk=issue_id)
    damaged_qty=request.POST.get("damaged_qty")
    reason = request.POST.get("reason")
    user_obj = ToolUser.objects.get(admin=request.user.id)
    damage = DamagedItemP91(reason=reason, issue_id=useritem,user_dri_MI_ID= user_obj.admin.username, user_dri_name=user_obj.admin.first_name, damaged_qty=damaged_qty,date=datetime.now())
    damage.save()   
    useritem.issue_qty = int(useritem.issue_qty) - int(damaged_qty)
    useritem.save()
    return redirect('manage_transaction')

def manage_damage_P91_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    damage_data = DamagedItemP91.objects.all()
    context = {
        "damage_data":damage_data
    }
    return render(request, 'tool_template/manage_damageP91.html',context)

def damage2(request,issue_id):
    useritem=get_object_or_404(IssueItem2,pk=issue_id)
    context ={
        "useritem" : useritem
    }
    return render(request, 'tool_template/damage2.html', context)

def damageitem2(request,issue_id):
    useritem=IssueItem2.objects.get(pk=issue_id)
    damaged_qty=request.POST.get("damaged_qty")
    reason = request.POST.get("reason")
    user_obj = ToolUser.objects.get(admin=request.user.id)
    damage = DamagedItemP75(reason=reason, issue_id=useritem,user_dri_MI_ID= user_obj.admin.username, user_dri_name=user_obj.admin.first_name,damaged_qty=damaged_qty,date=datetime.now())
    damage.save()   
    useritem.issue_qty = int(useritem.issue_qty) - int(damaged_qty)
    useritem.save()
    return redirect('manage_issueitems2')

def manage_damage_P75_data(request):
    #user_obj = PTSUser.objects.get(admin=request.user.id)
    damage_data = DamagedItemP75.objects.all()
    context = {
        "damage_data":damage_data
    }
    return render(request, 'tool_template/manage_damageP75.html',context)


def summa(request):
    repeatednames = StoreItems.objects.annotate(total_sum=Sum('RequestItem__item_id__issue_qty'))
    context = {
        "repeatednames":repeatednames
    }
    return render(request, 'tool_template/summary_consolidated_report.html',context)


def tool_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    tool = ToolUser.objects.get(admin=user)

    context={
        "user": user,
        "tool": tool
    }
    return render(request, 'tool_template/tool_profile.html', context)


def tool_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('tool_profile')
    else:
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            tool = ToolUser.objects.get(admin=customuser.id)
            tool.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('tool_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('tool_profile')