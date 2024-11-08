import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'class_digital.settings')

import django
django.setup()

#Fake Pop Script
import random
from classdigitalapp.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get tge topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script...")
    populate(20)
    print("Populating complete!")