from django.urls import path
from psyapp import views

urlpatterns = [
    path('pi',views.pi,name='pi'),
    path('ptanc',views.ptanc,name='ptanc'),
    path('preg',views.preg,name='preg'),
    path('plog',views.plog,name='plog'),
    path('pntlog',views.pntlog,name='pntlog'),
    path('pregdata',views.pregdata,name='pregdata'),
    path('plogdata',views.plogdata,name='plogdata'),
    path('plogout',views.plogout,name='plogout'),
    path('paprs',views.paprs,name='paprs'),
    path('apnreq',views.apnreq,name='apnreq'),
    path('apna',views.apna,name='apna'),
    path('apnapr/<int:id>',views.apnapr,name='apnapr'),
    path('apnd',views.apnd,name='apnd'),
    path('apndec/<int:id>',views.apndec,name='apndec'),
]
