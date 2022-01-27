from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from emtiazy.models import (PageContactInfo, SiteIntroVideo, ContactUsInfo, SiteLogo, Carousel, CarouselAction, WhyChose, Team, ContactInfo, SiteSection, MessagePoint,
                           AboutUsMessage, Service, Statistic, WhatCustomersSay, OurPartner, MoreWorks, LatestWork, PageAboutPoint,
                           PageAboutInfo, ContactedUs, Subscriber)

admin.site.site_header = 'MY-TECH'


class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ['name']

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super().save_model(request, obj, form, change)


admin.site.register(SiteLogo, SiteLogoAdmin)


class SiteIntroVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'heading']

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super().save_model(request, obj, form, change)


admin.site.register(SiteIntroVideo, SiteIntroVideoAdmin)


class CarouseActionInline(admin.TabularInline):
    model = CarouselAction
    extra = 1
    max_num = 3


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'enabled']
    inlines = [CarouseActionInline]


admin.site.register(Carousel, CarouselAdmin)


class SiteSectionAdmin(admin.ModelAdmin):
    list_display = ['section_type', 'title',
                    'subtitle', 'description', 'enabled']

    def save_model(self, request, obj, form, change):
        sections = SiteSection.objects.all()
        for section in sections:
            if section.section_type == obj.section_type:
                obj.id = section.id
        return super(SiteSectionAdmin, self).save_model(request, obj, form, change)


admin.site.register(SiteSection, SiteSectionAdmin)


class WhyChoseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'enabled']


admin.site.register(WhyChose, WhyChoseAdmin)


class MessagePointInline(admin.TabularInline):
    model = MessagePoint
    extra = 1


class AboutUsMessageAdmin(SummernoteModelAdmin):
    list_display = ['label', 'description', 'enabled']
    summernote_fields = ['description']
    inlines = [MessagePointInline]

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super(AboutUsMessageAdmin, self).save_model(request, obj, form, change)


admin.site.register(AboutUsMessage, AboutUsMessageAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'description', 'enabled']


admin.site.register(Team, TeamAdmin)


class ServiceAdmin(SummernoteModelAdmin):
    list_display = ['title', 'description', 'enabled']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ['content']


admin.site.register(Service, ServiceAdmin)


# class WorkCollectionAdmin(admin.ModelAdmin):
#     list_display = ['name', 'enabled']


# admin.site.register(WorkCollection, WorkCollectionAdmin)


class MoreWorksAdmin(SummernoteModelAdmin):
    list_display = ['title', 'work_collection', 'enabled']
    sumernote_fields = ['description']


admin.site.register(MoreWorks, MoreWorksAdmin)


class LatestWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'enabled']


admin.site.register(LatestWork, LatestWorkAdmin)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ['title', 'count']
    readonly_fields = ['icon']


admin.site.register(Statistic, StatisticAdmin)


class WhatCustomersSayAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'enabled']


admin.site.register(WhatCustomersSay, WhatCustomersSayAdmin)


class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'enabled']


admin.site.register(OurPartner, OurPartnerAdmin)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email']

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super(ContactInfoAdmin, self).save_model(request, obj, form, change)


admin.site.register(ContactInfo, ContactInfoAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactedUs, ContactUsAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['contact']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Subscriber, SubscriberAdmin)


class PageAboutPointInline(admin.TabularInline):
    model = PageAboutPoint
    extra = 1


class PageAboutInfoAdmin(SummernoteModelAdmin):
    list_display = ['title']
    summernote_fields = ['description']
    inlines = [PageAboutPointInline]

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super(PageAboutInfoAdmin, self).save_model(request, obj, form, change)


admin.site.register(PageAboutInfo, PageAboutInfoAdmin)


class PageContactInfoAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(PageContactInfo, PageContactInfoAdmin)


class ContactUsInfoAdmin(admin.ModelAdmin):
    list_display = ['title']

    def save_model(self, request, obj, form, change):
        obj.id = 1
        return super(ContactUsInfoAdmin, self).save_model(request, obj, form, change)


admin.site.register(ContactUsInfo, ContactUsInfoAdmin)
