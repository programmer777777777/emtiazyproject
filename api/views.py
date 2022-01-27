from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F
from api.serializers import (ContactUsInfoSerializer, ContactedUsSerializer, PageContactInfoSerializer, SiteIntroVideoSerializer, SiteLogoSerializer, CarouselSerializer, WhyChoseSerializer, TeamSerializer,
                             SiteSectionSerializer, AboutUsMessageSerializer, ServiceSerializer, StatisticSerializer,
                             WhatCustomersSaySerializer, OurPartnerSerializer, MoreWorksSerializer,
                             LatestWorkSerializer, PageAboutInfoSerializer, ContactInfoSerializer)


@api_view(['GET'])
def site_logo_api_view(request):
    queryset = SiteLogoSerializer.Meta.model.objects.first()
    serializer = SiteLogoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CarouselApiView(generics.ListAPIView):
    serializer_class = CarouselSerializer
    queryset = CarouselSerializer.Meta.model.objects.filter(enabled=True)


@api_view(['GET'])
def site_intro_video_view(request):
    queryset = SiteIntroVideoSerializer.Meta.model.objects.first()
    serializer = SiteIntroVideoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SiteSectionApiView(generics.ListAPIView):
    serializer_class = SiteSectionSerializer
    queryset = SiteSectionSerializer.Meta.model.objects.filter(enabled=True)


class WhyChoseApiView(generics.ListAPIView):
    serializer_class = WhyChoseSerializer
    queryset = WhyChoseSerializer.Meta.model.objects.filter(enabled=True)


class AbutUsMessageApiView(generics.ListAPIView):
    serializer_class = AboutUsMessageSerializer
    queryset = AboutUsMessageSerializer.Meta.model.objects.filter(enabled=True)


class TeamApiView(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = TeamSerializer.Meta.model.objects.filter(enabled=True)


class ServiceApiView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceSerializer.Meta.model.objects.filter(enabled=True)


class MoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True)

# TODO: These apis will be removed in the future.


class WebDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='web_development')


class AppDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='apps_development')


class StoreDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='stores_design')


class BusinessDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='businessـidentityـdesign')


class WebHostingMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='web_hosting')


class GraphicsDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='graphics_design')


class DigitalDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='digitalـphotoـdesign')


class CommercialDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='commercialـadvertisingـdesign')


class ComputerDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='computerـsystemsـdesign')


class MediaDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='media_post_design')


class LogoDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='logo_design')


class BusinessCardDMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='business_card_design')


class OthersMoreWorksApiView(generics.ListAPIView):
    serializer_class = MoreWorksSerializer
    queryset = MoreWorksSerializer.Meta.model.objects.filter(
        enabled=True, work_collection='others')


# End of TODO: These apis will be removed in the future.


class LatestWorkApiView(generics.ListAPIView):
    serializer_class = LatestWorkSerializer
    queryset = LatestWorkSerializer.Meta.model.objects.filter(enabled=True)


class StatisticApiView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = StatisticSerializer.Meta.model.objects.filter(enabled=True)


class WhatCustomersSayApiView(generics.ListAPIView):
    serializer_class = WhatCustomersSaySerializer
    queryset = WhatCustomersSaySerializer.Meta.model.objects.filter(
        enabled=True)


class OurPartnerApiView(generics.ListAPIView):
    serializer_class = OurPartnerSerializer
    queryset = OurPartnerSerializer.Meta.model.objects.filter(enabled=True)


@api_view(['GET'])
def page_about_info_api_view(request):
    queryset = PageAboutInfoSerializer.Meta.model.objects.first()
    serializer = PageAboutInfoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def contact_info_api_view(request):
    queryset = ContactInfoSerializer.Meta.model.objects.first()
    serializer = ContactInfoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def contact_us_info_api_view(request):
    queryset = ContactUsInfoSerializer.Meta.model.objects.first()
    serializer = ContactUsInfoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def page_contact_info_api_view(request):
    queryset = PageContactInfoSerializer.Meta.model.objects.first()
    serializer = PageContactInfoSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def contacted_us_api_view(request):
    print(request.data)
    serializer = ContactedUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 0, 'message': '.لقد وصلتنا رسالتك ونقدر وقتك معنا وسنتواصل معك في أقرب وقت ممكن'}, status=status.HTTP_201_CREATED)
    return Response({'status': 1, 'message': '.يرجى التأكد من بيانات الإدخال الخاصة بك'}, status=status.HTTP_400_BAD_REQUEST)
