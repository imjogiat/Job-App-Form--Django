from django.shortcuts import render
from .forms import ApplicationForm
#add the model class that we defined/inherited in the models.py file
from .models import Form
from django.contrib import messages
#import the django library and classes from it to work with emails
#EmailMessage class already has built in SMTP and SSL
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(data=request.POST)
        print("application form object created")
    
        #cleaned_Data is a method in the parent class forms.Form
        #that adds the user input to a dictionary and cleans the format
        print(form.is_valid())
        print(f"\n\n{form.errors}\n\n")

        if form.is_valid():
            #code below creates variables to hold the form input date received
            #through the webpage then the form object
            print("reached form")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
        
            print(f"print log: extracted form data- {first_name}")

            #calling objects variable from within the Form class (Acutally inherited from models.Model)
            #then call create method within that variable object named objects
            #arguments are the column variable that we defined in the models.py file

            #creates the web form webpage with the fields of the form (from index.html) 
            # getting the form variables form variables receive form fields
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            
            #code to send email after above code where web form fields are instantiated 
            # sender email is specified in the 
            # settings.py under the project directory (not App directory)
            #Django looks at variables(acually constants) in settings.py
            #when an application is run
            message_body = f"A new job application was submitted. Thank you, {first_name} {last_name}"
            email_message = EmailMessage("Form submission confirmation",message_body, to=[email])
            email_message.send()
            
            #displays success message
            messages.success(request, "Form submitted successfully!")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
