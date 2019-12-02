from apps.users.models import VerifyCode
from extra_apps import xadmin
from extra_apps.xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "暮雪生鲜后台"
    site_footer = "mxshop"


class VerifycodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode, VerifycodeAdmin)
xadmin.site.register(views)