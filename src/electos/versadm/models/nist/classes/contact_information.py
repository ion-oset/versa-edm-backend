from datetime import date, time
from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from versadm.models.nist.classes.annotated_string import AnnotatedString
from versadm.models.nist.classes.annotated_uri import AnnotatedUri
from versadm.models.nist.classes.intl_text import InternationalizedText
from versadm.models.nist.enums.nist import DayEnum
from versadm.models.nist.enums.type_tag import TypeTags
from versadm.models.nist.util import fieldname_alias


class Hours(BaseModel):
    obj_type: Literal[TypeTags.HoursTag] = Field(TypeTags.HoursTag)

    day: Optional[DayEnum]
    end_time: time
    label: Optional[str]
    start_time: time

    class Config:
        alias_generator = fieldname_alias


class LatLng(BaseModel):
    obj_type: Literal[TypeTags.LatLngTag] = Field(TypeTags.LatLngTag)

    label: Optional[str]
    latitude: float
    longitude: float
    source: Optional[str]

    class Config:
        alias_generator = fieldname_alias


class Schedule(BaseModel):
    obj_type: Literal[TypeTags.ScheduleTag] = Field(TypeTags.ScheduleTag)

    end_date: Optional[date]
    hours: List[Hours] = []
    is_only_by_appointment: bool = False
    is_or_by_appointment: bool = False
    is_subject_to_change: bool = False
    label: Optional[str]
    start_date: Optional[date]

    class Config:
        alias_generator = fieldname_alias


class ContactInformation(BaseModel):
    obj_type: Literal[TypeTags.ContactInformationTag] = Field(TypeTags.ContactInformationTag)

    address_line: List[str] = []
    directions: Optional[InternationalizedText]
    email: List[AnnotatedString] = []
    fax: List[AnnotatedString] = []
    label: Optional[str]
    lat_lng: Optional[LatLng]
    name: Optional[str]
    phone: List[AnnotatedString] = []
    schedule: List[Schedule] = []
    uri: List[AnnotatedUri] = []

    class Config:
        alias_generator = fieldname_alias
