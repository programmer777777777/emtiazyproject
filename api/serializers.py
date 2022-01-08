from django.db import models
from rest_framework import serializers

from emtiazy.models import ContactUsInfo, PageContactInfo, SiteLogo, Carousel, Team, CarouselAction, WhyChose, SiteSection, MessagePoint, AboutUsMessage, \
    Service, Statistic, WhatCustomersSay, OurPartner, MoreWorks, LatestWork, PageAboutPoint, PageAboutInfo, ContactInfo, WorkCollection


class SiteLogoSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField('get_logo')

    class Meta:
        model = SiteLogo
        fields = ['name', 'logo']

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url
        return None


class CarouselActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselAction
        fields = ['label', 'button', 'action', 'outline']


class CarouselSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    actions = CarouselActionSerializer(source='carouselaction_set', many=True)

    class Meta:
        model = Carousel
        fields = ['id', 'image', 'title', 'description', 'actions']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class SiteSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSection
        fields = ['id', 'section_type', 'title', 'subtitle', 'description']


class WhyChoseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = WhyChose
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class MessagePointSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = MessagePoint
        fields = ['id', 'label', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class AboutUsMessageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    points = MessagePointSerializer(source='messagepoint_set', many=True)

    class Meta:
        model = AboutUsMessage
        fields = ['id', 'label', 'description', 'image', 'points']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class TeamSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')

    class Meta:
        model = Team
        fields = ['id', 'name', 'job', 'description', 'profile', 'facebook', 'twitter', 'instagram', 'whatsapp',
                  'phone']

    def get_profile(self, obj):
        if obj.profile:
            return obj.profile.url
        return None


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'description',
                  'content', 'image', 'created_at', 'updated_at']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class MoreWorksSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    work_collection = serializers.CharField(
        source='get_work_collection_display', read_only=True)

    class Meta:
        model = MoreWorks
        fields = ['id', 'work_collection', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class LatestWorkSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = LatestWork
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id', 'icon', 'count', 'title',
                  'description', 'theme', 'text_as_theme']


class WhatCustomersSaySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = WhatCustomersSay
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class OurPartnerSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField('get_logo')

    class Meta:
        model = OurPartner
        fields = ['id', 'name', 'logo']

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url
        return None


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'phone', 'email', 'facebook', 'twitter', 'instagram',
                  'whatsapp', 'open_from_time', 'open_to_time']


class PageAboutPointSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = PageAboutPoint
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class PageAboutInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    points = PageAboutPointSerializer(source='pageaboutpoint_set', many=True)

    class Meta:
        model = PageAboutInfo
        fields = ['id', 'title', 'description', 'image', 'points']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class ContactUsInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = ContactUsInfo
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None


class PageContactInfoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = PageContactInfo
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
