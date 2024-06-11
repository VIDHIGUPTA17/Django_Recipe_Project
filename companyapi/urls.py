"""
URL configuration for companyapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from .view import homepage
from vege.views import receipes,delete_receipe,update_receipe,login_page,register,logout_page
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',homepage),
    path('admin/', admin.site.urls),
    # path("api/v1",include('api.urls')),
    path("receipes/", receipes),
    path("delete-receipe/<id>/", delete_receipe, name="delete"),
    path("update-receipe/<id>/", update_receipe, name="update"),
    path("login_page/", login_page, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_page, name="logout")






]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()
