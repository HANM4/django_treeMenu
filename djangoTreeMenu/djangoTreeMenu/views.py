from django.views.generic.base import TemplateView
from treeMenu.models import TreeMenu


class IndexTemplateView(TemplateView):
    template_name = 'index.html'
