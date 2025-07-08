from django.shortcuts import render
from .forms import ApplicationForm


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print("application form object created")
        print(f"Application form data {form.first_name} {form.last_name}")
        #cleaned_Data is a method in the parent class forms.Form
        #that adds the user input to a dictionary and cleans the format
        print(form.is_valid())
        if form.is_valid():
            print("reached form")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email_addr = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
        
        print(f"{first_name}")

    return render(request, "index.html")


