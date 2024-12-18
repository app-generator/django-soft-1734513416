# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Test1(models.Model):

    #__Test1_FIELDS__
    test1 = models.CharField(max_length=255, null=True, blank=True)
    test2 = models.CharField(max_length=255, null=True, blank=True)

    #__Test1_FIELDS__END

    class Meta:
        verbose_name        = _("Test1")
        verbose_name_plural = _("Test1")



#__MODELS__END
