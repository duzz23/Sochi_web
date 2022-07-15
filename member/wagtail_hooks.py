from wagtail import hooks
from wagtail.contrib.modeladmin.mixins import ThumbnailMixin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from . import models


class MemberAdmin(ThumbnailMixin, ModelAdmin):
    model = models.Member
    menu_label = 'Member'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('admin_thumb', 'title')
    list_filter = ('speakers__event__title', )
    search_fields = ('title', 'speakers__event__title')
    thumb_image_field_name = "avatar"
    thumb_image_width = 100


@modeladmin_register
class MemberGroup(ModelAdminGroup):
    menu_label = 'Members'
    menu_icon = 'user'
    items = (MemberAdmin, )
