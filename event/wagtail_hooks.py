from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from . import models


class EventAdmin(ModelAdmin):
    model = models.Event
    menu_label = 'Event'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', )
    list_filter = ('title', )
    search_fields = ('title', )


class EventGroup(ModelAdminGroup):
    menu_label = 'Event'
    menu_icon = 'date'
    items = (EventAdmin, )


modeladmin_register(EventGroup)
