from django.urls import path
from . import views

urlpatterns = [
    path("january", views.janindex),
    path("february", views.febindex),
    path("march", views.marchindex),
    path("april", views.aprindex),
    path("may", views.mayindex),
    path("june", views.junindex),
    # path("<month>", views.monthly_challenges)
]
