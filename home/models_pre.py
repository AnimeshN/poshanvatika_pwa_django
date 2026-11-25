from pickle import TRUE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.core.exceptions import ValidationError
import easygui
import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
#from matplotlib.pyplot import summer
from numpy import average
import datetime

# Create your models here.

# def validate_image(image):
#     file_size = image.file.size
#     limit_mb = 15
#     if file_size > limit_mb * 1024 * 1024:
#         easygui.msgbox("Upload image lesser than 15 MB", title="Warning!")
#         raise ValidationError("Max size of file is %s MB" % limit_mb)

# class CensusTable(models.Model):
#     sstart = models.DateTimeField(blank=True, null=True)
#     eend = models.DateTimeField(blank=True, null=True)
#     name_of_the_city = models.CharField(max_length=50, blank=True, null=True)
#     cencus_code = models.IntegerField(blank=True, null=True)
#     tree_common_name = models.CharField(max_length=50, blank=True, null=True)
#     scientific_name = models.CharField(max_length=50, blank=True, null=True)
#     tree_type = models.CharField(max_length=50, blank=True, null=True)
#     tree_gps_location = models.CharField(max_length=50, blank=True, null=True)
#     tree_gps_location_latitude = models.CharField(max_length=30, blank=True, null=True)
#     tree_gps_location_longitude = models.CharField(max_length=30, blank=True, null=True)
#     tree_gps_location_altitude = models.CharField(max_length=30, blank=True, null=True)
#     tree_gps_location_precision = models.CharField(max_length=30, blank=True, null=True)
#     photo = models.CharField(max_length=70, blank=True, null=True)
#     photo_url = models.BinaryField(blank=True, null=True)
#     tree_girth_in_inches = models.IntegerField(blank=True, null=True)
#     tree_height_in_cm = models.IntegerField(blank=True, null=True)
#     tree_canopy = models.CharField(max_length=50, blank=True, null=True)
#     total_area_in_sq_kms_under_all_trees = models.IntegerField(blank=True, null=True)
#     total_area_in_sq_kms_under_native_indegeniuos_trees = models.IntegerField(blank=True, null=True)
#     current_tree_age = models.IntegerField(blank=True, null=True)
#     age_of_tree_when_planted = models.CharField(max_length=50, blank=True, null=True)
#     date_of_plantation = models.DateField(blank=True, null=True)
#     present_status_of_tree = models.CharField(max_length=50, blank=True, null=True)
#     tree_ownership_plantation_initiated_by = models.CharField(max_length=50, blank=True, null=True)
#     please_specify_tree_ownership = models.CharField(max_length=50, blank=True, null=True)
#     name_of_the_owner = models.CharField(max_length=50, blank=True, null=True)
#     field_version_field = models.CharField(db_column='__version__', max_length=50, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
#     tree_scientific_tree_local_name = models.CharField(max_length=50, blank=True, null=True)
#     address = models.CharField(max_length=50, blank=True, null=True)
#     id = models.BigIntegerField(blank=True, null=False, primary_key=True)
#     field_uuid = models.CharField(db_column='_uuid', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_submission_time = models.DateField(db_column='_submission_time', blank=True, null=True)  # Field renamed because it started with '_'.
#     field_validation_status = models.CharField(db_column='_validation_status', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_notes = models.CharField(db_column='_notes', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_status = models.CharField(db_column='_status', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_submitted_by = models.CharField(db_column='_submitted_by', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_tags = models.CharField(db_column='_tags', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
#     field_index = models.IntegerField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.
#     tree_gps_location_geom = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'census_table'


