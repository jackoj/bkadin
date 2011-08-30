from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import RichTextPageAdmin
from mezzanine.pages.models import Page, RichTextPage
from ecms.models import TopicPage, RichTextData

topic_page_extra_fieldsets = ((None, {"fields": ("notes",'displayed_pages',)}),)

class RichTextDataInlineAdmin(admin.TabularInline):
    model = RichTextData
    extra = 1
    max_num = 1

class ModifiedRichTextPageAdmin(RichTextPageAdmin):
    inlines = (RichTextDataInlineAdmin,)
    fieldsets = deepcopy(RichTextPageAdmin.fieldsets)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, ModifiedRichTextPageAdmin)

class TopicPageAdmin(RichTextPageAdmin):
    #inlines = (DisplayedPageInline,)
    fieldsets = deepcopy(RichTextPageAdmin.fieldsets) + topic_page_extra_fieldsets

admin.site.register(TopicPage, TopicPageAdmin)
