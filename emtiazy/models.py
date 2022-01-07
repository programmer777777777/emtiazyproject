from django.core.validators import FileExtensionValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from emtiazy.validators import FacebookValidator, TwitterValidator, InstagramValidator, WhatsappValidator, PhoneValidator


def site_logo_upload(instance, filename):
    return f"logo/{instance.name}.{filename.split('.')[-1]}"


class SiteLogo(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('Site Title'))
    logo = models.ImageField(
        verbose_name=_('Site Logo'),
        upload_to=site_logo_upload,
        validators=[FileExtensionValidator(
            allowed_extensions=['svg', 'png', 'jpg'])],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Site Logo')


class Carousel(models.Model):
    image = models.ImageField(
        verbose_name=_('Carousel Image'),
        upload_to='carousel/',
    )
    title = models.CharField(max_length=50, verbose_name=_(
        "Title"), blank=True, null=True)
    description = models.TextField(
        verbose_name=_("Description"),
        validators=[MaxLengthValidator(500)],
        blank=True,
        null=True
    )
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"))

    def __str__(self):
        return self.title if self.title else "Emtiazy"

    class Meta:
        verbose_name_plural = _('Carousel')


class CarouselAction(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    label = models.CharField(max_length=10, verbose_name=_('Label'))
    BUTTON_CHOICES = [
        ('error', _('Red')),
        ('info', _('Sky Blue')),
        ('primary', _('Blue')),
        ('secondary', _('Purple')),
        ('warning', _('Yellow')),
    ]
    button = models.CharField(
        max_length=20,
        verbose_name=_('Button'),
        choices=BUTTON_CHOICES,
        default='primary'
    )
    action = models.URLField(verbose_name=_('Action'))
    outline = models.BooleanField(default=False, verbose_name=_('Outline'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = _('Carousel Action')


class SiteSection(models.Model):
    TYPE_CHOICES = [('why_chose', _('Why Chose')), ('aboutus', _('About Us')), ('services', _('Services')),
                    ('latestwork', _('Latest Works')),
                    ('morework', _('More Works')),
                    ('whatcustomersay', _('What Customer Say')
                     ), ('ourteam', _('Our Teams')),
                    ('contact', _('Contact')), ('ourpartner', _('Our Partner'))]
    section_type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, verbose_name=_('Section Type'))
    title = models.CharField(max_length=20, verbose_name=_('Title'))
    subtitle = models.CharField(max_length=50, verbose_name=_(
        'Subtitle'), blank=True, null=True)
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(400)],
        blank=True,
        null=True
    )
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Site Section')


class WhyChose(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(110)],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='whychose/',
                              verbose_name=_('Descriptive Image'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Why Chose')


class AboutUsMessage(models.Model):
    label = models.CharField(max_length=30, verbose_name=_('Label'))
    description = models.TextField(validators=[MaxLengthValidator(110)], verbose_name=_('Description'), blank=True,
                                   null=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='aboutus/')
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = _('About Us Message')


class MessagePoint(models.Model):
    aboutus_message = models.ForeignKey(
        AboutUsMessage, on_delete=models.CASCADE)
    label = models.CharField(max_length=15, verbose_name=_('Label'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.CharField(max_length=50, verbose_name=_(
        'Description'), blank=True, null=True)
    image = models.ImageField(verbose_name=_(
        'Image'), upload_to='message_point/')

    def __str__(self):
        return self.label


class Team(models.Model):
    name = models.CharField(
        max_length=255, verbose_name=_('Name'), unique=True)
    job = models.CharField(max_length=30, verbose_name=_('Job'))
    description = models.CharField(max_length=400, verbose_name=_(
        'Description'), blank=True, null=True)
    profile = models.ImageField(verbose_name=_(
        'Profile'), upload_to='teams/', blank=True, null=True)
    facebook = models.CharField(max_length=100, verbose_name=_('Facebook Link'), unique=True, blank=True, null=True,
                                validators=[FacebookValidator()])
    twitter = models.CharField(max_length=100, verbose_name=_('Twitter Link'), unique=True, blank=True, null=True,
                               validators=[TwitterValidator()])
    instagram = models.CharField(max_length=100, verbose_name=_('Instagram Link'), unique=True, blank=True, null=True,
                                 validators=[InstagramValidator()])
    whatsapp = models.CharField(max_length=100, verbose_name=_('Whatsapp Link'), unique=True, blank=True, null=True,
                                validators=[WhatsappValidator()])
    phone = models.CharField(max_length=12, verbose_name=_('Phone'), unique=True, blank=True, null=True,
                             validators=[PhoneValidator()])
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Teams')


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, verbose_name=_('Url'),
                            help_text=_('Url will be generated automatically'))
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(200)],
        blank=True,
        null=True
    )
    content = models.TextField(
        blank=True, null=True, verbose_name=_('Content'))
    image = models.ImageField(upload_to='services/',
                              verbose_name=_('Image'), blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated At'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Service')


class WorkCollection(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Work Collection')


class MoreWorks(models.Model):
    # work_collection = models.ForeignKey(WorkCollection, on_delete=models.PROTECT)
    WORK_COLLECTION_CHOICES = [('graphics', _('Graphics')), ('web_design', _(
        'Web Design')), ('mobile_development', _('Mobile Development')), ('other', _('Other'))]
    work_collection = models.CharField(
        max_length=50, choices=WORK_COLLECTION_CHOICES, verbose_name=_('Work Collection'))
    title = models.CharField(max_length=50, verbose_name=_(
        "Title"), blank=True, null=True)
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(1000)],
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to='more_works/'
    )
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"))

    class Meta:
        verbose_name_plural = _('More Works')


