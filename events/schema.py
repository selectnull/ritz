from typing import List
from ninja.orm import ModelSchema
from .models import Host, Speaker, Event, Talk, TalkSpeaker


class HostOut(ModelSchema):
    class Config:
        model = Host
        model_fields = '__all__'


class EventOut(ModelSchema):
    host: HostOut

    class Config:
        model = Event
        model_fields = '__all__'


class SpeakerOut(ModelSchema):
    class Config:
        model = Speaker
        model_fields = '__all__'


class TalkSpeakerOut(ModelSchema):
    speaker: SpeakerOut
    class Config:
        model = TalkSpeaker
        model_fields = '__all__'


class TalkOut(ModelSchema):
    event: EventOut
    speakers: List[TalkSpeakerOut]

    class Config:
        model = Talk
        model_fields = '__all__'
