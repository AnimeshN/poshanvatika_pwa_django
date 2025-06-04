from cmath import log
from django.core.exceptions import TooManyFieldsSent
from django.shortcuts import render , redirect, get_object_or_404
from .forms import CreateUserForm
import re
# from django.core.files import 
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import base64, os
import time,requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from django.http import HttpResponse
import csv
from django.db.models.functions import ExtractYear
from django.db.models import Count

#login dependacies
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UploadPictureForm, UploadWellPictureForm,BasicPoshanForm,UploadSeedForm
from .models import  UploadWellPictureModel, UploadPictureModel,PoshanFormInformation,BasicPoshanModel,CensusTable,AhmedSchoolForm,UploadSeedModel,KoboPoshan,KoboPoshan2
# Create your views here.
from django.template.defaultfilters import filesizeformat
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.db.models.functions import TruncMonth 
from django.db.models import Sum, Avg ,Max

from django.views import View
from xml.etree import ElementTree as ET

#For autocad uplaod files
from .forms import AutoCADFileUploadForm

#for rendering the data from database 

# #compress image
# from io import BytesIO
# from PIL import Image
# from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib import messages
from django.conf import settings
import os
from django.shortcuts import render

def upload_autocadFiles(request):
    if request.method == 'POST':
        form = AutoCADFileUploadForm(request.POST, request.FILES)
        upload_type = request.POST.get('uploadType')

        if form.is_valid():
            files = request.FILES.getlist('file')
            uploaded_files = []
            existing_files = []
            unsupported_files = []

            # Set the external mount path
            directory_path = '/mnt/HC_Volume_22591574/autocadfiles'
            
            for file in files:
                # Check file extension
                if file.name.endswith(('.dxf', '.dwg')):
                    # Ensure the directory exists
                    if not os.path.exists(directory_path):
                        os.makedirs(directory_path, exist_ok=True)

                    # Construct the full file path
                    file_path = os.path.join(directory_path, file.name)

                    # Check if the file already exists
                    if os.path.exists(file_path):
                        existing_files.append(file.name)
                    else:
                        # Save the file to the desired location
                        with open(file_path, 'wb+') as destination:
                            for chunk in file.chunks():
                                destination.write(chunk)
                        uploaded_files.append(file.name)
                else:
                    unsupported_files.append(file.name)

            # Create messages with counts
            if uploaded_files:
                messages.success(request, f"Files uploaded successfully: {', '.join(uploaded_files)}. Total uploaded: {len(uploaded_files)}")
            
            if existing_files:
                messages.error(request, f"Files already exist: {', '.join(existing_files)}. Total existing: {len(existing_files)}")
            
            if unsupported_files:
                messages.error(request, f"Unsupported files: {', '.join(unsupported_files)}. Total unsupported: {len(unsupported_files)}")

            return render(request, 'home/upload.html', {'form': form})

        else:
            messages.error(request, "Form is not valid.")
    else:
        form = AutoCADFileUploadForm()

    return render(request, 'home/upload.html', {'form': form})

# def upload_autocadFiles(request):
#     if request.method == 'POST':
#         form = AutoCADFileUploadForm(request.POST, request.FILES)
#         upload_type = request.POST.get('uploadType')

#         if form.is_valid():
#             files = request.FILES.getlist('file')
#             uploaded_files = []
#             existing_files = []
#             unsupported_files = []

#             for file in files:
#                 # Check file extension
#                 if file.name.endswith(('.dxf', '.dwg')):
#                     # Ensure the directory exists
#                     directory_path = os.path.join(settings.MEDIA_ROOT, 'data/autocadfiles')
#                     if not os.path.exists(directory_path):
#                         os.makedirs(directory_path, exist_ok=True)

#                     # Construct the full file path
#                     file_path = os.path.join(directory_path, file.name)

#                     # Check if the file already exists
#                     if os.path.exists(file_path):
#                         existing_files.append(file.name)
#                     else:
#                         # Save the file to the desired location
#                         with open(file_path, 'wb+') as destination:
#                             for chunk in file.chunks():
#                                 destination.write(chunk)
#                         uploaded_files.append(file.name)
#                 else:
#                     unsupported_files.append(file.name)

#             # Create messages with counts
#             if uploaded_files:
#                 messages.success(request, f"Files uploaded successfully: {', '.join(uploaded_files)}. Total uploaded: {len(uploaded_files)}")
            
#             if existing_files:
#                 messages.error(request, f"Files already exist: {', '.join(existing_files)}. Total existing: {len(existing_files)}")
            
#             if unsupported_files:
#                 messages.error(request, f"Unsupported files: {', '.join(unsupported_files)}. Total unsupported: {len(unsupported_files)}")

#             return render(request, 'home/upload.html', {'form': form})

#         else:
#             messages.error(request, "Form is not valid.")
#     else:
#         form = AutoCADFileUploadForm()

#     return render(request, 'home/upload.html', {'form': form})
# def upload_autocadFiles(request):
#     if request.method == 'POST':
#         form = AutoCADFileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             files = request.FILES.getlist('file')
#             uploaded_files = []
#             for file in files:
#                 # Check file extension
#                 if file.name.endswith(('.xml', '.csv')):
#                     # Ensure the directory exists
#                     directory_path = os.path.join(settings.MEDIA_ROOT, 'data/autocadfiles')
#                     if not os.path.exists(directory_path):
#                         os.makedirs(directory_path, exist_ok=True)

#                     # Construct the full file path
#                     file_path = os.path.join(directory_path, file.name)

