import datetime
import uuid

from ninja import Schema
from pydantic import UUID4
from django.contrib.auth import get_user_model
from django.db import models

User=get_user_model()



class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str

class LabelOut(Schema):
    id: UUID4
    name: str

class notifications(Schema):
    id: UUID4
    title: str
    sender: str
    description: str
    time: datetime.time


class update_notifications(Schema):
    title: str
    sender: str
    description: str
    image: str
    time: datetime.time


class notificationsOut(Schema):
    id: UUID4
    title: str
    sender: str
    description: str
    image: str
    time: datetime.time

############################################

class OpinionUser(Schema):
    id:UUID4
    email:str


class Service_opinionIn(Schema):
    # id: UUID4
    user: OpinionUser
    rating: float
    description: str
    time: datetime.time


class Service_opinionOUT(Schema):
    # id :UUID4
    rating: float
    user_id: UUID4
    service_id:UUID4
    description: str
    time: datetime.time


class Update_Service_opinion(Schema):
    #user: User
    rating: float
    description: str
    time: datetime.time


########################################


class Image_S(Schema):
    image:str
    service_id:UUID4


class ImageOut_S(Schema):
    id: UUID4
    image:str

class update_Images_S(Schema):
    image:str


#########################################
class Services(Schema):
    #id: UUID4
    name: str
    description: str
    time: datetime.time
    background_image:str
    price: float
    label_id:UUID4
    latitude: str
    longitude: str
    location: str
    is_feature : bool



class ServiceOut(Schema):
    id: UUID4
    label: LabelOut
    background_image: str
    name: str
    latitude: str
    longitude: str
    location: str
    description: str
    time: datetime.time
    Service_images: list[ImageOut_S]
    price: float
    is_feature : bool

    ServiceOpinions: list[Service_opinionIn]


class update_Services(Schema):
    #id: UUID4
    name: str
    description: str
    time: datetime.time
    background_image: str
    price: float
    latitude: str
    longitude: str
    location: str
    is_feature : bool



########################################


class Image_C(Schema):
    image:str
    center_id:UUID4


class ImageOut_C(Schema):
    id:UUID4
    image:str


class update_Images_C(Schema):
    image:str



#####################################


class Center_opinionIn(Schema):
    id: UUID4
    rating: float
    user: OpinionUser
    description: str
    time: datetime.time


class Center_opinionOUT(Schema):
    #id: UUID4
    user_id:UUID4
    description: str
    rating: float

    time: datetime.time
    center_id:UUID4


class Update_Center_opinion(Schema):
    #user: User
    rating: float
    description: str
    time: datetime.time









###################################

class Center(Schema):
    #id: UUID4
    name: str
    description: str
    location: str
    image: str
    open_days: datetime.date
    close_days: datetime.date
    open_time: datetime.time
    close_time: datetime.time
    is_feature : bool

    latitude: str
    longitude: str
    location: str




class CenterOut(Schema):
    id: UUID4
    name: str
    description: str

    services: list[ServiceOut]
    Center_images: list[ImageOut_C]
    CenterOpinions:list[Center_opinionIn]
    image: str
    open_time:  datetime.time
    is_feature : bool
    location: str

    latitude: str
    longitude: str
    location: str

    close_time: datetime.time
    open_days: datetime.date
    close_days: datetime.date


class update_Center(Schema):
    name: str
    description: str
    location: str
    is_feature : bool

    latitude: str
    longitude: str
    location: str

    image: str
    open_time: datetime.time
    close_time:datetime.time
    open_days: datetime.date
    close_days:datetime.date


##################################################

class Advertising(Schema):
    #id: UUID4
    title: str
    description: str
    url: str

    image: str
    # center_id: UUID4






class AdvertisingOut(Schema):
    id: UUID4
    title: str
    url: str
    description: str
    image: str
    # center: CenterOut


class update_Advertising(Schema):
    image: str
    url: str

    title: str
    description: str



####################################
class News(Schema):
    id: UUID4
    image: str
    title: str
    description: str
    # time: str


class NewsOut(Schema):
    id: UUID4
    image: str
    title: str
    description: str

    # time: str


class update_News(Schema):
    title: str
    description: str
    image: str



############################

"""
class Center_opinionIn(Schema):
    id: UUID4
    # rating: float
    user: OpinionUser
    description: str
    time: datetime.time


class Center_opinionOUT(Schema):
    #id: UUID4
    user_id:UUID4
    description: str
    time: datetime.time
    center_id:UUID4"""





class Reservation(Schema):
    id: UUID4
    user: OpinionUser
    service: ServiceOut
    title: str
    time: datetime.time
    is_active: bool



class ReservationOut(Schema):
    user_id:UUID4
    service_id: UUID4
    title: str
    time: datetime.time
    is_active: bool





class update_Reservation(Schema):
    title: str
    time: datetime.time
    is_active: bool


############################

class FavList(Schema):
    id: UUID4
    user: OpinionUser
    service: ServiceOut

    created: datetime.datetime
    updated: datetime.datetime


class FavCreate(Schema):
    user: OpinionUser
    service: ServiceOut
    updated: datetime.datetime




class FavShow(Schema):
    user_id:UUID4
    service_id: UUID4
    created: datetime.datetime
    updated: datetime.datetime




class UpdateFav(Schema):
    user_id: UUID4
    service_id: UUID4
    updated: datetime.datetime


