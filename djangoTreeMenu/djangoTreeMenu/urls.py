from django.contrib import admin
from django.urls import path
from treeMenu.urls import urlpatterns as tree_menu_urlpatterns
from .views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index_page')
] + tree_menu_urlpatterns


