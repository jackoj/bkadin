
from django.conf.urls.defaults import *
from django.contrib import admin

from mezzanine.conf import settings
from mezzanine.utils.urls import static_urls
from mezzanine.core.views import direct_to_template

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality to
# the project's homepage.
urlpatterns = patterns("mezzanine.generic.views",
    url("^admin_keywords_submit/$", "admin_keywords_submit",
        name="admin_keywords_submit"),
    url("^rating/$", "rating", name="rating"),
)

if getattr(settings, "PACKAGE_NAME_FILEBROWSER") in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        ("^admin/filebrowser/", include("%s.urls" %
                                        settings.PACKAGE_NAME_FILEBROWSER)),
        static_urls(settings.FILEBROWSER_URL_FILEBROWSER_MEDIA.strip("/"),
                    settings.FILEBROWSER_PATH_FILEBROWSER_MEDIA),
    )

urlpatterns += patterns("",
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
#    url("^(?P<slug>.*)/$", "ecms.views.topic_page", name="topic_page"),
    ("^", include("mezzanine.urls")),
)

# Adds ``MEDIA_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"

