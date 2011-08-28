from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import RichTextPageAdmin
from mezzanine.pages.models import Page
from ecms.models import TopicPage

topic_page_extra_fieldsets = ((None, {"fields": ("notes",)}),)

#class DisplayedPageInline(admin.TabularInline):
##    list_display = ('id', )
##    fields = ('slug', )
#    model = Page

class TopicPageAdmin(RichTextPageAdmin):
    #inlines = (DisplayedPageInline,)
    fieldsets = deepcopy(RichTextPageAdmin.fieldsets) + topic_page_extra_fieldsets

admin.site.register(TopicPage, TopicPageAdmin)
