from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from mezzanine.pages.models import Page, RichText

# The members of Page will be inherited by the Gallery model, such as
# title, slug, etc. In this example the Gallery model is essentially a
# container for GalleryImage instances.

NUM_ARTICLE_PAGES = 5

class TopicPage(Page, RichText):
    def get_article_pages(self):
        selected_pages = [page for page in self.displayed_pages.all()]
        if len(selected_pages) < NUM_ARTICLE_PAGES:
            pages = Page.objects.filter(parent=self)
            pages = sorted(pages, key=lambda page: page.publish_date, reverse=True)
            for page in pages:
                if page not in selected_pages:
                    selected_pages.append(page)
                    if selected_pages >= NUM_ARTICLE_PAGES:
                        break
        return selected_pages[:NUM_ARTICLE_PAGES]
    

    class Meta:
        verbose_name = _("Topic Page")
        verbose_name_plural = _("Topic Pages")

    notes = models.TextField("Notes")
    displayed_pages = models.ManyToManyField(Page,
        related_name='displayed_pages')

def main():
    print User.objects.all()

if __name__ == '__main__':
    from django.core.management import setup_environ
    from django.contrib.auth.models import User
    import settings
    setup_environ(settings)
    main()
