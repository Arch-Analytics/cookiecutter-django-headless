from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from django.urls import include
from django.urls import path


router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# API urls for viewsets go here
# router.register("users", UserViewSet)

# Your Stuff: additional api routes go here (not using viewsets)
urlpatterns = [

]


app_name = "api"
urlpatterns += router.urls
