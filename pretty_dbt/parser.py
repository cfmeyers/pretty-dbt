from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class Event:
    model_name: str
    event_type: str
    duration_seconds: float


def parse_event_type(event_starting: str) -> str:
    if 'OK' in event_starting:
        return 'OK'
    else:
        return event_starting.split(' ')[-1]


def parse_model_name(event_ending: str) -> str:
    raw_model_name = event_ending.split(' ')[0]
    return raw_model_name.strip('.')


def parse_duration_seconds(event_ending: str) -> Optional[float]:
    inside_brackets = event_ending.split('[')[1].strip(']')
    if 'SUCCESS' in inside_brackets:
        return float(re.findall(r'([0-9.]+)s', inside_brackets)[0])
    else:
        return None


def parse_event(msg: str) -> Event:
    starting, ending = msg.split(' table model ')
    event_type = parse_event_type(starting)
    model_name = parse_model_name(ending)
    duration_seconds = parse_duration_seconds(ending)
    return Event(
        model_name=model_name, event_type=event_type, duration_seconds=duration_seconds
    )
