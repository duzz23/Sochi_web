from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmodelchooser import register_model_chooser


@register_model_chooser
class Member(models.Model):
    title = models.CharField(max_length=64)
    avatar = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("title"),
        ImageChooserPanel("avatar"),
    ]


    def __str__(self):
        return self.title
