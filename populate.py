import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myProject.settings')

import django
django.setup()

##fake pop script
import random
from myApp.models import Topics,AccessRecord,Webpage

from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topics.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top=add_topic()

        #create the fake data fro that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


        #create fake access record for that webpage
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='main':
    print('Populating Script!')
    populate(20)
    print('Populating complete')
