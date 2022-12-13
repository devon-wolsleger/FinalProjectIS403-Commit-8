from django.urls import path
from .views import IndexViewPage, LoginPage, TenantInfoPage, AddTennant


urlpatterns = [
    path("", IndexViewPage, name = "index"),
    path("tennants/", TenantInfoPage, name = "tennants"),
    path("contact/", LoginPage, name = "contact"),
    path("addTennant/", AddTennant, name = "addTennant")
]   