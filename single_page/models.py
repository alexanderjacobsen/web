import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from web import settings


class SingleImage(models.Model):
    image = models.ImageField(
        blank=False,
        upload_to="image_page/files/%Y/%m/%d",
    )
    slug = models.SlugField(
        blank=False,
        unique=True,
        primary_key=True,
        verbose_name='url',
    )

    def __str__(self):
        return self.slug + f' - {self.filename}'

    def get_absolute_url(self):
        return reverse("single_image", kwargs={'slug': self.slug})

    @property
    def filename(self):
        return os.path.basename(self.image.name)


class SinglePage(models.Model):
    content = RichTextUploadingField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        blank=False,
        unique=True,
        primary_key=True,
        verbose_name='url',
    )

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("single_page", kwargs={'slug': self.slug})

    def delete(self, using=None, keep_parents=False):
        for file in self.files.all():
            file.delete()
        super().delete(using, keep_parents)


class SingleFile(models.Model):
    file = models.FileField(upload_to="single_page/files/%Y/%m/%d")
    page = models.ForeignKey(SinglePage, on_delete=models.CASCADE, related_name='files')

    def delete(self, using=None, keep_parents=False):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(using, keep_parents)

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.filename} - {self.page}'
