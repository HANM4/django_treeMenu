from django import template
from ..models import TreeMenu, BranchMenu
from typing import Optional
from django.db.models import QuerySet


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: dict,
              menu_name: str,
              current_slug: Optional[str]) -> Optional[str]:
    try:
        menu = TreeMenu.objects.get(name=menu_name)
        branches = menu.branch.filter(parent=None)
        if current_slug:
            current_branch = BranchMenu.objects.get(slug=current_slug)
        else:
            current_branch = None
        return render_menu(context, branches, current_branch)
    except TreeMenu.DoesNotExist:
        return "Menu not found"
    except BranchMenu.DoesNotExist:
        return "Current item not found"


def render_menu(context: dict,
                branches: QuerySet[BranchMenu],
                current_branch: Optional[BranchMenu], level: int = 0) -> str:
    result = '<ul>'
    for branch in branches:
        is_active = branch == current_branch
        result += (f'<li>'
                   f'<a class="{"active" if is_active else ""}'
                   f'"href="/{branch.slug}">{branch.name}</a>')
        if is_active or (current_branch is not None and
                         branch.is_ancestor_of(current_branch)) or level < 1:
            children = branch.children.all()
            if children:
                result += render_menu(context, children, current_branch, level + 1)
        result += '</li>'
    result += '</ul>'
    return result
