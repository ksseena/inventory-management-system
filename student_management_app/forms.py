from django import forms 
from django.forms import Form

from student_management_app.models import CustomUser, Staffs, ToolUser, StoreItems,RequestItem #


class DateInput(forms.DateInput):
    input_type = "date"



class DateInput(forms.DateInput):
    input_type = "date"



Department_CHOICES =(
    ("AE", "AE"),
    ("AFTE", "AFTE"),
    ("PME", "PME"),
    ("RE", "RE"),
    ("RF", "RF"),
    ("TOOL ROOM", "TOOL ROOM"),  
    ("Common", "Common"),
    ("NA", "NA"),
)
Category_CHOICES =(
    ("W-BUY_SPARE", "W-BUY_SPARE"),
    ("W-BUY_CONSUMABLES", "W-BUY_CONSUMABLES"),
    ("A-BUY_SPARE", "A-BUY_SPARE"),
    ("A-BUY_CONSUMABLES", "A-BUY_CONSUMABLES"),
)

Project_CHOICES =(
    
    ("NA", "NA"),
    ("P91", "P91"),
    ("P75", "P75"),
)



Currency_CHOICES =(
    ("INR", "INR"),
    ("USD", "USD"),
)


class Store_Items_Form(forms.Form):
    project = forms.ChoiceField(label="Project", choices=Project_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    category = forms.ChoiceField(label="Category", choices=Category_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    po_number = forms.CharField(label="PO Number", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    im_part_no = forms.CharField(label="IM Part No", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    function = forms.ChoiceField(label="Function Name", choices=Department_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    station_name = forms.CharField(label="Station Name", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    item_name=forms.CharField(label="Item", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    spec=forms.CharField(label="Specification", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    mfr_part_no=forms.CharField(label="MFR Part No", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    dummy_part_no=forms.CharField(label="Dummy Part No", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    mfr=forms.CharField(label="MFR", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    current_stock=forms.CharField(label="Current Stock", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    uom=forms.CharField(label="UOM", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    unit_price=forms.CharField(label="Unit Price", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    currency=forms.ChoiceField(label="Currency", choices=Currency_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    total_value_wo_gst_usd=forms.CharField(label=" Total Value WO GST USD", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    location=forms.CharField(label=" Location", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    vendor_name=forms.CharField(label="Vendor Name ", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    #dri_name=forms.CharField(label="DRI Name ", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))
    product_image = forms.FileField(label="Product Image", required=False, widget=forms.FileInput(attrs={"class":"form-control",'blank':True , 'required': False}))
    life_cycle = forms.CharField(label="Life Cycle(in months)", max_length=100, widget=forms.NumberInput(attrs={"class":"form-control"}))

class user_items_Form(forms.Form):
    try:
        items = store_items.objects.all()
        items_list = []
        for item in items:
            single_item = (item.id, str(item))
            items_list.append(single_item)
    except:
        items_list = []

    Shift_CHOICES =(
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("G", "G"),
    ("NA", "NA"),
    )

    Category_CHOICES =(
        ("spare", "spare"),
        ("Consumable", "Consumable"),
        ("NA", "NA"),
    )

    Line_CHOICES =(
        ("Common", "Common"),
        ("FATP", "FATP"),
        ("FATP D53G", "FATP D53G"),
        ("Fixtures", "Fixtures"),
        ("IQC", "IQC"),
        ("IQC-FA", "IQC-FA"),
        ("Line", "Line"),
        ("MAIN", "MAIN"),
        ("MAIN LINE", "MAIN LINE"),
        ("PACK", "PACK"),
        ("POST", "POST"),
        ("POST LINE", "POST LINE"),
        ("NA", "NA"),
    )
    IW_OOw_CHOICES =(
        ("IW", "IW"),
        ("OOW", "OOW"),
        ("NA", "NA"),
    )
    item=forms.ChoiceField(label="Item", choices=items_list, widget=forms.Select(attrs={"class":"form-control"}))
    req_qty=forms.CharField(label="Req Qty ", max_length=500, widget=forms.NumberInput(attrs={"class":"form-control"}))
    shift=forms.ChoiceField(label="Shift", choices=Shift_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    category=forms.ChoiceField(label="Category", choices=Category_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    line=forms.ChoiceField(label="Line",choices=Line_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    iw_oow=forms.ChoiceField(label="IW/OOW",choices=IW_OOw_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    
    


class remark_Form(forms.Form):
    remark=forms.CharField(label=" Remark ", max_length=500, widget=forms.TextInput(attrs={"class":"form-control"}))


   


  
    
    