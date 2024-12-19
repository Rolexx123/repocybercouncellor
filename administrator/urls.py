from django.urls import path
from .views import *

urlpatterns = [

    path('viewcouncellor/',VerifyCouncellor.as_view(),name='View1234'),
    path('feedback/',Viewfeedback.as_view(),name='feedback1234'),
    path('rating/',Viewrating.as_view(),name='rating1234'),
    path('complaint/',Viewcomplaint.as_view(),name='complaint1234'),
    path('adminhomepage/',adminhomepage.as_view(),name='adminhomepage'),
    path('login/',login.as_view(),name='login'), 
    path('ratingandfeedback/',ratingandfeedback.as_view(),name='ratingandfeedback'), 
    path('replaybox/',replaybox.as_view(),name='replaybox'), 
    path('verify_user/',verify_user.as_view(),name='verify_user'),
    path('chatwithuser/',chatwithuser.as_view(),name='chatwithuser'),
    path('councellorregister/',councellorregister.as_view(),name='councellorregister'),
    path('counsellorHomepage/',counsellorHomepage.as_view(),name='counsellorHomepage'),
    path('requestfromuser/',requestfromuser.as_view(),name='requestfromuser'),
    path('uploadmotivationalthought/',uploadmotivationalthoughts.as_view(),name='uploadmotivationalthought'),
    path('uploadmotivationalVideos/',uploadmotivationalVideos.as_view(),name='uploadmotivationalVideos'),
    path('videocallwithuser/',videocallwithuser.as_view(),name='videocallwithuser'),
    path('applicationandrating/',applicationandrating.as_view(),name='applicationandrating'),
    path('Accept_Councellor/<int:C_id>',Accept_Councellor.as_view(),name='Accept_Councellor'),
    path('Reject_Councellor/<int:id>',Reject_Councellor.as_view(),name='Reject_Councellor'),

]