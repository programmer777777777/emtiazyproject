from django.urls import path

from api.views import (AppDMoreWorksApiView, BusinessCardDMoreWorksApiView, BusinessDMoreWorksApiView, CarouselApiView, CommercialDMoreWorksApiView, ComputerDMoreWorksApiView, DigitalDMoreWorksApiView, GraphicsDMoreWorksApiView, LogoDMoreWorksApiView, WebHostingMoreWorksApiView, MediaDMoreWorksApiView, OthersMoreWorksApiView, StoreDMoreWorksApiView, WebDMoreWorksApiView, contacted_us_api_view, contact_us_info_api_view, page_contact_info_api_view, site_logo_api_view, WhyChoseApiView, SiteSectionApiView,
                       AbutUsMessageApiView, TeamApiView, ServiceApiView, StatisticApiView, WhatCustomersSayApiView,
                       OurPartnerApiView, MoreWorksApiView, LatestWorkApiView, page_about_info_api_view,
                       contact_info_api_view, site_intro_video_view)

urlpatterns = [
    path('sitelogo/', site_logo_api_view),
    path('carousels/', CarouselApiView.as_view()),
    path('sitesections/', SiteSectionApiView.as_view()),
    path('siteintovideo/', site_intro_video_view),
    path('contactinfo/', contact_info_api_view),
    path('contactusinfo/', contact_us_info_api_view),
    path('whychoses/', WhyChoseApiView.as_view()),
    path('aboutusmessage/', AbutUsMessageApiView.as_view()),
    path('teams/', TeamApiView.as_view()),
    path('services/', ServiceApiView.as_view()),
    path('moreworks/', MoreWorksApiView.as_view()),
    # TODO: These urls will be removed in the future.
    path('wdmoreworks/', WebDMoreWorksApiView.as_view()),
    path('admoreworks/', AppDMoreWorksApiView.as_view()),
    path('sdmoreworks/', StoreDMoreWorksApiView.as_view()),
    path('bidmoreworks/', BusinessDMoreWorksApiView.as_view()),
    path('whmoreworks/', WebHostingMoreWorksApiView.as_view()),
    path('gdmoreworks/', GraphicsDMoreWorksApiView.as_view()),
    path('dpdmoreworks/', DigitalDMoreWorksApiView.as_view()),
    path('cadmoreworks/', CommercialDMoreWorksApiView.as_view()),
    path('cdmoreworks/', ComputerDMoreWorksApiView.as_view()),
    path('mpdmoreworks/', MediaDMoreWorksApiView.as_view()),
    path('lddmoreworks/', LogoDMoreWorksApiView.as_view()),
    path('bcdmoreworks/', BusinessCardDMoreWorksApiView.as_view()),
    path('odmoreworks/', OthersMoreWorksApiView.as_view()),
    # End of TODO: These urls will be removed in the future.
    path('latestworks/', LatestWorkApiView.as_view()),
    path('statistics/', StatisticApiView.as_view()),
    path('whatcustomerssay/', WhatCustomersSayApiView.as_view()),
    path('ourpartner/', OurPartnerApiView.as_view()),
    path('pageaboutinfo/', page_about_info_api_view),
    path('pagecontactinfo/', page_contact_info_api_view),
    path('contactedus/', contacted_us_api_view),
]
