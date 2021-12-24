from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from .models import Keller


@plugin_pool.register_plugin
class KleberPlugin(CMSPluginBase):
    model = Keller
    render_template = "mypage.html"
    cache = False
