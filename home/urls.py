from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from map.views import map

urlpatterns = [
    path('compendium', map, name='compendium'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_request, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register_request, name='register'),
    path('myPoshan/', views.myPoshan, name='myPoshan'),
    path('treecensus/', views.treecensus, name='treecensus'),
    path('treecharts/', views.treecharts, name='treecharts'),
    path('VayamUpakram/', views.VayamUpakram, name='VayamUpakram'),

    path('news/', views.news, name='news'),
    path('howto/', views.howto, name='howto'),
    path('captvatikapic/', views.captvatikapic, name='captvatikapic'),
    path('uploadvatikapic/', views.uploadvatikapic, name='uploadvatikapic'),
    path('captwellpic/', views.captwellpic, name='captwellpic'),
    path('uploadwellpic/', views.uploadwellpic, name='uploadwellpic'),
    path('viewVatikas/', views.viewVatikas, name='viewVatikas'),
    path('viewWells/',views.viewWells, name='viewWells'),
    path('ahmednagar_schools/',views.ahmednagar_schools,name='ahmednagar_schools'),
    path('ahmed_sch_form/',views.ahmed_sch_form,name='ahmed_sch_form'),
    path('archive/',views.archive,name='archive'),
    path('download/<int:id>',views.single,name='download'),
    path('captseedpic/', views.captseedpic, name='captseedpic'),
    path('uploadseedpic/', views.uploadseedpic, name='uploadseedpic'),
    path('well_info/', views.well_info, name='well_info'),
    path('graph_well/', views.graph_well, name='graph_well'),
    path('view_poshan/', views.view_poshan, name='view_poshan'),
    path('view_entered_details/', views.view_entered_details, name="view_entered_details"),
    # path('delete/<int:id>', views.delete, name='delete')
    path('edit_well_picture/<int:pk>/', views.edit_well_picture, name='edit_well_picture'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

