from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser_safe.fields import FileBrowseField

# Create your models here.
from mezzanine.pages.models import Page, RichText, RichTextPage

# The members of Page will be inherited by the Gallery model, such as
# title, slug, etc. In this example the Gallery model is essentially a
# container for GalleryImage instances.

NUM_ARTICLE_PAGES = 4

class RichTextData(models.Model):
    # Chosen to be TextField to get the admin to look proper. Otherwise,
    # they should ide
    header = models.TextField(_("header"),
                              max_length=512,
                              blank=True,
                              )
    homepage_header = models.TextField(_("homepage_header"),
                                       max_length=512,
                                       blank=True,
                                       )
    main_image = FileBrowseField(
            blank=True,
            null=True,
            max_length=100,
            )
    rich_text_page = models.ForeignKey(RichTextPage, editable=False)

class TopicPage(Page, RichText):
    def get_article_pages(self):
        selected_pages = [page for page in self.displayed_pages.all()]
        pages = Page.objects.filter(parent=self)
        pages = sorted(pages, key=lambda page: page._order)
        return pages if len(pages) < NUM_ARTICLE_PAGES else pages[:NUM_ARTICLE_PAGES]

    class Meta:
        verbose_name = _("Topic Page")
        verbose_name_plural = _("Topic Pages")

    notes = models.TextField("Notes")
    displayed_pages = models.ManyToManyField(Page,
        related_name='displayed_pages',
        blank=True,
        )

def main():
    print User.objects.all()

if __name__ == '__main__':
    from django.core.management import setup_environ
    from django.contrib.auth.models import User
    import settings
    setup_environ(settings)
    main()
