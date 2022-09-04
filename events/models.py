from django.db import models
from django.http import HttpResponse
from django.utils.html import escape


class Collection(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)

    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection


class Participant(models.Model):
    name = models.CharField(max_length=50)


class Participants(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default=False)
    liste = []
    """
    @classmethod
    def __init__(cls):
        Participants.participants = []

    @classmethod
    def add_participant(cls, participant):
        Participants.participants = participant
        return Participants.participants
    """

    def create_participants_list(self):
        self.liste = self.liste

    def add_participant(self, participant):
        self.liste.append(participant)

    def get_participants(self):
        return self.liste
