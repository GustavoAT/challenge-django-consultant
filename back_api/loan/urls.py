from django.urls import include, path
from rest_framework import routers
from loan import views

router = routers.DefaultRouter()
router.register(r'fields', views.LoanRequestFieldViewSet)

urlpatterns = [
    path('', include(router.urls)),
]