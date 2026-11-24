from django.db import models
from django.conf import settings
from datetime import datetime

nutrigardentype = [
            ('Organic', 'Organic'),
            ('Uses Chemical Fertilizer', 'Uses Chemical Fertilizer'),
           
]
familysize=[('','Choose Your Option'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('more than 6', 'More than 6'),]

shedtype=[('','Choose Your Option'),
('Open Field', 'Open Field'),
('Poly House', 'Poly House'),
('Shed net', 'Shed net'),]

pattern=[('','Choose Your Option'),
('Circular', 'Circular'),
('Rectangle/Square', 'Rectangle/Square'),
('Other Pattern', 'Other Pattern'),]

consumption= [('','Choose Your Option'),
    ('Only self-consumption (includes sharing with neighbors)', 'Only self-consumption (includes sharing with neighbors)'),
('Selling surplus', 'Selling surplus'),
('Selling surplus with value addition', 'Selling surplus with value addition'),]

activityType= [('','Choose Your Option'),
('Fruits/ seeds/ vegetables', 'Fruits/ seeds/ vegetables'),
('Vegetarian + Poultry', 'Vegetarian + Poultry'),
('Vegetarian + Poultry + Others', 'Vegetarian + Poultry + Others'),]

#dynamic indications 
cultivationTech = [('','Choose Your Option'),
('Raised bed', 'Raised bed'),
('Circular bed', 'Circular bed'),
('Container cultivation', 'Container cultivation'),
('Vertical gardening', 'Vertical gardening'),
('Other', 'Other'),]

typeSeed = [('','Choose Your Option'),
('Indegenious','Indegenious'),
('Hybrid', 'Hybrid'),]

seedSource = [('','Choose Your Option'),
('Market', 'Market'),
('Household', 'Household'),
('Seed Bank', 'Seed Bank'),
('Government Department (Horticulture, KVK etc.)', 'Government Department (Horticulture, KVK etc.)'),
('NGOs/ CSOs', 'NGOs/ CSOs'),
('Others','Others'),]

seedBankLocation = [('','Choose Your Option'),
('Village', 'Village'),
('Panchayat', 'Panchayat'),
('Block', 'Block'),
('Others', 'Others'),]

fertilizerType = [('','Choose Your Option'),
('Chemical', 'Chemical'),
('Organic manure', 'Organic manure'),
('Natural', 'Natural'),]

fertSource = [('','Choose Your Option'),
('Household vermicompost', 'Household vermicompost'),
('Market', 'Market'),
('Livestock', 'Livestock'),
('Government', 'Government'),]

vermicompostGrade = [('','Choose Your Option'),
('Agnihotra', 'Agnihotra'),
('Jeevamurat', 'Jeevamurat'),
('Steramil', 'Steramil'),
('Neem', 'Neem'),
('Humic', 'Humic'),
('Others','Others'),]

pestManage = [('','Choose Your Option'),
('Healthy seedling production', 'Healthy seedling production'),
('Infected shoot clipping', 'Infected shoot clipping'),
('Pheromone trap', 'Pheromone trap'),
('Minimal use of pesticides', 'Minimal use of pesticides'),
('Others', 'Others'),]

typeOfFence = [('','Choose Your Option'),
('Natural (mud, bamboo, trees, shrubs, tree leaves etc.)', 'Natural (mud, bamboo, trees, shrubs, tree leaves etc.)'),
('Metal/ wire Fencing', 'Metal/ wire Fencing'),
('Cement/ brick wall', 'Cement/ brick wall'),
('Any cloth type material/ tarpaulin', 'Any cloth type material/ tarpaulin'),
('Others', 'Others'),]

irrigationMethod = [('','Choose Your Option'),
('Drip', 'Drip'),
('Flood', 'Flood'),
('Watering by pot', 'Watering by pot'),
('Rain-fed', 'Rain-fed'),
('Others', 'Others'),]

waterSource = [('','Choose Your Option'),
('Pond', 'Pond'),
('River', 'River'),
('Tube Well', 'Tube well'),
('Well', 'well'),
('Rain', 'Rain'),
('Lake', 'Lake'),
('Pipe water', 'Pipe water'),
('Others', 'Others'),]

resourcesLeveraged = [('','Choose Your Option'),
('Self', 'Self'),
('Government Scheme', 'Government Scheme'),
('NGOs/ CSOs', 'NGOs/ CSOs'),
('Others', 'Others'),]

govtSchemeName = [('','Choose Your Option'),
('MGNREGA', 'MGNREGA'),
('ICDS', 'ICDS'),
('Education', 'Education'),
('Agriculture', 'Agriculture'),
('Panchayat', 'Panchayat'),
('Others', 'Others'),]

yesOrno = [('','Yes/No'),('yes','Yes'),('no','No'), ]

provisionPlace = [('','Choose Your Option'),
('Cold storage', 'Cold storage'),
('Open storage', 'Open storage'),
('Others', 'Others'),]

month = [('','Select'),
('January', 'January'),
('February', 'February'),
('March', 'March'),
('April','April'),
('May','May'),
('June','June'),
('July','July'),
('August','August'),
('September','September'),
('October','October'),
('November','November'),
('December','December'),]

soldwhere = [('','Select'),
('Middleman','Middleman'),
('Institution','Institution'),
('direct','Direct'),
('CSOs','CSOs'),]

class BasicInformationModel(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    organization = models.CharField(max_length = 100)
    district  = models.CharField(max_length = 50)  
    village = models.CharField(max_length = 50)
    one_to_fivehundred = models.CharField(max_length = 5, default='no', blank=True,null = True)
    fivehundred_to_1000 = models.CharField(max_length = 5, default='no', blank=True,null = True)
    one_two_thousand = models.CharField(max_length = 5, default='no', blank=True,null = True)
    two_four_thousand = models.CharField(max_length = 5, default='no', blank=True,null = True)
    more4000 = models.CharField(max_length = 5, default='no', blank=True, null = True)
    vegetable = models.CharField(max_length = 5, default='no', blank=True, null = True)
    poultry = models.CharField(max_length = 5, default='no', blank=True, null = True)
    goat = models.CharField(max_length = 5, default='no', blank=True, null = True)
    fisheries = models.CharField(max_length = 5, default='no', blank=True, null = True)
    others = models.CharField(max_length = 5, default='no', blank=True, null = True)
    surplus = models.CharField(max_length = 50, default='')
    income = models.CharField(max_length = 50, default='', blank=True, null = True)
    prodCompany = models.CharField(max_length = 50, default='')
    farmernum = models.IntegerField(default='0', blank=True, null = True)
    innov_method = models.CharField(max_length = 150, default='')
    afif = models.CharField(max_length = 10,blank=True,null = True)
    ifAFIF = models.CharField(max_length = 10, blank=True,null = True)
    covervillage = models.IntegerField(default='0', blank=True,null = True)
    averagehousehold = models.IntegerField(default='0', blank=True,null = True)
    shg = models.IntegerField(default='0', blank=True,null = True)
    lat = models.CharField(max_length=15, default='')
    lng = models.CharField(max_length=15, default='')


# class NutrigardenInformationModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
#     village = models.CharField(max_length = 50)
#     pincode = models.CharField(max_length = 6)
#     nutrigardentype = models.CharField(max_length = 50)
#     size = models.CharField(max_length = 50)
#     use = models.CharField(max_length = 50)
#     varieties  = models.CharField(max_length = 50)
#     backyard = models.CharField(max_length = 10)
#     unit = models.CharField(max_length = 10,blank=True,null = True)
#     seed = models.CharField(max_length = 50)
#     nutrigardennumber = models.IntegerField()
#     organic = models.IntegerField()
#     training = models.CharField(max_length  = 100)
#     afvillage = models.CharField(max_length = 10, blank=True,null = True)
#     villagename = models.CharField(max_length = 50,blank=True,null = True)
#     villagenumber = models.CharField(max_length = 50,blank=True,null = True)
#     promote = models.CharField(max_length = 10)


# class factsheetInformationModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
#     location = models.CharField(max_length = 100, blank=True,null = True)
#     state = models.CharField(max_length = 100, blank=True,null = True)
#     district = models.CharField(max_length = 100, blank=True,null = True)
#     ICDSProj = models.CharField(max_length = 100, blank=True,null = True)
#     sector = models.CharField(max_length = 100, blank=True,null = True)
#     village = models.CharField(max_length = 100, blank=True,null = True)
#     anganwadi = models.CharField(max_length = 100, blank=True,null = True)
#     famsize = models.CharField(choices = familysize, max_length = 100, blank=True, default='Choose Your Option')
#     typeofShed = models.CharField(choices = shedtype, max_length = 100, blank=True, default='Choose Your Option')
#     patt = models.CharField(choices = pattern, max_length = 100, blank=True, default='Choose Your Option')
#     consump = models.CharField(choices = consumption, max_length = 100, blank=True, default='Choose Your Option')
#     typeOf = models.CharField(choices = activityType, max_length = 100, blank=True, default='Choose Your Option')

# class factsheetDynamicIndicatorsModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
#     cultTech = models.CharField(choices = cultivationTech, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     seedtype = models.CharField(choices = typeSeed, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     seedSource = models.CharField(choices = seedSource, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     seedbnkloc = models.CharField(choices = seedBankLocation, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     fertType = models.CharField(choices = fertilizerType, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     fertSour = models.CharField(choices = fertSource, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     vermigrade = models.CharField(choices = vermicompostGrade, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     pest = models.CharField(choices = pestManage, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     fence = models.CharField(choices = typeOfFence, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     irrig = models.CharField(choices = irrigationMethod, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     water = models.CharField(choices = waterSource, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     resrcLvrgd = models.CharField(choices = resourcesLeveraged, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     govt = models.CharField(choices = govtSchemeName, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     prov = models.CharField(choices = yesOrno, max_length = 100, blank=True,null = True, default='Choose Your Option')
#     provPlace = models.CharField(choices = provisionPlace, max_length = 100, blank=True,null = True, default='Choose Your Option')

# class financialExpensesModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
#     soilPrep = models.IntegerField(blank=True,null = True)
#     soilPrepDate= models.DateField(null=True, blank=True, default=datetime.now)
#     fertilizers = models.IntegerField( blank=True,null = True)
#     fertilizersDate = models.DateField(null=True, blank=True, default=datetime.now)
#     seeds = models.IntegerField( blank=True,null = True)
#     seedsDate = models.DateField(null=True, blank=True, default=datetime.now)
#     cultTools = models.IntegerField(blank=True,null = True)
#     cultToolsDate = models.DateField(null=True, blank=True, default=datetime.now)
#     fence = models.IntegerField(blank=True,null = True)
#     fenceDate = models.DateField(null=True, blank=True, default=datetime.now)
#     transportation = models.IntegerField(blank=True,null = True)
#     transportaionDate = models.DateField(null=True, blank=True, default=datetime.now)
#     labor = models.IntegerField(blank=True,null = True)
#     laborDate = models.DateField(null=True, blank=True, default=datetime.now)
#     irrigation = models.IntegerField(blank=True,null = True)
#     irrigationDate = models.DateField(null=True, blank=True, default=datetime.now)
#     miscellaneous = models.IntegerField(blank=True,null = True)
#     miscellaneousDate = models.DateField(null=True, blank=True, default=datetime.now)

# class outputIndicatorsModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
#     plantType = models.CharField(max_length = 100, blank=True,null = True)
#     sowingDate = models.DateField(null=True, blank=True, default=datetime.now)
#     harvestDate = models.DateField(null=True, blank=True, default=datetime.now)
#     seedQuantity = models.IntegerField(blank=True,null = True)
#     harvestQuant = models.IntegerField(blank=True,null = True)
#     lostQuant = models.CharField(choices = yesOrno, max_length = 100, blank=True,null = True)
#     income = models.CharField(max_length = 100, blank=True,null = True)
#     whereSold = models.CharField(choices = soldwhere, max_length = 100, blank=True,null = True)
#     finishingMonth = models.CharField(choices = month, max_length = 100, blank=True,null = True)
#     soldQuant = models.IntegerField(blank=True,null = True)
#     consumedQuant = models.IntegerField(blank=True,null = True)


