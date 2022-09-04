from django.urls import path
import events.views as events_views

urlpatterns = [
    path('add-collection/', events_views.add_collection, name='add-collection'),
    path('add-participant/', events_views.add_participant, name='add-participant'),
]