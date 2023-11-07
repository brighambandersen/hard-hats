from django.contrib import admin
from app.models import UserProfile, SurveyQuestion, SurveyResponse

admin.site.register(UserProfile)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyResponse)
