"""splitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # the following are all of the urls for the user models
    path('api/user/profile/', include('users.api.urls.ProfileUrls')),
    path('api/user/detail/', include('users.api.urls.DetailUrls')),
    path('api/user/friends/', include('users.api.urls.FriendUrls')),
    path('api/users/', include('users.api.urls.UserUrls')),
    # the following are all of the urls for the group models
    path('api/member/user/', include('groups.api.urls.MemberUserUrls')),
    path('api/member/group/', include('groups.api.urls.MemberGroupUrls')),
    path('api/groups/', include('groups.api.urls.GroupsUrls')),
]
