# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, null=True)

    create_date = models.DateTimeField('Create Date')
    due_date = models.DateTimeField('Due Date')
    completed_date = models.DateTimeField('Completed Date')

    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assignee')
    developer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='developer')
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project_manager')
    business_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='business_manager')

    HIGH = 'HIGH'
    MODERATE = 'MODERATE'
    LOW = 'LOW'

    PRIORITY_CHOICES = ((HIGH, 'High'), (MODERATE, 'Moderate'), (LOW, 'Low'),)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=HIGH)

    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'

    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)

    FW = 'CAR'
    TW = 'BIKE'
    TR = 'TRAVEL'
    TL = 'TERM_LIFE'
    HE = 'HEALTH'
    CF = 'CFSUPPORT'
    WS = 'WEBSITE'
    UL = 'ULTRON'

    COMPONENT_CHOICES = (
        (FW, 'Car'),
        (TW, 'Bike'),
        (TR, 'Travel'),
        (TL, 'Term Life'),
        (HE, 'Health'),
        (CF, 'CF Support'),
        (WS, 'Website'),
        (UL, 'Ultron'),
    )
    component = models.CharField(max_length=20, choices=COMPONENT_CHOICES, default=FW)

    asana_task = models.URLField(max_length=100, null=True, blank=True)
    pull_request = models.URLField(max_length=500, null=True, blank=True)
    test_link = models.URLField(max_length=100, null=True, blank=True)

    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return '%s : %s' % (self.component, self.title)


class Comment(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    add_date = models.DateTimeField('Date Added')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Added by %s' % (self.added_by)
