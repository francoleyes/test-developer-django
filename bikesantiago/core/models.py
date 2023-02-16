from django.db import models
import requests
import json

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    typology = models.CharField(max_length=200)
    holder = models.CharField(max_length=200)
    investment = models.CharField(max_length=200)
    date_presentation = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name

def load_data_from_json():
    file_path = './proyectos.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data:
            project = Project(
                name=item['name'],
                type=item['type'],
                region=item['region'],
                typology=item['typology'],
                holder=item['holder'],
                investment=item['investment'],
                date_presentation=item['date_presentation'],
                state=item['state']
            )
            project.save()



class BikeSantiago(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    free_bikes = models.PositiveIntegerField()
    empty_slots = models.PositiveIntegerField()

    def __str__(self):
        return self.name

def get_bike_santiago_data():
    url = "http://api.citybik.es/v2/networks/bikesantiago"
    response = requests.get(url)
    data = response.json()
    for station in data['network']['stations']:
        bike_santiago = BikeSantiago(
            name=station['name'],
            latitude=station['latitude'],
            longitude=station['longitude'],
            free_bikes=station['free_bikes'],
            empty_slots=station['empty_slots']
        )
        bike_santiago.save()