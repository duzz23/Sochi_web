from django import template
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from wagtail.models import Site

from event.models import BlogCategoryOrganizers
from home.models import SocialLink, PartnerLink, Menu

register = template.Library()

"""Tag for Social"""
@register.simple_tag
def social_menu(template):
    context = {
        "objects": SocialLink.objects.all()
    }
    return render_to_string(template, context)


"""Tag for Partner"""
@register.simple_tag
def partner_list(template):
    context = {
        "objects": PartnerLink.objects.all()
    }
    return render_to_string(template, context)


"""Tag for Menu headers"""
@register.simple_tag()
def menu_tags(slug):
    return Menu.objects.get(slug=slug)


@register.simple_tag()
def categories_list(slug):
    return BlogCategoryOrganizers.objects.get(slug=slug)

#
#
# @register.simple_tag(takes_context=True)
# def pageurl(context, page, fallback=None):
#     """
#     Outputs a page's URL as relative (/foo/bar/) if it's within the same site as the
#     current page, or absolute (http://example.com/foo/bar/) if not.
#     If kwargs contains a fallback view name and page is None, the fallback view url will be returned.
#     """
#     if page is None and fallback:
#         return resolve_url(fallback)
#
#     if not hasattr(page, "relative_url"):
#         raise ValueError("pageurl tag expected a Page object, got %r" % page)
#
#     try:
#         site = Site.find_for_request(context["request"])
#         current_site = site
#     except KeyError:
#         # request not available in the current context; fall back on page.url
#         return page.url
#
#     if current_site is None:
#         # request does not correspond to a recognised site; fall back on page.url
#         return page.url
#
#     # Pass page.relative_url the request object, which may contain a cached copy of
#     # Site.get_site_root_paths()
#     # This avoids page.relative_url having to make a database/cache fetch for this list
#     # each time it's called.
#     return page.relative_url(current_site, request=context.get("request"))