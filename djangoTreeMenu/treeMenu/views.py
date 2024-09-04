from django.views.generic import DetailView
from .models import BranchMenu
from typing import Dict, Any


class BranchMenuDetailView(DetailView):
    template_name = "index.html"
    model = BranchMenu

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_slug'] = self.kwargs.get('slug', '')
        return context
