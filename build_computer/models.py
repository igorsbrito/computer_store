from django.db import models
from datetime import datetime

from userProfile.models import User


class ComputerQuerySet(models.QuerySet):

    def create_computer(self, components, user):

        mother_board = components['mother_board']['name']
        cpu = components['cpu']['name']
        ram = ''

        for ram_element in components['ram']:
            ram += "{} {}Gb,".format(ram_element['name'], ram_element['size'])

        if components['video_card'] is not None:
            vide_card = components['video_card']['name']
        else:
            vide_card = ''

        self.create(
            mother_board=mother_board,
            cpu=cpu,
            ram_memory=ram,
            video_card=vide_card,
            belong=user)


class Computer(models.Model):
    belong = models.ForeignKey(User, related_name='computer_user', on_delete=models.CASCADE,
                               verbose_name='Belong to user')
    mother_board = models.CharField(max_length=120, verbose_name='Mother Board')
    cpu = models.CharField(max_length=120, verbose_name='CPU')
    ram_memory = models.CharField(max_length=120, verbose_name='RAM Memory',
                                   help_text='if have more than one ram must be divide by a comma')
    video_card = models.CharField(max_length=120, verbose_name='Video Card', blank=True)
    created_date = models.DateTimeField(default=datetime.now, verbose_name='Created Date')

    objects = ComputerQuerySet.as_manager()

    def __str__(self):
        return "Cpu: {}".format(self.cpu)
