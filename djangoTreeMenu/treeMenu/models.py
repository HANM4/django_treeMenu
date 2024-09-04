from django.db import models
from django.utils.text import slugify


class TreeMenu(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return self.name


class BranchMenu(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(TreeMenu,
                             on_delete=models.CASCADE,
                             related_name="branch")
    parent = models.ForeignKey("self",
                               on_delete=models.CASCADE,
                               related_name="children",
                               null=True,
                               blank=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = self.generate_unique_slug(self.name)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, name: str) -> str:
        slug = slugify(name)
        unique_slug = slug
        num = 1
        while BranchMenu.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def is_ancestor_of(self, branch: 'BranchMenu') -> bool:
        ancestor = branch.parent
        while ancestor is not None:
            if ancestor == self:
                return True
            ancestor = ancestor.parent
        return False

