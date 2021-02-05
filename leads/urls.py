from django.urls import path
from .views import (
    home, lead_detail, lead_create, lead_update, lead_delete,
    LeadDetailView, LeadCreateView, LeadDeleteView, LeadUpdateView, LeadListView,
)


app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead_list"),
    path("<int:pk>/", LeadDetailView.as_view(), name="lead_detail"),
    path("update/<int:pk>/", LeadUpdateView.as_view(), name="lead_update"),
    path("create/", LeadCreateView.as_view(), name="lead_create"),
    path("delete/<int:pk>/", LeadDeleteView.as_view(), name="lead_delete"),
]