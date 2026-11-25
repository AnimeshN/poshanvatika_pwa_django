from django import forms 
from .models import BasicInformationModel #NutrigardenInformationModel, factsheetInformationModel, factsheetDynamicIndicatorsModel, financialExpensesModel, outputIndicatorsModel

from bootstrap_datepicker_plus import DatePickerInput

from bootstrap_datepicker_plus.widgets import DatePickerInput

class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformationModel
        fields = '__all__'
        


# class NutrigardenInformationForm(forms.ModelForm):
#     class Meta:
#         model = NutrigardenInformationModel
#         fields = ('village','pincode','nutrigardentype','size','use','varieties','backyard','unit','seed','nutrigardennumber','organic','training','afvillage','villagename','villagenumber','promote')


# class factsheetInformationForm(forms.ModelForm):
#     class Meta:
#         model= factsheetInformationModel
#         fields = ('location','state','district', 'ICDSProj', 'sector', 'village', 'anganwadi', 'famsize','typeofShed','patt','consump', 'typeOf')
#         labels = {
#             'location' : ('Location of Nutri-garden/ POSHAN Vatika'),
#             'state' : ('State'),
#             'district' : ('District'),
#             'ICDSProj':('ICDS Project'),
#             'sector' : ('Sector'),
#             'village' : ('Village/Tola'),
#             'anganwadi' : ('Anganwadi Centre'),
#             'famsize' : ('If it is household (ICDS beneficiary) Nutri-garden then what is the family size of the household'),
#             'typeofShed' : ('Type of vegetable/ fruit Nutri-garden shed'),
#             'patt' : ('Nutri-garden patterns employed'),
#             'consump': ('Consumption category of Nutri-garden'),
#             'typeOf' : ('Type of Nutri-garden activity')
#         }
        

# class factsheetDynamicIndicatorsForm(forms.ModelForm):
#     class Meta:
#         model = factsheetDynamicIndicatorsModel
#         fields = ('cultTech', 'seedtype', 'seedSource', 'seedbnkloc', 'fertType', 'fertSour', 'vermigrade', 'pest', 'fence', 'irrig', 'water', 'resrcLvrgd', 'govt', 'prov', 'provPlace')
#         labels = {
#             'cultTech' : ('Cultivation Technique'),
#             'seedtype' : ('Type of Seed'),
#             'seedSource' : ('Source of Seed'),
#             'seedbnkloc' : ('If seed bank then location of seed bank'),
#             'fertType' : ('Type of Fertilizer'),
#             'fertSour' : ('Source of Fertilizer'),
#             'vermigrade' : ('If vermicompost, then which grade'),
#             'pest' : ('Pest Management'),
#             'fence' : ('Type of Fences'),
#             'irrig' : ('Irrigation method'),
#             'water': ('Water source'),
#             'resrcLvrgd' : ('Resources leveraged for the establishing the nutri-garden'),
#             'govt' : ('If government scheme, then name it'),
#             'prov' : ('Is there any provision for storage of produce'),
#             'provPlace' : ('If Yes, then where')
#         }
        


# class financialExpensesForm(forms.ModelForm):  
#     class Meta:
#         model = financialExpensesModel
#         fields = ('soilPrep', 'soilPrepDate', 'fertilizers', 'fertilizersDate', 'seeds', 'seedsDate', 'cultTools', 'cultToolsDate', 'fence', 'fenceDate', 'transportation', 'transportaionDate', 'labor', 'laborDate', 'irrigation', 'irrigationDate', 'miscellaneous', 'miscellaneousDate')
#         labels = {
#             'soilPrep' : ('Soil preparation (including seeding bed)'),
#             'fertilizers' : ('Fertilizers'),
#             'seeds' : ('Seeds'),
#             'cultTools' : ('Cultivation tools'),
#             'fence' : ('Fence'),
#             'transportation' : ('Transportation'),
#             'labor' : ('Labor'),
#             'irrigation' : ('Irrigation'),
#             'miscellaneous': ('Miscellaneous')

#         }
#         widgets = {
#                     'soilPrepDate': DatePickerInput(), 
#                     'fertilizersDate': DatePickerInput(), 
#                     'seedsDate': DatePickerInput(), 
#                     'cultToolsDate': DatePickerInput(), 
#                     'fenceDate': DatePickerInput(), 
#                     'transportaionDate': DatePickerInput(), 
#                     'laborDate': DatePickerInput(), 
#                     'irrigationDate': DatePickerInput(), 
#                     'miscellaneousDate': DatePickerInput(), 
#                  }



# class outputIndicatorsForm(forms.ModelForm):
#     class Meta:
#         model = outputIndicatorsModel
#         fields = ('plantType', 'sowingDate', 'harvestDate', 'seedQuantity', 'harvestQuant', 'lostQuant', 'income', 'whereSold', 'finishingMonth', 'soldQuant', 'consumedQuant' )
#         labels = {
#             'plantType' : ('Vegetable/ Fruit/ herbs'),
#             'sowingDate' : ('Date of sowing(dd/mm/yy)'),
#             'harvestDate' : ('Date of harvest(dd/mm/yy)'),
#             'seedQuantity' : ('Quantity of seed sowed (in gm)'),
#             'harvestQuant' : ('Quantity harvested (in Kg)'),
#             'lostQuant' : ('If any quantity lost after harvest'),
#             'income' : ('Income from sale of seeds/surplus (in Rs)'),
#             'whereSold' : ('Sold where'),
#             'finishingMonth' : ('Month of finishing the produce'),
#             'soldQuant' : ('Quantity sold (in Kg)'),
#             'consumedQuant' : ('Quantity Consumed (in Kg)')
#         }
#         widgets = {
#             'sowingDate' : DatePickerInput(), 
#             'harvestDate' : DatePickerInput(), 
#         }
