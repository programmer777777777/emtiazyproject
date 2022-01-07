from django.urls import path

from api.views import (CarouselApiView, contact_us_info_api_view, page_contact_info_api_view, site_logo_api_view, WhyChoseApiView, SiteSectionApiView,
                       AbutUsMessageApiView, TeamApiView, ServiceApiView, StatisticApiView, WhatCustomersSayApiView,
                       OurPartnerApiView, MoreWorksApiView, LatestWorkApiView, page_about_info_api_view,
                       contact_info_api_view)

urlpatterns = [
    path('sitelogo/', site_logo_api_view),
    path('carousels/', CarouselApiView.as_view()),
    path('sitesections/', SiteSectionApiView.as_view()),
    path('contactinfo/', contact_info_api_view),
    path('contactusinfo/', contact_us_info_api_view),
    path('whychoses/', WhyChoseApiView.as_view()),
    path('aboutusmessage/', AbutUsMessageApiView.as_view()),
    path('teams/', TeamApiView.as_view()),
    path('services/', ServiceApiView.as_view()),
    path('moreworks/', MoreWorksApiView.as_view()),
    path('latestworks/', LatestWorkApiView.as_view()),
    path('statistics/', StatisticApiView.as_view()),
    path('whatcustomerssay/', WhatCustomersSayApiView.as_view()),
    path('ourpartner/', OurPartnerApiView.as_view()),
    path('pageaboutinfo/', page_about_info_api_view),
    path('pagecontactinfo/', page_contact_info_api_view),
]
