from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# forms
class EmployeeForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)


def index(request):
    return render(request, "index.html")


# FIXME below, should remove
@csrf_exempt
def apply(request):
    return redirect(success)
    # first_name = request.POST["first_name"] # .get("first_name")
    # last_name = request.POST["last_name"]

    # return HttpResponse(first_name + " " + last_name)
    # if request.method != "POST":
    #     return HttpResponseBadRequest("This endpoint only allows POST")

    # context = {"first_name": ""}
    # print("validating")
    # form = EmployeeForm(request.POST)
    # if form.is_valid():
    #     print("is valid")
    #     # Add user to DB
    #     first_name = form.cleaned_data["first_name"]

    # # return HttpResponse("apply")
    # # context = {"first_name": first_name}
    # return redirect(request, "success.html", {"first_name": first_name})
    # return HttpResponseRedirect(reverse(""))


def success(request):
    return render(request, "success.html")
