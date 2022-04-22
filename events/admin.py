from django.contrib import admin
from .models import Event, Speaker, Talk, Host, Sponsor, EventSponsor, TalkSpeaker


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime', 'host']


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


class TalkSpeakerInline(admin.TabularInline):
    model = TalkSpeaker
    extra = 0


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    inlines = [TalkSpeakerInline]


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    pass


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(EventSponsor)
class EventSponsorAdmin(admin.ModelAdmin):
    list_display = ['event', 'sponsor']