class AhmedSchoolForm(models.Model):
    school_name=models.CharField(max_length = 250, default='', blank=True,null = True)
    
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    gram_panchayat_name = models.CharField(max_length=255, blank=True, null=True)
    principal_name = models.CharField(max_length=255, blank=True, null=True)
    data_entry_date = models.DateField(blank=True, null=True)
    officer_designation = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    school_level = models.CharField(max_length=255, blank=True, null=True)
    school_type = models.CharField(max_length=255, blank=True, null=True)
    sch_building_type = models.CharField(max_length=255, blank=True, null=True)
    sch_building_use = models.CharField(max_length=255, blank=True, null=True)
    sch_location = models.CharField(max_length=255, blank=True, null=True)
    tot_boys_students = models.IntegerField(blank=True, null=True)
    tot_girls_students = models.IntegerField(blank=True, null=True)
    tot_diff_abled_students = models.IntegerField(blank=True, null=True)
    drinking_water_availability_per_day = models.CharField(max_length=255, blank=True, null=True)
    water_storage_in_school = models.CharField(max_length=255, blank=True, null=True)
    is_water_quality_check_done = models.CharField(max_length=255, blank=True, null=True)
    is_sanitization_done_timely = models.CharField(max_length=255, blank=True, null=True)
    solid_waste_management = models.CharField(max_length=255, blank=True, null=True)
    sewage_water_management = models.CharField(max_length=255, blank=True, null=True)
    is_toilet_facility_available = models.CharField(max_length=255, blank=True, null=True)
    tot_boys_toilets = models.IntegerField(blank=True, null=True)
    tot_girls_toilets = models.IntegerField(blank=True, null=True)
    tot_diff_abled_toilets = models.IntegerField(blank=True, null=True)
    kitchen_hygiene = models.CharField(max_length=255, blank=True, null=True)
    hand_wash_before_eating = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.school_name




