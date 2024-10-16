from django.contrib import admin
from django.urls import path

from app.views import hey_you, how_old, order_total

urlpatterns = [
    path("hey/<name>", hey_you),
    path("age-in/<int:end>/<int:birthyear>", how_old),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", order_total),
    path('admin/', admin.site.urls),
]
