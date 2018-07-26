"""cfeapi URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin


from updates.views import (
        json_example_view,
        JsonCBV,
        JsonCBV2,
        SerializedDetailView,
        SerializedListView
        )



# if django 2.0, this looks different V
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls')),
    url(r'^api/status/', include('status.api.urls')),
    url(r'^api/updates/', include('updates.api.urls')),  # api/updates/ --> api/updates/1/ --> detail
]
