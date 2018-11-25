"""sheepsbridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from home import views as home_views
from services import views as services_views
from contact import views as contact_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^about/$', home_views.about, name='about'),
    url(r'^kennels/$', services_views.kennels, name='kennels'),
    url(r'^grooming/$', services_views.grooming, name='grooming'),
    url(r'^find/$', contact_views.find, name='find'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^captcha/', include('captcha.urls')),
]

# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
#   ]+urlpatterns
