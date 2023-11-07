from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

from .models import UserProfile, SurveyResponse


def index(request):
    return render(request, "index.html")


def apply(request):
    if request.method != "POST":
        return HttpResponseBadRequest("This endpoint only allows POST")

    # Build user profile and add to DB
    user_profile = UserProfile()
    user_profile.first_name = request.POST.get("first_name")
    user_profile.last_name = request.POST.get("last_name")
    user_profile.phone_number = request.POST.get("phone_number")
    user_profile.email = request.POST.get("email")
    user_profile.address = request.POST.get("address")
    user_profile.profile_picture_url = request.POST.get("profile_picture_url")
    user_profile.resume_url = request.POST.get("resume_url")
    user_profile.save()

    # Build survey responses and add to DB
    survey_response = SurveyResponse()
    survey_response.user = user_profile
    survey_response.question_id = 1
    survey_response.response_text = request.POST.get("target_salary")
    survey_response.save()

    return redirect(success)


def success(request):
    return render(request, "success.html")
