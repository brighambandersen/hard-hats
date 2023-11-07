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
    survey_response1 = SurveyResponse()
    survey_response1.user = user_profile
    survey_response1.question_id = 1
    survey_response1.response_text = request.POST.get("salary_range")
    survey_response1.save()

    survey_response2 = SurveyResponse()
    survey_response2.user = user_profile
    survey_response2.question_id = 2
    survey_response2.response_text = request.POST.get("company_benefits")
    survey_response2.save()

    survey_response3 = SurveyResponse()
    survey_response3.user = user_profile
    survey_response3.question_id = 3
    survey_response3.response_text = request.POST.get("certifications")
    survey_response3.save()

    survey_response4 = SurveyResponse()
    survey_response4.user = user_profile
    survey_response4.question_id = 4
    survey_response4.response_text = request.POST.get("skills_and_experience")
    survey_response4.save()

    survey_response5 = SurveyResponse()
    survey_response5.user = user_profile
    survey_response5.question_id = 5
    survey_response5.response_text = request.POST.get("any_additions")
    survey_response5.save()

    return redirect(success)


def success(request):
    return render(request, "success.html")
