from django.conf.urls import url
from .views import LugaresApi
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', LugaresApi.as_view(), name="lugares_endpoint"),
]