from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    about_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)

    class Meta:
        db_table = 'event_speakers'

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'event_sponsors'

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    class Meta:
        db_table = 'event_hosts'

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    host = models.ForeignKey(Host, related_name='events', on_delete=models.CASCADE)

    class Meta:
        db_table = 'event_events'

    def __str__(self):
        return self.title


class Talk(models.Model):
    event = models.ForeignKey(Event, related_name='talks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'event_talks'

    def __str__(self):
        return self.title


class TalkSpeaker(models.Model):
    talk = models.ForeignKey(Talk, related_name='speakers', on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, related_name='talks', on_delete=models.PROTECT)

    class Meta:
        db_table = 'talk_speakers'

    def __str__(self):
        return f'{self.talk} @ {self.speaker}'


class EventSponsor(models.Model):
    event = models.ForeignKey(Event, related_name='sponsors', on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, related_name='events', on_delete=models.CASCADE)

    class Meta:
        db_table = 'event_event_sponsors'

    def __str__(self):
        return f'{self.event} {self.sponsor}'
