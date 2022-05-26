from django.contrib import admin
from django.urls import path

from jamil_bot.views import createjamilbot, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view())
]
