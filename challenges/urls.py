from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.janindex),
    # path("february", views.febindex),
    # path("march", views.marchindex),
    # path("april", views.aprindex),
    # path("may", views.mayindex),
    # path("june", views.junindex),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month_cha") #name added to use with reverse function # str: stringfy 
]
