from django.db import models

# Create your models here.

class Pet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey('auth.User', related_name='pets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')

    PET_STATUS = (
        ('p', 'Placed'),
        ('a', 'Approved'),
        ('d', 'Delivered'),
    )
    status = models.CharField(
        max_length=1,
        choices=PET_STATUS,
        blank=True,
    )
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=False, default='')
    created_by = models.ForeignKey('auth.User', related_name='tags', on_delete=models.CASCADE)
    pets = models.ManyToManyField('Pet', related_name='tags', blank=True)

    class Meta:
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=False, default='')
    created_by = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name