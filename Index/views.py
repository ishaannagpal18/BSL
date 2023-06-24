from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'index.html')

def general_listing(request):
    if request.method == 'POST':
        
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        

        print(company_name)
        print(company_address)
        print(contact_email)
        print(contact_phone)
 

       
        
        

       
        try:
            auth_token = str(uuid.uuid4())
            general_lsiting_obj = General_Listing.objects.create(auth_token = auth_token, company_name = company_name,company_address=company_address,contact_email=contact_email,contact_phone=contact_phone)
            messages.success(request, 'You Have Successfully Registered!')
            # html_template = render_to_string('register_email.html', {'company_name':company_name, 'business_type':business_type,'kind_of_products':kind_of_products,'company_website':company_website,'company_address':company_address,'information':information,'name_of_person':name_of_person,'contact_email':contact_email,'contact_phone':contact_phone})
            # recipient_list = [contact_email]
            # message = EmailMessage('Welcome To BSL ASSOCIATION', html_template,
            #                        'BSL ASSOCIATION <info@bslassociation.com>', [contact_email])
            # message.content_subtype = 'html'
            # message.send()
            general_lsiting_obj.save()
            
            

            return HttpResponseRedirect(reverse('home'))


        except Exception as e:
            print(e)



    return render(request, 'general_listing.html')

def empaneled_vendor(request):
    if request.method == 'POST' and request.FILES['user_image'] and request.FILES['company_profile'] and request.FILES['small_video']:
        company_name = request.POST.get('company_name')
        user_image = request.FILES.get('user_image')
        company_profile = request.FILES.get('company_profile')
        small_video = request.FILES.get('small_video')
        business_type = request.POST.get('business_type')
        kind_of_products = request.POST.get('kind_of_products')
        company_website = request.POST.get('company_website')
        company_address = request.POST.get('company_address')
        information = request.POST.get('information')
        name_of_person = request.POST.get('name_of_person')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        

        print(company_name)
        print(user_image)
        print(company_profile)
        print(small_video)
        print(business_type)
        print(kind_of_products)
        print(company_website)
        print(company_address)
        print(information)
        print(name_of_person)
        print(contact_email)
        print(contact_phone)
 

       
        
        

       
        try:
            auth_token = str(uuid.uuid4())
            empaneled_vendor_obj = Empaneled_Vendor.objects.create(auth_token = auth_token,user_image=user_image,company_profile=company_profile,small_video=small_video, company_name = company_name,business_type=business_type, kind_of_products=kind_of_products, company_website=company_website,company_address=company_address,information=information,name_of_person=name_of_person,contact_email=contact_email,contact_phone=contact_phone)
            messages.success(request, 'You Have Successfully Registered!')
            # html_template = render_to_string('register_email.html', {'company_name':company_name, 'business_type':business_type,'kind_of_products':kind_of_products,'company_website':company_website,'company_address':company_address,'information':information,'name_of_person':name_of_person,'contact_email':contact_email,'contact_phone':contact_phone})
            # recipient_list = [contact_email]
            # message = EmailMessage('Welcome To SAVTHEARTH', html_template,
            #                        'BSL ASSOCIATION <info@bslassociation.com>', [contact_email])
            # message.content_subtype = 'html'
            # message.send()
            empaneled_vendor_obj.save()
            
            

            return HttpResponseRedirect(reverse('home'))


        except Exception as e:
            print(e)



    return render(request, 'empaneled_vendor.html')

def auditorium(request):
    return render(request, 'auditorium.html')

def global_summit(request):
    return render(request, 'global_summit.html')

def about(request):
    return render(request, 'about.html')

def membership(request):
    return render(request, 'membership.html')

def members(request):
    return render(request, 'members.html')

def knit_event(request):
    return render(request, 'knit_event.html')

def powerplay1_event(request):
    return render(request, 'powerplay1_event.html')

def powerplay2_event(request):
    return render(request, 'powerplay2_event.html')

def award(request):
    return render(request, 'award.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')