#                     # Check if the file already exists
#                     if os.path.exists(file_path):
#                         messages.error(request, f"File '{file.name}' already exists.")
#                         return render(request, 'home/upload.html', {'form': form})

#                     # Save the file to the desired location
#                     with open(file_path, 'wb+') as destination:
#                         for chunk in file.chunks():
#                             destination.write(chunk)
#                     uploaded_files.append(file.name)
#                 else:
#                     messages.error(request, "File not supported.")
#                     return render(request, 'home/upload.html', {'form': form})

#             if uploaded_files:
#                 messages.success(request, f"Files uploaded successfully: {', '.join(uploaded_files)}")
#             return render(request, 'home/upload.html', {'form': form})
#         else:
#             messages.error(request, "Form is not valid.")
#     else:
#         form = AutoCADFileUploadForm()

#     return render(request, 'home/upload.html', {'form': form})
# def upload_autocadFiles(request):
#     if request.method == 'POST':
#         form = AutoCADFileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             files = request.FILES.getlist('file')
#             uploaded_files = []
#             for file in files:
#                 # Check file extension
#                 if file.name.endswith(('.xml', '.csv')):
#                     # Ensure the directory exists
#                     directory_path = os.path.join(settings.MEDIA_ROOT, 'data/autocadfiles')
#                     if not os.path.exists(directory_path):
#                         os.makedirs(directory_path, exist_ok=True)

#                     # Construct the full file path
#                     file_path = os.path.join(directory_path, file.name)

#                     # Check if the file already exists
#                     if os.path.exists(file_path):
#                         messages.error(request, f"File '{file.name}' already exists.")
#                         return render(request, 'home/upload.html', {'form': form})

#                     # Save the file to the desired location
#                     with open(file_path, 'wb+') as destination:
#                         for chunk in file.chunks():
#                             destination.write(chunk)
#                     uploaded_files.append(file.name)
#                 else:
#                     messages.error(request, "File not supported.")
#                     return render(request, 'home/upload.html', {'form': form})

#             if uploaded_files:
#                 messages.success(request, f"Files uploaded successfully: {', '.join(uploaded_files)}")
#             return render(request, 'home/upload.html', {'form': form})
#         else:
#             messages.error(request, "Form is not valid.")
#     else:
#         form = AutoCADFileUploadForm()

#     return render(request, 'home/upload.html', {'form': form})

def viewselfconsVatikas(request):
    selfcons = PoshanFormInformation.objects.filter(level_nutri_garden='for_self_consumption',nutri_garden_scale ='Only for vegetables and fruits, Backyard Poultry')
    context = {'selfcons': selfcons }
    return render(request, 'home/viewVatikas.html', context )

def viewAFIFVatikas(request):
    vatikas2 = UploadPictureModel.objects.filter(type='AFIF')
    vatikascount = UploadPictureModel.objects.count()
    view_name = 'viewAFIFVatikas'
    context = {'vatikas2': vatikas2,'vatikascount':vatikascount,'view_name': view_name,'is_view_AFIF_Vatikas': view_name == 'viewAFIFVatikas' }
    return render(request, 'home/viewVatikas.html', context )

def viewVatikas(request):
    wells = UploadWellPictureModel.objects.all()
    view_name = 'viewVatikas'
    vatikas = UploadPictureModel.objects.all()
    vatikascount = UploadPictureModel.objects.count()
    AFIF_yearly_counts = UploadPictureModel.objects.annotate(year=ExtractYear('submission_date')) \
    .values('year') \
    .annotate(count=Count('id')) \
    .order_by('year')
    vatikas1 = PoshanFormInformation.objects.all()
    onlinevatikascount = PoshanFormInformation.objects.count()
    vatikas3 = KoboPoshan.objects.all()
    vatikas3a = KoboPoshan2.objects.all()
    kobovatiakscount = KoboPoshan.objects.count()+ KoboPoshan2.objects.count()
    vatikas2 = UploadPictureModel.objects.filter(type='AFIF')
    selfcons = PoshanFormInformation.objects.filter(level_nutri_garden='for_self_consumption',nutri_garden_scale ='Only for vegetables and fruits, Backyard Poultry')
    selfconscount =selfcons.count()
    sellsurp = PoshanFormInformation.objects.filter(level_nutri_garden='selling_surplus')
    sellsurpcount = sellsurp.count()
    context = {'vatikas1': vatikas1,'vatikas2': vatikas2, 'vatikas':vatikas,'selfcons':selfcons,'sellsurp':sellsurp,'vatikas3':vatikas3,'vatikas3a':vatikas3a,'vatikascount':vatikascount,'onlinevatikascount':onlinevatikascount,'kobovatiakscount':kobovatiakscount,'AFIF_yearly_counts':AFIF_yearly_counts,'selfconscount':selfconscount,'sellsurpcount':sellsurpcount,'view_name': view_name,'is_view_Vatikas': view_name == 'viewVatikas' }
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewVatikas.html', context )
    # return render(request, 'map/map.html', context)
def viewsarkarivatikas(request):
    # Your view logic here
    view_name = 'viewsarkarivatikas'
    

    context = {'view_name': view_name}
    return render(request, 'home/viewVatikas.html', context)

