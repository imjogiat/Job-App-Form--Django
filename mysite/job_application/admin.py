from django.contrib import admin
#import the Form class defining the database model from the models file
from .models import Form

#Define a class that inherits from the ModelAdmin class in the admin module
#this will add funcitonality to the admin webpage when used as argument
#list_display (name it exactly), will be used by Django to name the columns
#that you see when you log in to admin portal
class FormAdmin(admin.ModelAdmin):
    #the variables defined below need to be named exactly

    list_display = ("first_name", "last_name", "email")
    
    #adds search fields to search for input form data
    search_fields = ("first_name", "last_name", "email")

    list_filter = ("date", "occupation")
    ordering = ("first_name",)

    readonly_fields = ("occupation",)


#call the register method from within the site object in the admin module
#admin module is a module within the django library
#argument is the Form class we defined as tbe database model
admin.site.register(Form, FormAdmin)


