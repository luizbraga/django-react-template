from django.contrib.admin import AdminSite
from django.contrib.admin import register as _register
from functools import partial


class DefaultAdminSite(AdminSite):
    site_title = 'project_name'
    site_header = 'project_name'
    index_title = 'Modules'


admin = DefaultAdminSite(name='project_name')
register = partial(_register, site=admin)
