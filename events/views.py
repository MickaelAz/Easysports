from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
import re

from events.models import Collection, Participant, Participants


def index(request):
    context = {}

    #collection = Collection.get_default_collection()

    context["collection"] = Collection.objects.order_by("slug")
    context["participant"] = Participants.objects.order_by("name")

    return render(request, 'events/index.html', context=context)


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("La collection existe déjà.", status=409)
    """
    participant_name = f"{collection_name}_participant"
    participant_name = re.sub(" ", "_", f"{collection_name}_participant")
    print(participant_name)
    participants, created = Participants.objects.get_or_create(name=participant_name)
    #if not created:
    #    return HttpResponse("La collection existe déjà.", status=409)

    return_liste_participant = "toto"
    #for participant in liste_participants:
    #    part_html = f"<p>{participant}</p>"
    #    #print(participant)
    #    return_liste_participant = return_liste_participant + part_html
    """

    return HttpResponse(f"<h2>{collection_name}</h2>")


def add_participant(request):
    participant_name = escape(request.POST.get("participant-name"))
    participants_name = escape(request.POST.get("liste_connection_name"))
    #participants_name = re.sub(" ", "_", escape(request.POST.get("liste_connection_name")))
    #print(participants_name)
    participants, created = Participants.objects.get_or_create(title=participants_name, name=participant_name)
    #participants.create_participants_list()
    #participants.add_participant(participant_name)
    #print(participants.get_participants())
    """
    participants.name = participant_name
    participants.save()
    #participants.objects.values_list('name', flat=True)
    print(participants.name)

    #liste_participant = collection_liste_participant.add_participant(participant_name)
    """

    return HttpResponse(f"<p>{participant_name}</p>")
