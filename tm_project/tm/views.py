from django.core import serializers
from models import *
# Needed to manually create HttpResponses or raise an Http404 exception
from django.http import HttpResponse, Http404
# Helper function to guess a MIME type from a file name
from mimetypes import guess_type
from django.shortcuts import get_object_or_404


def home(request):
    events = Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data, mimetype='application/json')


def get_photo_list(request):
    event_id = request.GET.get('event_id')
    event = Event.objects.filter(id=event_id)
    photo_list = Photos.objects.filter(event=event)
    data = serializers.serialize('json', photo_list)
    return HttpResponse(data, mimetype='application/json')


def get_photo(request):
    photo_id = request.GET.get('photo_id')
    photo_object = get_object_or_404(Photos, id=photo_id)
    if not photo_object.photo:
        raise Http404
    content_type = guess_type(photo_object.photo.name)
    return HttpResponse(photo_object.photo, mimetype=content_type)


def show_thumbnail(request):
    event_id = request.GET.get('event_id')
    event = get_object_or_404(Event, id=event_id)
    if not event.first_photo:
        raise Http404
    content_type = guess_type(event.first_photo.name)
    return HttpResponse(event.first_photo, mimetype=content_type)


def get_event_list(request):
    if request.GET.get('label'):
        label = request.GET.get('label')
        label_object = Labels.objects.filter(label=label)
        events = Event.objects.filter(label=label_object)
    #elif request.user.is_authenticated():
    #    labels = UserLabels.objects.filter(user=request.user)
    #    label_object = Labels.objects.filter(label=labels)
    #    events = Event.objects.filter(label=label_object)
    else:
        events = Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data, mimetype='application/json')


def show_event(request):
    event_id = request.GET.get('event_id')
    event = Event.objects.filter(id=event_id)
    data = serializers.serialize('json', event)
    return HttpResponse(data, mimetype='application/json')


def get_comments(request):
    event_id = request.GET.get('event_id')
    event = Event.objects.filter(id=event_id)
    comments = Comments.objects.filter(event=event)
    data = serializers.serialize('json', comments)
    return HttpResponse(data, mimetype='application/json')


def get_labels(request):
    labels = Labels.objects.all()
    data = serializers.serialize('json', labels)
    return HttpResponse(data, mimetype='application/json')