# def viewVatikas(request):
#     # wells = UploadWellPictureModel.objects.all()
#     vatikas = UploadPictureModel.objects.all()
#     # vatikas1 = PoshanInformation.objects.all()
#     # vatikas1 = BasicPoshanModel.objects.all()
#     # selfcons = PoshanInformation.objects.filter(level_nutri_garden='for_self_consumption',nutri_garden_scale ='Only for vegetables and fruits, Backyard Poultry')
#     # sellsurp = PoshanInformation.objects.filter(level_nutri_garden='selling_surplus')
    
    # context = {'vatikas1': vatikas1}
    #  context = {'vatikas1': vatikas1, 'vatikas':vatikas,'selfcons':selfcons,'sellsurp':sellsurp} 
    # {'selfcons':selfcons,'sellsurp':sellsurp}
    # context = {'wells': wells, 'mylist':mylist}
    return render(request, 'home/viewVatikas.html', context )
    #return render(request, 'map/map.html', context)

def viewWells(request):
    wells = UploadWellPictureModel.objects.all()
    context = {'wells': wells}
    return render(request, 'home/viewWells.html',context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def captwellpic(request):
    form = UploadWellPictureForm()
    global datauri
    # if request.is_ajax():
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        datauri = request.POST['picture']
    
    if request.method == 'POST' and not request.META.get('HTTP_X_REQUESTED_WITH'):
    # if request.method == 'POST':
    # if user is authenticated, use their username
                       
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if not request.user.is_authenticated:
                obj.username = "Guest"
            else:
                obj.username = request.user.username
            # obj.save()
        name = request.POST.get('name')
        well_nm = request.POST.get('well_nm')
        radius = request.POST.get('radius')
        depth = request.POST.get('depth')
        level = request.POST.get('level')
        village = request.POST.get('village')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        date= request.POST.get('date')
        water_quality = request.POST.get('water_quality')
        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "WellPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation = UploadWellPictureModel.objects.create(picture=filename, name=name, well_nm=well_nm, radius=radius, depth=depth, level=level, village=village, district=district, state=state,pincode=pincode, lat=lat, lng=lng, date=date, username=obj.username, water_quality =water_quality)
            picLocation.save()
            datauri= False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadWellPictureForm()
    return render(request,'home/captureWellPic.html',{})

# def uploadwellpic(request):
#     data = dict()
#     if "GET" == request.method:
#         return render(request,'home/uploadWellPic.html',{})
    
#     # process POST request
#     files = request.FILES  # multivalued dict
#     image = files.get("picture")
    
#     # compress the image here and then save it
#     i = Image.open(image)
#     thumb_io = BytesIO()
#     i.save(thumb_io, format='JPEG', quality=80)
#     inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'foo.jpeg', 
#                                               'image/jpeg', thumb_io.tell(), None)

#     instance = UploadWellPictureModel()
#     instance.image = inmemory_uploaded_file
#     instance.save()
#     return render(request,'home/uploadWellPic.html',{})
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def uploadwellpic(request):
    if request.method == 'POST':
        form = UploadWellPictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            messages.success(request, "Registration successful." )
            print("data is saved.")
            return redirect('/captwellpic')
    else:
        form = UploadWellPictureForm()
    return render(request,'home/uploadWellPic.html',{})
#Capture poshan vatika

def captvatikapic(request):
    form = UploadPictureForm()
    global datauri
    # if request.is_ajax():
    if request.is_ajax():
        datauri = request.POST['picture']
   
    
    if request.method == 'POST' and not request.is_ajax():
        form = UploadPictureForm(request.POST, request.FILES)
        # Save the username of the logged-in user
        # user = request.user
        # username = user.username
        # if form.is_valid():
        #     form.save()
        name = request.POST.get('name')
        # nutri_nm = request.POST.get('nutri_nm')
        # area = request.POST.get('area')
        village = request.POST.get('village')
        # district = request.POST.get('district')
        state = request.POST.get('state')
        # pincode = request.POST.get('pincode')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        organization= request.POST.get('organization')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        self_made=request.POST.get('self_made')
        local_ngo = request.POST.get('local_ngo')
        external_support = request.POST.get('external_support')
        community_level= request.POST.get('community_level')
        school_level = request.POST.get('school_level')
        anganwadi = request.POST.get('anganwadi')
        others_nutri =request.POST.get('other_nutri')
        self_consumption=request.POST.get('self_consumption')
        selling_surplus = request.POST.get('selling_surplus')
        surplus_addition = request.POST.get('surplus_addition')
        others_level= request.POST.get('other_level')
        vegetable = request.POST.get('vegetable')
        backyard_poultry= request.POST.get('backyard_poultary')
        backyard_fishery =request.POST.get('backyard_fishery')
        others_scale =request.POST.get('other_scale')
        surplus = request.POST.get('surplus')
        income =request.POST.get('income') 
        one_to_fourthousand_sq= request.POST.get('one_to_fourthousand')
        seed_ngo = request.POST.get('seed_ngo')
        seasonal_vegetable = request.POST.get('seasonal_vegetable')
        fruitsgrown=request.POST.get('fruitgrown')
        dailyfruit=request.POST.get('dailyfruit')
        indigeous=request.POST.get('indigeous')
        open_cultivation= request.POST.get('open_cultivation')
        open_cultivation_multilayer= request.POST.get('open_cultivation_multilayer')
        protectcultivation_shed_net= request.POST.get('protectcultivation_shed_net')
        protectcultivation_shed_polyhouse=request.POST.get('protectcultivation_shed_polyhouse')
        cultivation_others = request.POST.get('cultivation_others')
        month= request.POST.get('month')
        well= request.POST.get('well')
        canel= request.POST.get('canel')
        bore_well=request.POST.get('bore_well')
        river =request.POST.get('river')
        source_water= request.POST.get('source_water')
        school_name=request.POST.get('school_name')
        any_weekly_class=request.POST.get('any_weekly_class')
        weekly=request.POST.get('weekly')
        any_innovative=request.POST.get('any_innovative')
        mid_day_meal = request.POST.get('mid_day_meal')
        surplus_selling= request.POST.get('surplus_selling')
        openfield_science_lab= request.POST.get('openfield_science_lab')
        hot_cooked_meal = request.POST.get('hot_cooked_meal')
        school_child = request.POST.get('school_child')
        school_scale = request.POST.get('school_scale')
        type=request.POST.get('type')

        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "VatikaPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            # picLocation = UploadPictureModel.objects.create(picture=filename, name=name, nutri_nm=nutri_nm, area=area, village=village, district=district, state=state,pincode=pincode, lat=lat, lng=lng)
            picLocation = UploadPictureModel.objects.create(picture=filename,organization=organization,district=district,pincode=pincode,lat=lat,lng=lng,self_made=self_made,
                               local_ngo=local_ngo,external_support=external_support,
                               community_level=community_level,school_level=school_level,anganwadi=anganwadi,others_nutri=others_nutri,
                               self_consumption=self_consumption,selling_surplus=selling_surplus,surplus_addition=surplus_addition,
                               others_level=others_level,vegetable=vegetable,backyard_poultry=backyard_poultry,backyard_fishery=backyard_fishery,
                               others_scale=others_scale,surplus=surplus,income=income,one_to_fourthousand_sq=one_to_fourthousand_sq,
                               seed_ngo=seed_ngo,seasonal_vegetable=seasonal_vegetable,fruitsgrown=fruitsgrown,dailyfruit=dailyfruit,indigeous=indigeous,
                               open_cultivation=open_cultivation,open_cultivation_multilayer=open_cultivation_multilayer,
                               openfield_science_lab=openfield_science_lab,protectcultivation_shed_net=protectcultivation_shed_net,protectcultivation_shed_polyhouse=protectcultivation_shed_polyhouse,
                               cultivation_others=cultivation_others,month=month,well=well,canel=canel,bore_well=bore_well,river=river,
                               source_water=source_water,school_name=school_name,any_weekly_class=any_weekly_class,
                               weekly=weekly,any_innovative=any_innovative,mid_day_meal=mid_day_meal,surplus_selling=surplus_selling,
                               hot_cooked_meal=hot_cooked_meal,school_child=school_child,school_scale=school_scale,village=village,state=state,name=name,type=type)
            picLocation.save()
            datauri = False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadPictureForm()
    return render(request,'home/captureVatikaPic.html',{})

    
def uploadvatikapic(request):
    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            # messages.info(request, _(u'Your data is submitted successfully!'))
            messages.info(request,"Your Data is submitted successfully")
            return redirect('/captvatikapic')
    else:
        form = UploadPictureForm()
    return render(request,"home/uploadVatikaPic.html",{'form': form})


def contact(request):
    return render(request,"home/contact.html",{})

def nurition(request):
    return render(request,"forms/nutritiongarden_info.html",{})

# def nutri(request):
#     return render(request,"forms/poshan.html",{})
def nutri(request):
    if request.method == 'POST':
        form = BasicPoshanForm(request.POST)
        # if form.is_valid():
        #     instance = form.save()
        #     instance.user = request.user
        #     instance.save()
        organization= request.POST.get('organization')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        self_made=request.POST.get('self_made')
        local_ngo = request.POST.get('local_ngo')
        external_support = request.POST.get('external_support')
        community_level= request.POST.get('community_level')
        school_level = request.POST.get('school_level')
        anganwadi = request.POST.get('anganwadi')
        others_nutri =request.POST.get('other_nutri')
        self_consumption=request.POST.get('self_consumption')
        selling_surplus = request.POST.get('selling_surplus')
        surplus_addition = request.POST.get('surplus_addition')
        others_level= request.POST.get('other_level')
        vegetable = request.POST.get('vegetable')
        backyard_poultry= request.POST.get('backyard_poultary')
        backyard_fishery =request.POST.get('backyard_fishery')
        others_scale =request.POST.get('other_scale')
        surplus = request.POST.get('surplus')
        income =request.POST.get('income') 
        one_to_fourthousand_sq= request.POST.get('one_to_fourthousand')
        seed_ngo = request.POST.get('seed_ngo')
        seasonal_vegetable = request.POST.get('seasonal_vegetable')
        fruitsgrown=request.POST.get('fruitgrown')
        dailyfruit=request.POST.get('dailyfruit')
        indigeous=request.POST.get('indigeous')
        open_cultivation= request.POST.get('open_cultivation')
        open_cultivation_multilayer= request.POST.get('open_cultivation_multilayer')
        protectcultivation_shed_net= request.POST.get('protectcultivation_shed_net')
        protectcultivation_shed_polyhouse=request.POST.get('protectcultivation_shed_polyhouse')
        cultivation_others = request.POST.get('cultivation_others')
        month= request.POST.get('month')
        well= request.POST.get('well')
        canel= request.POST.get('canel')
        bore_well=request.POST.get('bore_well')
        river =request.POST.get('river')
        source_water= request.POST.get('source_water')
        school_name=request.POST.get('school_name')
        any_weekly_class=request.POST.get('any_weekly_class')
        weekly=request.POST.get('weekly')
        any_innovative=request.POST.get('any_innovative')
        mid_day_meal = request.POST.get('mid_day_meal')
        surplus_selling= request.POST.get('surplus_selling')
        openfield_science_lab= request.POST.get('openfield_science_lab')
        hot_cooked_meal = request.POST.get('hot_cooked_meal')
        school_child = request.POST.get('school_child')
        school_scale = request.POST.get('school_scale')
        nutri=BasicPoshanModel(organization=organization,district=district,pincode=pincode,lat=lat,lng=lng,self_made=self_made,
                               local_ngo=local_ngo,external_support=external_support,
                               community_level=community_level,school_level=school_level,anganwadi=anganwadi,others_nutri=others_nutri,
                               self_consumption=self_consumption,selling_surplus=selling_surplus,surplus_addition=surplus_addition,
                               others_level=others_level,vegetable=vegetable,backyard_poultry=backyard_poultry,backyard_fishery=backyard_fishery,
                               others_scale=others_scale,surplus=surplus,income=income,one_to_fourthousand_sq=one_to_fourthousand_sq,
                               seed_ngo=seed_ngo,seasonal_vegetable=seasonal_vegetable,fruitsgrown=fruitsgrown,dailyfruit=dailyfruit,indigeous=indigeous,
                               open_cultivation=open_cultivation,open_cultivation_multilayer=open_cultivation_multilayer,
                               openfield_science_lab=openfield_science_lab,protectcultivation_shed_net=protectcultivation_shed_net,protectcultivation_shed_polyhouse=protectcultivation_shed_polyhouse,
                               cultivation_others=cultivation_others,month=month,well=well,canel=canel,bore_well=bore_well,river=river,
                               source_water=source_water,school_name=school_name,any_weekly_class=any_weekly_class,
                               weekly=weekly,any_innovative=any_innovative,mid_day_meal=mid_day_meal,surplus_selling=surplus_selling,
                               hot_cooked_meal=hot_cooked_meal,school_child=school_child,school_scale=school_scale)
        nutri.save()
        print("data is saved.")
        return redirect('/')
    else:
        form = BasicPoshanForm()
    return render(request,'forms/poshan.html',{'form':form})
def about(request):
    return render(request,"home/about.html",{})

def myPoshan(request):
    return render(request,"home/myPoshan.html",{})

def VayamUpakram(request):
    return render(request, "home/VayamPrakalp.html")

def ruTAG(request):
    return render(request, "home/ruTAG.html")

def WB_SNCU(request):
    return render(request, "home/WB_SNCU.html")

def SNCU(request):
    return render(request, "home/SNCU_MAPS.html")
def MAH_SNCU(request):
    return render(request, "home/MAH_SNCU.html")

# def upload_autocadFiles(request):
#     return render(request, "home/upload.html")

def treecensus(request):
    tree = CensusTable.objects.all()
    tree_satara = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council')
    tree_natepute = CensusTable.objects.filter(name_of_the_ulb='Natepute')
    tree_count = CensusTable.objects.count()
    tree_count_satara = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council').count()
    tree_count_natepute = CensusTable.objects.filter(name_of_the_ulb='Natepute').count()
    context = {'tree':tree,'tree_count':tree_count,'tree_count_satara':tree_count_satara,'tree_count_natepute':tree_count_natepute,'tree_satara':tree_satara,'tree_natepute':tree_natepute}
    return render(request,"home/treecensus.html",context)
# def treecharts(request):
#     return render(request,"home/tree_census_charts.html",{})

def treecharts(request):
    census_table_csv_data = CensusTable.objects.all()
    


    df = pd.DataFrame(census_table_csv_data.values())
    
    # print(df.columns)
    # fig = px.histogram(df, x = 'name_of_the_ulb')
    # plt.xlabel('Number of Trees')
    # plt.ylabel('Cities')
    # # fig.write_image('static/charts/tree-city.png')
    # plt.close()
    
    
    # fig = px.histogram(df[df['tree_type']=='Indegenious'], x = 'name_of_the_ulb')
    # plt.xlabel('Number of Indegenious Trees')
    # plt.ylabel('Cities')
    # fig.write_image('static/charts/indegenious-city.png')
    # plt.close()
    
    # fig = px.bar(df, x='tree_common_name', y= 'total_area_in_sq_kms_under_all_trees')
    # plt.xlabel('Common Name of the tree')
    # plt.ylabel('Total are in sq kms under all tree')
    # plt.xticks(rotation=40)
    # fig.write_image('static/charts/tree-area.png')
    # plt.close()

    no_of_heritage_trees = len(df[df['current_tree_age'] >= 50])
    no_of_newly_planted_trees = len(df[df['current_tree_age'] <= 25])
    total_area_under_indegenious_trees = sum(df['total_area_in_sq_kms_under_native_indegeniuos_trees'].tolist())
    total_area_under_all_trees = sum(df['total_area_in_sq_kms_under_all_trees'].tolist())
    trees_under_govt_land = sum(df[df['tree_ownership_plantation_initiated_by'] == 'Government']['total_area_in_sq_kms_under_all_trees'].tolist())
    trees_under_private_land = sum(df[df['tree_ownership_plantation_initiated_by'] == 'Private']['total_area_in_sq_kms_under_all_trees'].tolist())
    trees_under_other_land = sum(df[df['tree_ownership_plantation_initiated_by'] == 'Others']['total_area_in_sq_kms_under_all_trees'].tolist())

    print(no_of_heritage_trees)
    print(no_of_newly_planted_trees)
    print(total_area_under_indegenious_trees)
    print(total_area_under_all_trees)
    print(trees_under_govt_land)
    print(trees_under_private_land)
    print(trees_under_other_land)

    total_trees = CensusTable.objects.all().count()
    total_indegenious_trees = CensusTable.objects.filter(tree_type='Indegenious').count()
    govt_trees = CensusTable.objects.filter(tree_ownership_plantation_initiated_by='Government').count()
    private_trees = CensusTable.objects.filter(tree_ownership_plantation_initiated_by='Private').count()
    other_trees = CensusTable.objects.filter(tree_ownership_plantation_initiated_by='Other').count()

    satara_total_trees = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council').count()
    satara_total_indegenious_trees = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council',tree_type='Indegenious').count()
    satara_govt_trees = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council',tree_ownership_plantation_initiated_by='Government').count()
    satara_private_trees = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council',tree_ownership_plantation_initiated_by='Private').count()
    satara_other_trees = CensusTable.objects.filter(name_of_the_ulb='Satara Municipal Council',tree_ownership_plantation_initiated_by='Other').count()

    natepute_total_trees = CensusTable.objects.filter(name_of_the_ulb='Natepute').count()
    natepute_total_indegenious_trees = CensusTable.objects.filter(name_of_the_ulb='Natepute',tree_type='Indegenious').count()
    natepute_govt_trees = CensusTable.objects.filter(name_of_the_ulb='Natepute',tree_ownership_plantation_initiated_by='Government').count()
    natepute_private_trees = CensusTable.objects.filter(name_of_the_ulb='Natepute',tree_ownership_plantation_initiated_by='Private').count()
    natepute_other_trees = CensusTable.objects.filter(name_of_the_ulb='Natepute',tree_ownership_plantation_initiated_by='Other').count()




    context = {
        'heritage_trees' : no_of_heritage_trees,
        'newly_planted_trees' : no_of_newly_planted_trees,
        'area_under_indegenious_trees' : total_area_under_indegenious_trees,
        'area_under_all_trees' : total_area_under_all_trees,
        'govt_land_trees' : trees_under_govt_land,
        'private_land_trees' : trees_under_private_land,
        'other_land_trees' : trees_under_other_land,
        'total_trees':total_trees,
        'total_indegenious_trees':total_indegenious_trees,
        'govt_trees':govt_trees,
        'private_trees':private_trees,
        'other_trees':other_trees,
        'satara_total_trees':satara_total_trees,
        'satara_total_indegenious_trees':satara_total_indegenious_trees,
        'satara_govt_trees':satara_govt_trees,
        'satara_private_trees':satara_private_trees,
        'satara_other_trees':satara_other_trees,
        'natepute_total_trees':natepute_total_trees,
        'natepute_total_indegenious_trees':natepute_total_indegenious_trees,
        'natepute_govt_trees':natepute_govt_trees,
        'natepute_private_trees':natepute_private_trees,
        'natepute_other_trees':natepute_other_trees

        }

    return render(request,'home/tree_census_charts.html', context)

def ahmednagar_schools(request):
    ahmed_sch = AhmedSchoolForm.objects.all()
    context = {'ahmed_sch':ahmed_sch}
    return render(request,"home/ahmednagar_schools.html",context)

def ahmed_sch_form(request):
    form = AhmedSchoolForm()
    if request.method == 'POST':
        form = AhmedSchoolForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        # name = request.POST.get('name')
        # form = CoalForm(request.POST, request.FILES)
        school_name = request.POST.get('school_name')
        lat=request.POST.get('lat')
        lng=request.POST.get('lng')
        ahmed_sch = AhmedSchoolForm.objects.create(school_name = school_name,lat=lat,lng=lng)
        ahmed_sch.save()
        messages.info(request, _(u'Your data is submitted successfully!'))
        # return HttpResponseRedirect(request.path_info)
        return redirect('/ahmed_sch_form')
           
    else:
        form = AhmedSchoolForm()
    return render(request,'home/ahmed_sch_form.html',{})


def basic(request):
    return render(request,"forms/basic_forms.html",{})

def news(request):
    return render(request,"home/news.html",{})
def howto(request):
    return render(request,"home/How-to.html",{})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="home/login.html", context={"login_form":form})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def register_request(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    context = {'form':form}
    return render(request, "home/register.html", context)


# archive--> to archive all data from database table into csv
def archive(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Beneficiary name', 'State', 'District', 'Village','Pincode','Organization','type:Individual level-self made','type:Individual level-got help from local NGO','type:Community level-without external support','type:Community level-with support from external agency','type:Individual level-through Government support','type:School Nutri-garden','type:anganwadi','type:other','Name of supporting local NGO','Level:self consumption','Level:selling surplus','Level:Selling surplus with value addition','Level:other','Scale:Only for vegetables and fruits','Scale:backyard poultry','Scale:backyard fishery','Scale:other','Are you selling the surplus from Nutri-Garden','If yes How much surplus you sell per month (in Kg/month)','Area of Nutri-garden','Does the NGO/ supporter provide seeds every year?','seasonal vegetable','perennial vegetable','fruits grown','daily fruit output','Type of Seeds used in Nutri-Garden','Average Monthly income from Nutri-garden','Type of Cultivation method:open cultivation','Type of Cultivation method:open cultivation multilayer','Type of Cultivation method:protectcultivation using shed net','Type of Cultivation method:protectcultivation using shed polyhouse','Type of Cultivation method:other','Average per month expenses','Source of Water:well','Source of Water:pond','Source of Water:canel','Source of Water:bore_well','Source of Water:river','Source of Water:nal','Source of Water:other','Irrigation Water Availability','Name the organizations / government schemes supporting the school Nutri-Garden','any weekly class','Weekly time spent by students','Any Innovative practices','School nutri-garden scale:mid day meal','School nutri-garden scale:Selling the surplus produce from Nutri-Garden','School nutri-garden scale:openfield science lab','School nutri-garden scale:hot cooked meal','School nutri-garden scale:sharing the excess produce','School nutri-garden scale:other','category','submission_date'])

    for project in UploadPictureModel.objects.all().values_list('name', 'state', 'district', 'village','pincode','organization','self_made','local_ngo','external_support','community_level','govt_support','school_level','anganwadi','others_nutri','local_ngo','self_consumption','selling_surplus','surplus_addition','others_level','vegetable','backyard_poultry','backyard_fishery','others_scale','surplus','month','one_to_fourthousand_sq','seed_ngo','seasonal_vegetable','perennial_vegetable','fruitsgrown','dailyfruit','indigeous','income','open_cultivation','open_cultivation_multilayer','protectcultivation_shed_net','protectcultivation_shed_polyhouse','cultivation_others','month','well','pond','canel','bore_well','river','nal','source_water','irrigation','school_name','any_weekly_class','weekly','any_innovative','mid_day_meal','surplus_selling','openfield_science_lab','hot_cooked_meal','school_child','school_scale','type','submission_date'):
        writer.writerow(project)

    response['Content-Disposition'] = 'attachment; filename="archive.csv"'

    return response
def single(request,id):
    s=UploadPictureModel.objects.get(id=id)
    # print(s)
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Beneficiary name', 'State', 'District', 'Village','Pincode','Organization','type:Individual level-self made','type:Individual level-got help from local NGO','type:Community level-without external support','type:Community level-with support from external agency','type:Individual level-through Government support','type:School Nutri-garden','type:anganwadi','type:other','Name of supporting local NGO','Level:self consumption','Level:selling surplus','Level:Selling surplus with value addition','Level:other','Scale:Only for vegetables and fruits','Scale:backyard poultry','Scale:backyard fishery','Scale:other','Are you selling the surplus from Nutri-Garden','If yes How much surplus you sell per month (in Kg/month)','Area of Nutri-garden','Does the NGO/ supporter provide seeds every year?','seasonal vegetable','perennial vegetable','fruits grown','daily fruit output','Type of Seeds used in Nutri-Garden','Average Monthly income from Nutri-garden','Type of Cultivation method:open cultivation','Type of Cultivation method:open cultivation multilayer','Type of Cultivation method:protectcultivation using shed net','Type of Cultivation method:protectcultivation using shed polyhouse','Type of Cultivation method:other','Average per month expenses','Source of Water:well','Source of Water:pond','Source of Water:canel','Source of Water:bore_well','Source of Water:river','Source of Water:nal','Source of Water:other','Irrigation Water Availability','Name the organizations / government schemes supporting the school Nutri-Garden','any weekly class','Weekly time spent by students','Any Innovative practices','School nutri-garden scale:mid day meal','School nutri-garden scale:Selling the surplus produce from Nutri-Garden','School nutri-garden scale:openfield science lab','School nutri-garden scale:hot cooked meal','School nutri-garden scale:sharing the excess produce','School nutri-garden scale:other','category','submission_date'])
    # s.id == this will fetch id of each project--- helps in downloading excel sheet of only single project
    for project in UploadPictureModel.objects.filter(id=s.id).values_list('name', 'state', 'district', 'village','pincode','organization','self_made','local_ngo','external_support','community_level','govt_support','school_level','anganwadi','others_nutri','local_ngo','self_consumption','selling_surplus','surplus_addition','others_level','vegetable','backyard_poultry','backyard_fishery','others_scale','surplus','month','one_to_fourthousand_sq','seed_ngo','seasonal_vegetable','perennial_vegetable','fruitsgrown','dailyfruit','indigeous','income','open_cultivation','open_cultivation_multilayer','protectcultivation_shed_net','protectcultivation_shed_polyhouse','cultivation_others','month','well','pond','canel','bore_well','river','nal','source_water','irrigation','school_name','any_weekly_class','weekly','any_innovative','mid_day_meal','surplus_selling','openfield_science_lab','hot_cooked_meal','school_child','school_scale','type','submission_date'):
        # if(UploadPictureModel.objects.filter(project_name=s).latest('id')):
          writer.writerow(project)

    response['Content-Disposition'] = 'attachment; filename="project_info.csv"'

    return response
    
    # print(s)
    # return render(request,'home/download.html')

def uploadseedpic(request):
    form = UploadSeedForm()
    global datauri

    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    if is_ajax(request):
        datauri = request.POST['picture']
    
    # if request.method == 'POST' and not request.is_ajax():
    if request.method == 'POST' and not is_ajax(request):
        form = UploadSeedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        name = request.POST.get('name')
        # nutri_nm = request.POST.get('nutri_nm')
        # area = request.POST.get('area')
        village = request.POST.get('village')
        # district = request.POST.get('district')
        state = request.POST.get('state')
        # pincode = request.POST.get('pincode')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        # organization= request.POST.get('organization')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        seed_nm=request.POST.get('seed_nm')
        contact=request.POST.get('contact')


        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "SeedPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            picLocation =UploadSeedModel.objects.create(picture=filename,district=district,pincode=pincode,lat=lat,lng=lng,
                               village=village,state=state,name=name,seed_nm=seed_nm,contact=contact)
            
            picLocation.save()
            datauri= False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadSeedForm()
    return render(request,'home/UploadSeedPic.html',{})

def captseedpic(request):
    form = UploadSeedForm()
    global datauri
    def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    if is_ajax(request):
        datauri = request.POST['picture']
   
    
    if request.method == 'POST' and not is_ajax(request):
        
        form = UploadSeedForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        print(form)
        name = request.POST.get('name')
        # nutri_nm = request.POST.get('nutri_nm')
        # area = request.POST.get('area')
        village = request.POST.get('village')
        # district = request.POST.get('district')
        state = request.POST.get('state')
        # pincode = request.POST.get('pincode')
        # lat = request.POST.get('lat')
        # lng = request.POST.get('lng')
        # organization= request.POST.get('organization')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        seed_nm=request.POST.get('seed_nm')
        contact=request.POST.get('contact')


        try:
            imgstr = re.search(r'base64,(.*)', datauri).group(1)
            data = ContentFile(base64.b64decode(imgstr))
            myfile = "SeedPics/profile-"+time.strftime("%Y%m%d-%H%M%S")+".png"
            fs = FileSystemStorage()
            filename = fs.save(myfile, data)
            # picLocation = UploadPictureModel.objects.create(picture=filename, name=name, nutri_nm=nutri_nm, area=area, village=village, district=district, state=state,pincode=pincode, lat=lat, lng=lng)
            picLocation =UploadSeedModel.objects.create(picture=filename,district=district,pincode=pincode,lat=lat,lng=lng,
                               village=village,state=state,name=name,seed_nm=seed_nm,contact=contact)
            print(picLocation)
            picLocation.save()
            datauri = False
            del datauri
        except NameError:
            print("Image is not captured")
    else:
        form = UploadSeedForm()
    return render(request,'home/captureSeedPic.html',{})

def well_info(request):
    welldata = UploadWellPictureModel.objects.all().order_by('id')
    
    # check if a search query was submitted
    if request.GET.get('search'):
        # get the search query from the submitted form
        search_query = request.GET.get('search')
        
        # filter the welldata queryset to only include results containing the search query
        welldata = welldata.filter(well_nm__icontains=search_query)
        
        # create a message to display the search results
        message = f"Search results for '{search_query}':"
        
    else:
        # set message to None if no search query was submitted
        message = None
    
    context = {
        'welldata': welldata,
        'message': message,
    }
    # well_data= UploadWellPictureModel.objects.all().order_by('id')
    # date = []
    # level = []
    # for data in well_data:
    #     date.append(str(data.date))
    #     level.append(data.level)
    # context = {
    #     'dates': date,
    #     'level': level,
    # }
    
    return render(request, 'home/well_info.html', context)#context

def graph_well(request):
    well_data= UploadWellPictureModel.objects.all().order_by('date')   
    date = []
    level = []
    highest_level = []
    monthly_data = well_data.annotate(month=TruncMonth('date')).values('month').annotate(level_avg=Avg('level'),level_max=Max('level'))
    for data in monthly_data:
        if data['month'] is not None:
            date.append(data['month'].strftime('%B %Y'))
        else:
            date.append('')
        level.append(str(data['level_avg']))
        highest_level.append(str(data['level_max']))
    context = {
        'dates': date,
        'level': level,
        'highest_level': highest_level,
    }
    # water_level_data = {}
    # for data in well_data:
    #     date = data.date.strftime("%Y-%m")
    #     if date in water_level_data:
    #         water_level_data[date].append(data.level)
    #     else:
    #         water_level_data[date] = [data.level]
    # for date, levels in water_level_data.items():
    #     water_level_data[date] = sum(levels) / len(levels)
    # return render(request, 'home/graph_well.html',{'water_level_data':water_level_data})

    return render(request, 'home/graph_well.html',context)

def view_poshan(request):
    poshan_data= UploadPictureModel.objects.all().order_by('id')
    return render(request, 'home/view_poshan.html' ,{'poshandata': poshan_data}, )

def view_entered_details(request):
    username = request.user.username
    # Retrieve the record from the database based on the user who is currently logged in
    uploaded_pics = UploadWellPictureModel.objects.filter(username=username)
    
    context = {
        'uploaded_pics': uploaded_pics
    }
    return render(request, 'home/view_entered_details.html',context)

# def delete_uploaded_pic(request, pic_id):
#     pic = get_object_or_404(UploadWellPictureModel, id=pic_id, name=request.user.username)
#     pic.delete()
#     return redirect('view_entered_details')

# def delete_well(request):
#     pics = UploadWellPictureModel.objects.filter(username=request.user.username).values()
#     for pic in pics:
#         pic['delete_url'] = reverse('delete_well', args=[pic['id']])
#     context = {'pics': pics}
#     return render(request, 'home/view_entered_details.html', context)
# def delete(request,id):
#     dele = UploadWellPictureModel.objects.get(id=id)
#     dele.delete()
#     return redirect('/view_entered_details')

def edit_well_picture(request, pk):
    well_picture = get_object_or_404(UploadWellPictureModel,pk=pk, username=request.user.username)
    
    # form= None 

    if request.method == 'POST':
        form = UploadWellPictureForm(request.POST, instance=well_picture)
        if form.is_valid():
            

            well_picture = form.save(commit=False)
            well_picture.username = request.user.username
            
            well_picture.save()
            messages.success(request, 'Well picture updated successfully')
            return redirect('view_entered_details')
    else:
        # messages.error(request, 'There was an error in the form. Please correct it.')
        form = UploadWellPictureForm(instance=well_picture)

    context = {
        'form': form ,
        'well_picture': well_picture,
    }

    return render(request, 'home/edit_well_picture.html', context)

