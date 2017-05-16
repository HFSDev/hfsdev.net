from django.conf.urls import url
import lotteries.views

urlpatterns = [
    url(r'^$', lotteries.views.index, name="lotteries-views-index"),
    url(r'load_database/$', 
    	lotteries.views.load_data, name="lotteries-views-load_data"),
]
