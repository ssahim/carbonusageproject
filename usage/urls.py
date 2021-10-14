from django.urls import path
from .views import (
    UsageTypeView,
    UsageTypeCreateView,
    UsageTypeUpdateView,
    UsageTypeDeleteView,

    UsageCreateView,
    UsageUpdateView,
    UsageDeleteView,
)

urlpatterns = [
    path('type/', UsageTypeView.as_view(), name='usagetype'),
    path('type/update/<int:id>', UsageTypeUpdateView.as_view(),
         name='usagetypeupdate'),
    path('type/delete/<int:id>', UsageTypeDeleteView.as_view(),
         name='usagetypedelete'),

    path('', UsageCreateView.as_view(), name='usage'),
    path('update/<int:pk>/', UsageUpdateView.as_view(), name='usageupdate'),
    path('delete/<int:pk>/', UsageDeleteView.as_view(), name='usagedelete'),
]
