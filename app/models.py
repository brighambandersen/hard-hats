from django.db import models


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    profile_picture_url = models.URLField(max_length=200, blank=True, null=True)
    resume_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"[{self.user_id}] UserProfile: {self.first_name} {self.last_name}"


class SurveyQuestion(models.Model):
    question_id = models.TextField(primary_key=True)
    question_text = models.TextField()

    def __str__(self):
        return f'[{self.question_id}] SurveyQuestion: "{self.question_text}"'


class SurveyResponse(models.Model):
    response_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return f'[{self.response_id}] SurveyResponse: {self.user.first_name}  to "{self.question.question_text}"'
