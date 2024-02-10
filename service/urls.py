from django.urls import path

from .views import (ReferralCodeCreateAPIView,
                    ReferralCodeDeleteAPIView,
                    ReferralCodeSearchAPIView,
                    ReferralCodeUpdateAPIView,
                    ReferrerCreateAPIView,
                    ReferrerSearchAPIView)


app_name = 'referal_service'
urlpatterns = [
    path('codes/create/', ReferralCodeCreateAPIView.as_view(), name='create'),
    path('codes/update/<int:pk>/', ReferralCodeUpdateAPIView.as_view(), name='update'),
    path('codes/delete/<int:pk>/', ReferralCodeDeleteAPIView.as_view(), name='delete'),
    path('codes/search/', ReferralCodeSearchAPIView.as_view(), name='search'),
    path('referrers/attach/', ReferrerCreateAPIView.as_view(), name='referrer_attach'),
    path('referrers/search/', ReferrerSearchAPIView.as_view(), name='referrer_search')
]