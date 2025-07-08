from django.shortcuts import render
from .forms import ApplicationForm


def index(request):
    if request.method == "POST":
        form = ApplicationForm(data=request.POST)
        print("application form object created")
    
        #cleaned_Data is a method in the parent class forms.Form
        #that adds the user input to a dictionary and cleans the format
        print(form.is_valid())
        print(f"\n\n{form.errors}\n\n")

        if form.is_valid():
            print("reached form")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
        
            print(f"print log: extracted form data- {first_name}")

    return render(request, "index.html")


