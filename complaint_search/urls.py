from django.conf.urls import url
from django.views.generic.base import RedirectView

import complaint_search.views


urlpatterns = [
    url(
        r'^_suggest_company',
        complaint_search.views.suggest_company,
        name="suggest_company"
    ),
    url(
        r'^_suggest_zip',
        complaint_search.views.suggest_zip,
        name="suggest_zip"
    ),
    url(r'^_suggest', complaint_search.views.suggest, name="suggest"),
    url(
        r'^(?P<id>[0-9]+)$', complaint_search.views.document, name="complaint"
    ),
    url(r'^$', complaint_search.views.search, name="search"),
    url(r'^geo/states', complaint_search.views.states,
        name="states"),
    url(r'^geo',
        RedirectView.as_view(url='/geo/states'), name="geo"),
]
