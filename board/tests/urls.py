from django.conf.urls import url, include


urlpatterns = [
    url(r'^messages/', include('board.urls')),
]