class LatestWork(models.Model):
    title = models.CharField(max_length=50, verbose_name=_(
        "Title"), blank=True, null=True)
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(300)],
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to='latest_works/'
    )
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"))

    class Meta:
        verbose_name_plural = _('Our Latest Works')


class Statistic(models.Model):
    icon = models.CharField(max_length=20, verbose_name=_('Icon'))
    count = models.PositiveSmallIntegerField(verbose_name=_('Count'))
    title = models.CharField(max_length=20, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'),
        validators=[MaxLengthValidator(150)],
        blank=True,
        null=True
    )
    THEME_CHOICES = [('primary', _('Blue')), ('secondary', _('Purple')), ('success', _('Green')),
                     ('danger', _('Red')), ('warning', _('Yellow')
                                            ), ('info', _('Sky Blue')), ('light', _('White')),
                     ('dark', _('Dark'))]
    theme = models.CharField(max_length=20, verbose_name=_(
        'Theme'), choices=THEME_CHOICES, default='info')
    text_as_theme = models.BooleanField(
        default=False, verbose_name=_('Text as Theme'))
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Statistic')


class WhatCustomersSay(models.Model):
    title = models.CharField(max_length=50, verbose_name=_(
        'Title'), blank=True, null=True)
    description = models.CharField(max_length=500, verbose_name=_(
        "Description"), blank=True, null=True)
    image = models.ImageField(verbose_name=_(
        'Image'), upload_to='what_people_say/', )
    enabled = models.BooleanField(verbose_name=_('Enabled'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('What Customers Say')


class OurPartner(models.Model):
    name = models.CharField(max_length=100, verbose_name=_(
        'Name'), unique=True, blank=True, null=True)
    logo = models.ImageField(verbose_name=_(
        'Logo'), upload_to='our_partner/', )
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))

    class Meta:
        verbose_name_plural = _('Our Partner')


class ContactInfo(models.Model):
    address = models.CharField(max_length=100, verbose_name=_(
        'Address'), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_(
        'Phone'), blank=True, null=True)
    email = models.EmailField(
        max_length=100, verbose_name=_('Email'), blank=True, null=True)
    facebook = models.URLField(max_length=100, verbose_name=_(
        'Facebook'), blank=True, null=True)
    twitter = models.URLField(max_length=100, verbose_name=_(
        'Twitter'), blank=True, null=True)
    instagram = models.URLField(max_length=100, verbose_name=_(
        'Instagram'), blank=True, null=True)
    whatsapp = models.URLField(max_length=100, verbose_name=_(
        'Whatsapp'), blank=True, null=True)
    open_from_time = models.TimeField(
        verbose_name=_('From Time'), blank=True, null=True)
    open_to_time = models.TimeField(
        verbose_name=_('To Time'), blank=True, null=True)

    def __str__(self):
        return self.address if self.address else ''

    class Meta:
        verbose_name_plural = _('Contact Info')


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=12, verbose_name=_('Phone'))
    subject = models.CharField(max_length=50, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_(
        'Message'), validators=[MaxLengthValidator(400)])
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Contact Us')


class Subscriber(models.Model):
    contact = models.CharField(max_length=30, verbose_name=_('Contact'))

    def __str__(self):
        return self.contact

    class Meta:
        verbose_name_plural = _('Subscribers')


class PageAboutInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_(
        'Description'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='page_about/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Page About Info')


class PageAboutPoint(models.Model):
    about_page = models.ForeignKey(
        PageAboutInfo, on_delete=models.CASCADE, verbose_name=_('Page About'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_(
        'Description'), blank=True, null=True)
    image = models.ImageField(verbose_name=_(
        'Image'), upload_to='page_about_point/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Page About Point')


class ContactUsInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='contact_us_info/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Contact Us Info')


class PageContactInfo(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='page_contact_info/',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Page Contact Info')
