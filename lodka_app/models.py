from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def parents(self):
        parents = []
        instance = self

        while instance.parent:
            instance = instance.parent
            parents.append(instance)

        return parents

    def siblings(self):
        siblings = Category.objects.filter(parent=self.parent).exclude(id=self.id)
        return siblings

    def __str__(self):
        return self.name
