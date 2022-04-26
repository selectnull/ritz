from ninja import Router
from typing import List
from .schema import EventOut, TalkOut, SpeakerOut
from .models import Event, Talk, Speaker


router = Router()


@router.get('/events', response=List[EventOut])
def get_events(request):
    return Event.objects.all()


@router.get('/talks', response=List[TalkOut])
def get_talks(request):
    return Talk.objects.all().prefetch_related('speakers')


@router.get('/speakers', response=List[SpeakerOut])
def get_speakers(request):
    return Speaker.objects.all()
