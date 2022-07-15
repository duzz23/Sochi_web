from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail import blocks
from event.models import Event, Partner
from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class CallToActionWithSocial(blocks.StructBlock):
    call_to_action_label = blocks.CharBlock()
    call_to_action_link = blocks.URLBlock()

    class Meta:
        template = 'home/blocks/call_to_action.html'
        icon = 'hello'


class HeaderMenu(blocks.StructBlock):
    menu = blocks.CharBlock()
    links = blocks.URLBlock()


    class Meta:
        template = 'home/_header_menu.html'
        icon = 'Header_Menu'


class Hello(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock()
    call_to_action_label = blocks.CharBlock()
    call_to_action_link = blocks.URLBlock()

    class Meta:
        template = 'home/blocks/hello.html'
        icon = 'hello'


class EventCarousel(blocks.StaticBlock):
    class Meta:
        template = 'event/сarousel.html'
        icon = 'user'

    def get_context(self, value, context=None):
        result = super().get_context(value, context)
        result.update({
            "events": Event.objects.live().order_by('-date_event')
        })

        return result


class HomePage(Page):
    body = StreamField([
        ('HeaderMenu', HeaderMenu()),
        ('hello', Hello()),
        ('CallToActionWithSocial', CallToActionWithSocial()),
        ('html', blocks.RawHTMLBlock()),
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('carousel', EventCarousel()),

    ], use_json_field=True, null=True)


    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]



class MenuItem(Orderable):
    slug = models.CharField(max_length=64, null=True)
    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
        help_text='Choose a page to link to for the Call to Action',

    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("slug"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),

    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class SocialLink(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    icon_svg = models.TextField()

    class Meta:
        verbose_name = "Наша социальная сеть"
        verbose_name_plural = "Наши социальные сети"

    def __str__(self):
        return self.title


@register_snippet
class PartnerLink(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    icon_svg = models.TextField()

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"

    def __str__(self):
        return self.title


@register_snippet
class Menu(ClusterableModel):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    class Meta:
        verbose_name = "Раздел заголовка HEADER"
        verbose_name_plural = "Разделы заголовка HEADER"

    def __str__(self):
        return self.title


class PrivacyPolicy(Page):
    intro = RichTextField(blank=True)
    parent_page_types = ["home.HomePage"]
    template = "home/privacy-policy.html"

