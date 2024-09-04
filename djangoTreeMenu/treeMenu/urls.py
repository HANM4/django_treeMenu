from django.urls import path
from .views import BranchMenuDetailView


urlpatterns = [
    path("<slug:slug>/",
         BranchMenuDetailView.as_view(),
         name="branch_menu")
]