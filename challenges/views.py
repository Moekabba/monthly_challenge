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

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_txt = None
    if month == "january":
        challenge_txt = "This january, 1st month"
    elif month == "february":
        challenge_txt = "This is February, your birthday month"
    else:
        return HttpResponseNotFound(" month not found")
    return HttpResponse(challenge_txt)
