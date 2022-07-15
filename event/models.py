from datetime import datetime
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import InlinePanel, FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtailmodelchooser.edit_handlers import ModelChooserPanel
from wagtailmodelchooser.widgets import AdminModelChooser
from member.models import Member
from django.db import models



class EventIndex(Page):
    parent_page_types = ["home.HomePage"]
    template = "home/home_page.html"


class Event(Page):
    title_event = models.CharField(max_length=50, null=True)
    teaser = models.CharField(max_length=50, null=True)
    content_event = models.CharField(max_length=850, null=True)
    image_event = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    date_event = models.DateTimeField(verbose_name="date_event", blank=True, null=True)
    location_event = models.CharField(max_length=250, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("title_event"),
        FieldPanel("teaser"),
        FieldPanel("content_event"),
        ImageChooserPanel("image_event"),
        FieldPanel("date_event"),
        FieldPanel("location_event"),
        InlinePanel("speakers", label="Speakers"),
        InlinePanel("partners", label="Partners"),

    ]
    parent_page_types = ["LocalEvent"]
    template = "event/event.html"

    def time_zone(self):
        return self.date_event.date() > datetime.now().date()


class Speakers(Orderable):
    class Meta:
        unique_together = (
            ("event", "member")
        )

    title = models.CharField(max_length=64, null=True)
    event = ParentalKey("Event", on_delete=models.PROTECT, related_name="speakers")
    member = models.ForeignKey("member.Member", on_delete=models.PROTECT, related_name="speakers")
    teaser = models.TextField(null=True)
    panels = [
        ModelChooserPanel('member', widget=AdminModelChooser(Member)),
        FieldPanel("title"),
        FieldPanel("teaser"),
    ]

    def __str__(self):
        return f"{self.event} / {self.member}"




class Partner(Orderable):
    class Meta:
        unique_together = (
            ("event", "member")
        )

    title = models.CharField(max_length=64, null=True)
    event = ParentalKey("Event", on_delete=models.PROTECT, related_name="partners")
    member = models.ForeignKey("member.Member", on_delete=models.PROTECT, related_name="partners")
    teaser = models.TextField(null=True)

    panels = [
        ModelChooserPanel('member', widget=AdminModelChooser(Member)),
        FieldPanel("title"),
        FieldPanel("teaser"),

    ]

    def __str__(self):
        return f"{self.event} / {self.member}"


#eventlist
class LocalEvent(Page):
    intro = RichTextField(blank=True)

    @property
    def blogs(self):
        #events
        blogs = Event.objects.live().order_by('-date_event').descendant_of(self)
        return blogs

    def get_context(self, request, **kwargs):
        blogs = self.blogs
        context = super(LocalEvent, self).get_context(request)
        context['blogs'] = blogs

        return context

    template = "event/events.html"


@register_snippet
class BlogCategoryOrganizers(models.Model):

    name = models.CharField(max_length=50, null=True)
    slag = models.SlugField(
        verbose_name="slag",
        null=True,
        allow_unicode=True,
        max_length=50,
        help_text='Выбрать категорию для Организатора',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slag"),

    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организатор и  Контрибьютор"
        verbose_name_plural = "Организаторы и  Контрибьюторы"
        ordering = ["name"]


class Organizers(Page):
    name = models.CharField(max_length=50)
    telegram = models.URLField()
    description = models.CharField(max_length=150)
#    """подключения к блоку в котором создали подгруппы"""
    categories = ParentalManyToManyField("event.BlogCategoryOrganizers", blank=True, related_name="orgs")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    content_panels = Page.content_panels + [

        FieldPanel("name"),
        FieldPanel("telegram"),
        FieldPanel("description"),
        ImageChooserPanel("image"),
#        """панель выбора группы"""
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
        ]
    parent_page_types = ["OrganizersList"]



class OrganizersList(Page):
    intro = RichTextField(blank=True)

    @property
    def blogs(self):
        # events
        blogs = Organizers.objects.live().descendant_of(self)
        return blogs

    @property
    def organizers(self):
        return Organizers.objects.filter(categories__slag="Organizer")

    @property
    def contributors(self):
        return Organizers.objects.filter(categories__slag="Contributor")

    def get_context(self, request, **kwargs):
        blogs = self.blogs
        context = super(OrganizersList, self).get_context(request)
        context['blogs'] = blogs

        return context

    parent_page_types = ["home.HomePage"]
    template = "home/organizers.html"


