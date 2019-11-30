from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging
import geoip2.database
from djcrud import settings
# Create your views here.

log = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login/')
def home(request):
    geopath = settings.GEOIP_PATH + 'GeoLite2-City.mmdb'
    rander = geoip2.database.Reader(geopath)
    user = request.user
    print("Session ", request.session)
    ip = request.META.get('REMOTE_ADDR')
    print("Login Using IP:",ip)
    print("Browser Using :",request.META['HTTP_USER_AGENT'])
    print("Header :",request.headers)
    try:

        city = rander.city(ip)

        print("City :",city.city.name)
        # print("City :",g.city(ip)['city'])
    except Exception as e:
        print("Address Not Found",e)
    content = {}
    content['user'] = user


    return render(request, "index.html",content)
