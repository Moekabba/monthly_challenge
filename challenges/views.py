from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "aprill": "This when Absa mom cone",
    "may": "Baby due date month",
    "june": "this is June, stay focus",
    "july": "July is when you will be good at what you do",
    "aguest": "baby will be 3 months Insha Allah",
    "september": "get fit with Absa",
    "october": "get fit and stay fit",
    "november": "prepare to go see mom",
    "december": "Take break, reset and go see mom"

}


def monthly_challenge_by_number(request, month):
    forward_months = list(month_challenges_dict.keys())

    if month > len(forward_months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = forward_months[month - 1]
    redirect_path = reverse("month_cha", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)  # Redirect


# adding try catch to prevent failure if month is not in the dictionary
def monthly_challenges(request, month):
    try:
        challenge_txt = month_challenges_dict[month]
    except:
        return HttpResponseNotFound("this month is not supported in the dict")
    return HttpResponse(challenge_txt)
