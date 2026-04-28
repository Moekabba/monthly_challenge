from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def janindex(request):
#     return HttpResponse("This january, 1st month")


# def febindex(request):
#     return HttpResponse("This is February, your birthday month")

# def marchindex(request):
#     return HttpResponse("This march for march madnes")

# def aprindex(request):
#     return HttpResponse("this the current month")

# def mayindex(request):
#     return HttpResponse("Baby due on this month")

# def junindex(request):
#     return HttpResponse("Summer time!!Every massive haffi come along Go fi your sun tan inna di summer sun If you a bleacher, go back home ")

month_challenges_dict = {
    "january": "This january, 1st month from your dict",
    "februray": "this February, your birthday month",
    "march": "this is Absa's birthday",
    "Aprill": "This when Absa mom cone",
    "May": "Baby due date month",
    "June": "this is June, stay focus",
    "July": "July is when you will be good at what you do",
    "Aguest": "baby will be 3 months Insha Allah",
    "September": "get fit with Absa",
    "October": "get fit and stay fit",
    "November": "prepare to go see mom",
    "December": "Take break, reset and go see mom"

}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_txt = month_challenges_dict
  
    return HttpResponse(challenge_txt)
