from django.conf.urls import url
import lotteries.views

urlpatterns = [
    url(r'^$', lotteries.views.index, name="lotteries-views-index"),
    url(r'loader/$', lotteries.views.load_data, name="lotteries-views-load_data"),
]
