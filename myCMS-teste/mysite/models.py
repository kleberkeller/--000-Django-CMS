from cms.models.pluginmodel import CMSPlugin

from django.db import models


class Keller(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')
    body = models.CharField(max_length=1000, default='MyPage')
