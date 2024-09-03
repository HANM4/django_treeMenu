from django.db import models
from django.utils.text import slugify


class TreeMenu(models.Model):
    name = models.CharField(max_length=100, blank=False)


class BranchMenu(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(TreeMenu, on_delete=models.CASCADE)
    parent = models.ForeignKey("self",
                               on_delete=models.CASCADE,
                               related_name="children",
                               null=True,
                               blank=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slag = self.generate_unique_slug(self.name)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, name):
        slug = slugify(name)
        unique_slug = slug
        num = 1
        while BranchMenu.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