class CensusTable(models.Model):
    sstart = models.DateTimeField(blank=True, null=True)
    eend = models.DateTimeField(blank=True, null=True)
    name_of_the_ulb = models.CharField(max_length=50, blank=True, null=True)
    cencus_code = models.IntegerField(blank=True, null=True)
    tree_common_name = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=50, blank=True, null=True)
    tree_type = models.CharField(max_length=50, blank=True, null=True)
    tree_gps_location = models.CharField(max_length=220, blank=True, null=True)
    tree_gps_location_latitude = models.CharField(max_length=50, blank=True, null=True)
    tree_gps_location_longitude = models.CharField(max_length=50, blank=True, null=True)
    tree_gps_location_altitude = models.CharField(max_length=50, blank=True, null=True)
    tree_gps_location_precision = models.CharField(max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=70, blank=True, null=True)
    photo_url = models.BinaryField(blank=True, null=True)
    #photo_url = models.CharField(max_length=250,blank=True, null=True)
    tree_girth_in_inches = models.IntegerField(blank=True, null=True)
    tree_height_in_cm = models.IntegerField(blank=True, null=True)
    tree_canopy = models.CharField(max_length=250, blank=True, null=True)
    total_area_in_sq_kms_under_all_trees = models.IntegerField(blank=True, null=True)
    total_area_in_sq_kms_under_native_indegeniuos_trees = models.IntegerField(blank=True, null=True)
    current_tree_age = models.IntegerField(blank=True, null=True)
    age_of_tree_when_planted = models.CharField(max_length=50, blank=True, null=True)
    date_of_plantation = models.DateField(blank=True, null=True)
    present_status_of_tree = models.CharField(max_length=50, blank=True, null=True)
    tree_ownership_plantation_initiated_by = models.CharField(max_length=50, blank=True, null=True)
    please_specify_tree_ownership = models.CharField(max_length=50, blank=True, null=True)
    name_of_the_owner = models.CharField(max_length=50, blank=True, null=True)
    field_version_field = models.CharField(db_column='__version__', max_length=50, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    id = models.BigIntegerField(primary_key=True)
    field_uuid = models.CharField(db_column='_uuid', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submission_time = models.DateField(db_column='_submission_time', blank=True, null=True)  # Field renamed because it started with '_'.
    field_validation_status = models.CharField(db_column='_validation_status', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted_by = models.CharField(db_column='_submitted_by', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tags = models.CharField(db_column='_tags', max_length=50, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.IntegerField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.
    tree_gps_location_geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    name_of_the_user = models.CharField(max_length=250, blank=True, null=True)
    please_specify_common_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=50, blank=True, null=True)    
    def __str__(self):
        return self.name_of_the_ulb
    class Meta:
        managed = False
        db_table = 'census_table'



class UploadPictureModel(models.Model):
    # picture = models.ImageField(upload_to='PoshanVatikaPics/', blank=True, null=True, default='PoshanVatikaPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    # nutri_nm = models.CharField(max_length=100, default='')
    # area = models.IntegerField()
    village = models.CharField(max_length=100, blank=True, null=True)
    # district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    # pincode = models.CharField(max_length=8, blank=True, null=True)
    # lat = models.CharField(max_length=15)
    # lng = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='PoshanVatikaPics/', blank=True, null=True, default='PoshanVatikaPics/noImage.jpg')
    organization = models.CharField(max_length = 100, default='', blank=True,null = True)
    district  = models.CharField(max_length = 50, default='', blank=True,null = True) 
    pincode=models.CharField(max_length= 50, default='', blank=True,null = True)     
    self_made= models.CharField(max_length = 250, default='no', blank=True,null = True)
    local_ngo = models.CharField(max_length = 250, default='no', blank=True,null = True)
    external_support = models.CharField(max_length = 250, default='no', blank=True,null = True)
    community_level= models.CharField(max_length = 250, default='no', blank=True,null = True)
    govt_support= models.CharField(max_length = 250, default='no', blank=True,null = True)
    school_level = models.CharField(max_length = 250, default='no', blank=True, null = True)
    anganwadi = models.CharField(max_length = 250, default='no', blank=True, null = True)
    others_nutri = models.CharField(max_length = 250, default='no', blank=True, null = True)
    local_ngo=models.CharField(max_length= 250,default='', blank=True, null = True) 
    self_consumption= models.CharField(max_length = 250, default='no', blank=True,null = True)
    selling_surplus = models.CharField(max_length = 250, default='no', blank=True,null = True)
    surplus_addition = models.CharField(max_length = 250, default='no', blank=True,null = True)
    others_level= models.CharField(max_length = 250,default='no', blank=True, null = True)
    vegetable = models.CharField(max_length = 250, default='no', blank=True, null = True)
    backyard_poultry= models.CharField(max_length = 250, default='no', blank=True, null = True)
    backyard_fishery = models.CharField(max_length = 250, default='no', blank=True, null = True)
    others_scale = models.CharField(max_length = 250, default='no', blank=True, null = True)
    surplus = models.CharField(max_length = 250, default='',blank=True, null = True)
    income = models.CharField(max_length = 250, default='', blank=True, null = True)
    one_to_fourthousand_sq= models.CharField(max_length = 250, default='', blank=True, null = True)
    seed_ngo = models.CharField(max_length = 250, default='',blank=True, null = True)
    seasonal_vegetable = models.CharField(max_length = 250,default='', blank=True, null = True)
    perennial_vegetable= models.CharField(max_length = 250,default='', blank=True, null = True)
    fruitsgrown=models.CharField(max_length = 250,default='', blank=True, null = True)
    dailyfruit=models.CharField(max_length = 250, default='',blank=True, null = True)
    indigeous=models.CharField(max_length = 250, default='',blank=True, null = True)
    open_cultivation= models.CharField(max_length = 250, default='no', blank=True, null = True)
    open_cultivation_multilayer= models.CharField(max_length = 250, default='no', blank=True, null = True)
    protectcultivation_shed_net= models.CharField(max_length = 250, default='no', blank=True, null = True)
    protectcultivation_shed_polyhouse=models.CharField(max_length = 250, default='no', blank=True, null = True)
    cultivation_others = models.CharField(max_length = 50, default='no', blank=True, null = True)
    month= models.CharField(max_length = 250, default='', blank=True, null = True)
    well= models.CharField(max_length = 250, default='no', blank=True, null = True)
    pond= models.CharField(max_length = 250, default='no', blank=True, null = True)
    canel= models.CharField(max_length = 250, default='no', blank=True, null = True)
    bore_well=models.CharField(max_length = 250, default='no', blank=True, null = True)
    river = models.CharField(max_length = 250, default='no', blank=True, null = True)
    source_water= models.CharField(max_length = 250, default='no', blank=True, null = True)
    irrigation=models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_name=models.CharField(max_length = 250, default='', blank=True, null = True)
    any_weekly_class=models.CharField(max_length = 250, default='', blank=True, null = True)
    weekly=models.CharField(max_length = 250, default='', blank=True, null = True)
    any_innovative=models.CharField(max_length = 250, default='', blank=True, null = True)
    mid_day_meal = models.CharField(max_length = 250, default='no', blank=True, null = True)
    surplus_selling= models.CharField(max_length = 250, default='no', blank=True, null = True)
    openfield_science_lab= models.CharField(max_length = 250, default='no', blank=True, null = True)
    hot_cooked_meal = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_child = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_scale = models.CharField(max_length = 250, default='no', blank=True, null = True)
    lat = models.CharField(max_length=15, default='')
    lng = models.CharField(max_length=15, default='')
    type=models.CharField(max_length = 100, default='', blank=True,null = True)
    submission_date = models.DateTimeField(auto_now_add=True, blank=True)
    nal = models.CharField(max_length = 250, default='no', blank=True, null = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture
    def __str__(self):
        return str(self.organization)
    class Meta:
       managed = True

class UploadWellPictureModel(models.Model):
    picture = models.ImageField( upload_to='WellPics/', blank=True, null=True, default='WellPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadWellPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture

class UploadSeedModel(models.Model):
    id = models.AutoField(primary_key=TRUE)
    picture = models.ImageField( upload_to='SeedPics/', blank=True, null=True, default='SeedPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    seed_nm = models.CharField(max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super().save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture

    class Meta:
       managed = True
       db_table = 'home_uploadseedmodel'
       
class PoshanFormInformation(models.Model):
    organization_name = models.CharField(max_length=100,default='',blank=True, null = True)
    district_village_taluka_name = models.CharField(max_length=100,default='',blank=True, null = True)
    pin_code = models.IntegerField(blank=True, null=True,default='')
    lat = models.CharField(max_length=15,default='',blank=True, null = True)
    lng = models.CharField(max_length=15,default='',blank=True, null = True)
    type_of_nutri = models.CharField(max_length=355,default='',blank=True, null = True)
    name_of_ngo = models.CharField(max_length=100,default='',blank=True, null = True)
    level_nutri_garden = models.CharField(max_length=100,default='',blank=True, null = True)
    nutri_garden_scale=models.CharField(max_length=100,default='',blank=True, null = True)
    area_nutri_garden = models.CharField(max_length=100,default='',blank=True, null = True)
    ngo_year = models.CharField(max_length=100,default='',blank=True, null = True)
    type_seeds=models.CharField(max_length=100,default='',blank=True, null = True)
    seasonal_veg_name = models.CharField(max_length=500,default='',blank=True, null = True)
    perennial_veg_name = models.CharField(max_length=500,default='',blank=True, null = True)
    fruits_name = models.CharField(max_length=500,default='',blank=True, null = True)
    average=models.CharField(max_length = 250, default='',blank=True, null = True)
    jan=models.CharField(max_length = 250, default='',blank=True, null = True)
    feb= models.CharField(max_length = 250, default='no', blank=True, null = True)
    march= models.CharField(max_length = 250, default='no', blank=True, null = True)
    april= models.CharField(max_length = 250, default='no', blank=True, null = True)
    may=models.CharField(max_length = 250, default='no', blank=True, null = True)
    june = models.CharField(max_length = 50, default='no', blank=True, null = True)
    july= models.CharField(max_length = 250, default='', blank=True, null = True)
    august= models.CharField(max_length = 250, default='no', blank=True, null = True)
    septmber= models.CharField(max_length = 250, default='no', blank=True, null = True)
    october= models.CharField(max_length = 250, default='no', blank=True, null = True)
    november=models.CharField(max_length = 250, default='no', blank=True, null = True)
    december = models.CharField(max_length = 250, default='no', blank=True, null = True)
    adult= models.CharField(max_length = 250, default='no', blank=True, null = True)
    children=models.CharField(max_length = 250, default='no', blank=True, null = True)
    month_earnings=models.CharField(max_length = 250, default='', blank=True, null = True)
    month_expense=models.CharField(max_length = 250, default='', blank=True, null = True)
    cultivation_type=models.CharField(max_length = 250, default='', blank=True, null = True)
    rainy_season=models.CharField(max_length = 250, default='', blank=True, null = True)
    raniy_winter_transition = models.CharField(max_length = 250, default='no', blank=True, null = True)
    summer= models.CharField(max_length = 250, default='no', blank=True, null = True)
    summer_rainy_transition= models.CharField(max_length = 250, default='no', blank=True, null = True)
    winter= models.CharField(max_length = 250, default='no', blank=True, null = True)
    winter_summer_transition= models.CharField(max_length = 250, default='no', blank=True, null = True)
    surplus_nutri_garden= models.CharField(max_length = 250, default='no', blank=True, null = True)
    water_source = models.CharField(max_length = 250, default='no', blank=True, null = True)
    cultivation = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_name = models.CharField(max_length = 250, default='no', blank=True, null = True)
    weekly_class = models.CharField(max_length = 250, default='no', blank=True, null = True)
    weekly_time = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_scale = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_practice= models.CharField(max_length = 250, default='no', blank=True, null = True)
    id = models.CharField(max_length = 250, default='no', blank=True, null =False,primary_key=True)
    add_photo= models.CharField(max_length = 250, default='no', blank=True, null = True)
    
    

    # class Meta:
    #     managed = False
    #     db_table = 'poshan_form_information'
    # def __str__(self):
    #     return self.organization_name
    

class BasicPoshanModel(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    organization = models.CharField(max_length = 100)
    district  = models.CharField(max_length = 50) 
    pincode=models.CharField(max_length= 50)     
    self_made= models.CharField(max_length = 250, default='no', blank=True,null = True)
    local_ngo = models.CharField(max_length = 250, default='no', blank=True,null = True)
    external_support = models.CharField(max_length = 250, default='no', blank=True,null = True)
    community_level= models.CharField(max_length = 250, default='no', blank=True,null = True)
    govt_support= models.CharField(max_length = 250, default='no', blank=True,null = True)
    school_level = models.CharField(max_length = 250, default='no', blank=True, null = True)
    anganwadi = models.CharField(max_length = 250, default='no', blank=True, null = True)
    others_nutri = models.CharField(max_length = 250, default='no', blank=True, null = True)
    local_ngo=models.CharField(max_length= 250,default='', blank=True, null = True) 
    self_consumption= models.CharField(max_length = 250, default='no', blank=True,null = True)
    selling_surplus = models.CharField(max_length = 250, default='no', blank=True,null = True)
    surplus_addition = models.CharField(max_length = 250, default='no', blank=True,null = True)
    others_level= models.CharField(max_length = 250,default='no', blank=True, null = True)
    vegetable = models.CharField(max_length = 250, default='no', blank=True, null = True)
    backyard_poultry= models.CharField(max_length = 250, default='no', blank=True, null = True)
    backyard_fishery = models.CharField(max_length = 250, default='no', blank=True, null = True)
    others_scale = models.CharField(max_length = 250, default='no', blank=True, null = True)
    surplus = models.CharField(max_length = 250, default='',blank=True, null = True)
    income = models.CharField(max_length = 250, default='', blank=True, null = True)
    one_to_fourthousand_sq= models.CharField(max_length = 250, default='', blank=True, null = True)
    seed_ngo = models.CharField(max_length = 250, default='',blank=True, null = True)
    seasonal_vegetable = models.CharField(max_length = 250,default='', blank=True, null = True)
    perennial_vegetable= models.CharField(max_length = 250,default='', blank=True, null = True)
    fruitsgrown=models.CharField(max_length = 250,default='', blank=True, null = True)
    dailyfruit=models.CharField(max_length = 250, default='',blank=True, null = True)
    indigeous=models.CharField(max_length = 250, default='',blank=True, null = True)
    open_cultivation= models.CharField(max_length = 250, default='no', blank=True, null = True)
    open_cultivation_multilayer= models.CharField(max_length = 250, default='no', blank=True, null = True)
    protectcultivation_shed_net= models.CharField(max_length = 250, default='no', blank=True, null = True)
    protectcultivation_shed_polyhouse=models.CharField(max_length = 250, default='no', blank=True, null = True)
    cultivation_others = models.CharField(max_length = 50, default='no', blank=True, null = True)
    month= models.CharField(max_length = 250, default='', blank=True, null = True)
    well= models.CharField(max_length = 250, default='no', blank=True, null = True)
    pond= models.CharField(max_length = 250, default='no', blank=True, null = True)
    canel= models.CharField(max_length = 250, default='no', blank=True, null = True)
    bore_well=models.CharField(max_length = 250, default='no', blank=True, null = True)
    river = models.CharField(max_length = 250, default='no', blank=True, null = True)
    source_water= models.CharField(max_length = 250, default='no', blank=True, null = True)
    irrigation=models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_name=models.CharField(max_length = 250, default='', blank=True, null = True)
    any_weekly_class=models.CharField(max_length = 250, default='', blank=True, null = True)
    weekly=models.CharField(max_length = 250, default='', blank=True, null = True)
    any_innovative=models.CharField(max_length = 250, default='', blank=True, null = True)
    mid_day_meal = models.CharField(max_length = 250, default='no', blank=True, null = True)
    surplus_selling= models.CharField(max_length = 250, default='no', blank=True, null = True)
    openfield_science_lab= models.CharField(max_length = 250, default='no', blank=True, null = True)
    hot_cooked_meal = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_child = models.CharField(max_length = 250, default='no', blank=True, null = True)
    school_scale = models.CharField(max_length = 250, default='no', blank=True, null = True)
    lat = models.CharField(max_length=15, default='')
    lng = models.CharField(max_length=15, default='')

class PoshanInformation(models.Model):
    organization_name = models.CharField(max_length=100)
    district_village_taluka_name = models.CharField(max_length=100)
    pin_code = models.IntegerField(blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    type_of_nutri = models.CharField(max_length=50)
    name_of_ngo = models.CharField(max_length=100)
    area_nutri_garden = models.CharField(max_length=100)
    seasonal_veg_name = models.CharField(max_length=100)
    perennial_veg_name = models.CharField(max_length=100)
    fruits_name = models.CharField(max_length=100)
    month_earnings = models.IntegerField(blank=True, null=True)
    level_nutri_garden = models.CharField(max_length=100)
    nutri_garden_scale=models.CharField(max_length=100)


class KoboPoshan(models.Model):
    organization = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)
    lat_lng = models.CharField(max_length=100, blank=True, null=True)
    type_nutri = models.CharField(max_length=100, blank=True, null=True)
    local_ngo = models.CharField(max_length=100, blank=True, null=True)
    level_nutri = models.CharField(max_length=100, blank=True, null=True)
    nutri_scale = models.CharField(max_length=100, blank=True, null=True)
    selling_surplus = models.CharField(max_length=255, blank=True, null=True)
    surplus_in_month = models.CharField(max_length=100, blank=True, null=True)
    nutri_area = models.CharField(max_length=100, blank=True, null=True)
    nutri_area_other = models.CharField(max_length=100, blank=True, null=True)
    seeds = models.CharField(max_length=100, blank=True, null=True)
    seasonal_veg = models.CharField(max_length=100, blank=True, null=True)
    perennial_veg = models.CharField(max_length=100, blank=True, null=True)
    fruits = models.CharField(max_length=100, blank=True, null=True)
    avg_daily_fruits = models.CharField(max_length=100, blank=True, null=True)
    seed_type = models.CharField(max_length=100, blank=True, null=True)
    other_seed_type = models.CharField(max_length=100, blank=True, null=True)
    earning_per_month = models.CharField(max_length=100, blank=True, null=True)
    cultivation_type = models.CharField(max_length=100, blank=True, null=True)
    other_cultivation_type = models.CharField(max_length=100, blank=True, null=True)
    monthly_expenses = models.CharField(max_length=100, blank=True, null=True)
    water_source = models.CharField(max_length=100, blank=True, null=True)
    other_water_source = models.CharField(max_length=100, blank=True, null=True)
    irrigation_water = models.CharField(max_length=100, blank=True, null=True)
    org_name_school = models.CharField(max_length=100, blank=True, null=True)
    weekly_classes = models.CharField(max_length=100, blank=True, null=True)
    weekly_time = models.CharField(max_length=100, blank=True, null=True)
    nutri_scale_school = models.CharField(max_length=100, blank=True, null=True)
    other_nutri_scale_school = models.CharField(max_length=100, blank=True, null=True)
    innovative_practices = models.CharField(max_length=100, blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    endtime1 = models.DateTimeField(primary_key=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = TRUE
        db_table = 'kobo_poshan'

    def __str__(self):
        return self.organization
