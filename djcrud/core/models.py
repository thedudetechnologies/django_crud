from datetime import datetime

import geoip2.database
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import models
from django.dispatch import receiver

from djcrud import settings

LOGIN = 'user_logged_in'
LOGOUT = 'user_logged_out'


class LoginLog(models.Model):
    login = models.DateTimeField(auto_now=True)
    logout = models.DateTimeField(auto_now=False, null=True)
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    browser_string = models.TextField()
    city = models.TextField(null=True)
    session = models.TextField()
    header_string = models.TextField()

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    try:
        ip = request.META.get('REMOTE_ADDR')
        city = ''
        browser_string = request.META['HTTP_USER_AGENT']
        geopath = settings.GEOIP_PATH + 'GeoLite2-City.mmdb'
        rander = geoip2.database.Reader(geopath)
        try:
            city = rander.city(ip)
        except Exception as e:
            print("City not Found IN Database", e)
        headers = request.headers

        session_exist = LoginLog.objects.filter(user=request.user, ip=ip, action=LOGIN)
        if not session_exist:
            LoginLog.objects.create(action=LOGIN, ip=ip, user=user,
                                    browser_string=browser_string,
                                    city=city,
                                    session=request.session,
                                    header_string=headers)
    except Exception as e:
        print("Exception Occurs While Login Log :", e)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    try:
        ip = request.META.get('REMOTE_ADDR')
        exist = LoginLog.objects.filter(user=user, ip=ip, action=LOGIN)

        exist.update(action=LOGOUT, logout=datetime.now())
        # LoginLog.objects.create(action='user_logged_out',ip=ip, user=user,
        #                         logout=logout,
        #                         browser_string=browser_string,
        #                         city=city,
        #                         session_id=session_id)
    except Exception as e:
        print("Exception Occurs :", e)
