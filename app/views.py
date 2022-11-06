from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Employee


def index(request):
    return render(request, "index.html")


def apply(request):
    if request.method != "POST":
        return HttpResponseBadRequest("This endpoint only allows POST")
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")

    employee = Employee()
    employee.first_name = first_name
    employee.save()
    return redirect(success)
    # first_name = request.POST["first_name"] # .get("first_name")
    # last_name = request.POST["last_name"]

    # return HttpResponse(first_name + " " + last_name)

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
