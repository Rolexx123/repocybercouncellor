from django.urls import path
from .views import *

urlpatterns = [

    path('viewcouncellor/',ViewCouncellor.as_view(),name='View1234'),
    path('feedback/',Viewfeedback.as_view(),name='feedback1234'),
    path('rating/',Viewrating.as_view(),name='rating1234'),
    path('complaint/',Viewcomplaint.as_view(),name='complaint1234'),
    

]
