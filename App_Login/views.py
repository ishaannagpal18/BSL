from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth import login as authlogin
from django.conf import settings
from django.core.mail import send_mail

from App_Login.models import *


from django.contrib import messages
import razorpay
import uuid
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email_id')
        contact_no = request.POST.get('contact_no')
        interested = request.POST.get('interested')
        company = request.POST.get('company')
        designation = request.POST.get('designation')
        city = request.POST.get('city')
        username = email
        

        print(name)
        print(email)
        print(contact_no)
        print(interested)
        print(company)
        print(designation)
        print(city)
 

       
        
        

       
        try:
        #     if User.objects.filter(username = username).first():
        #         messages.success(request, 'Username is taken.')
        #         return HttpResponseRedirect(reverse('App_Login:register'))

        #     if User.objects.filter(email = email).first():
        #         messages.success(request, 'Email is taken.')
        #         return HttpResponseRedirect(reverse('App_Login:register'))


        #     user_obj = User(username = username , email = email)
        #     user_obj.set_password(password)
        #     user_obj.save()
            
            auth_token = str(uuid.uuid4())
            register_obj = Register.objects.create(auth_token = auth_token, name = name,contact_no=contact_no, email_id=email, interested=interested,company=company,designation=designation,city=city)
            # html_template = render_to_string('register_email.html', {'name':name, 'username':username,'password':password})
            # recipient_list = [email]
            # message = EmailMessage('NIT Hamirpur Alumni Association Registration Confirmation', html_template,
            #                        'VRAKSH <info@vraksh.co>', [email])
            # message.content_subtype = 'html'
            # message.send()
            register_obj.save()
            messages.success(request, 'You Have Successfully Registered!')
            # messages.success(request, 'Registered Sucessfully')
            # html_template = render_to_string('register_email.html', {'name':name, 'username':username,'password':password})
            # recipient_list = [email]
            # message = EmailMessage('Welcome To SAVTHEARTH', html_template,
            #                        'SAVTHEARTH <info@savthearth.org>', [email])
            # message.content_subtype = 'html'
            # message.send()
            

            return HttpResponseRedirect(reverse('home'))


        except Exception as e:
            print(e)



    return render(request, 'App_Login/register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user_obj = User.objects.filter(username = username).first()

#         if user_obj is None:
#             messages.success(request, 'User not found.')
#             return HttpResponseRedirect(reverse('App_Login:login'))


       

#         user = authenticate(username = username , password = password)
#         if user is None:
#             messages.success(request, 'Wrong password.')
#             return HttpResponseRedirect(reverse('App_Login:login'))

#         authlogin(request , user)
       
#         register_obj = Register.objects.filter(user = user).first()
#         if register_obj.is_verified:
#             return HttpResponseRedirect(reverse('payment_successful'))
#         else:
#             return HttpResponseRedirect(reverse('App_Login:payment'))


#     return render(request , 'App_Login/login.html')

# @login_required
# def logout(request):
#     logout(request)
#     messages.warning(request,"You Are Logged Out!")
#     return HttpResponseRedirect(reverse('home'))





