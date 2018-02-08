import json

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import View

from users.models import User, ImageStory


class CreateUser(View):

    def post(self, request, *args, **kwargs):
        coords = self.request.POST.get('coords', None)
        name = self.request.POST.get('name', None)
        if not coords or not name:
            return HttpResponseBadRequest('No name or coordinates')
        point = Point(coords['long'], coords['lat'])
        user = User.objects.create(name=name)
        return HttpResponse(
            json.dumps({"id": user.id}), status=200)


class UploadImage(View):

    def post(self, request, *args, **kwargs):
        uid = self.request.POST.get('uid', None)
        imagefile = self.request.FILES.get('image', None)
        if not imagefile or not uid:
            return HttpResponseBadRequest('No uid or no imagefile')
        user = User.objects.get(pk=uid)
        file = ImageStory.objects.create(
            owner_id=uid, document=imagefile)
        return HttpResponse(
            json.dumps({
                "id": uid,
                "image_url": file.document.url
            }),
            status=200)


class FetchNearby(View):

    def get(self, request, *args, **kwargs):
        uid = self.request.GET.get('uid', None)
        user = User.objects.get(id=uid)
        radius = 1
        stories = ImageStory.objects.all().order_by('-when')
        response = []
        for story in stories:
            response.append({
                "name": story.owner.name,
                "image_url": story.document.url})
        return HttpResponse(json.dumps(response), status=200)
