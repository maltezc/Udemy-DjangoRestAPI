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
from .views import (
                StatusAPIView,
                StatusAPIDetailView,
                )


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()), #shift to id because of lookup field # <pk> is built in method for giving view id
]

'''
Start with:
    /api/status/ --> List
    /api/status/create --> create
    /api/status/12/ --> detail
    /api/status/12/update --> Update
    /api/status/12/delete --> Delete


**ENDING WITH THIS ONE** images complicates others. makes this one simpler
End with:
    /api/status/ --> List --> CRUD 
    /api/status/1/ --> Detail --> CRUD
    
Final:

    /api/status/ --> CRUD & LS(List and Search)

'''


