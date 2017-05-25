# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from task.models import Task

# Create your views here.


def all_task(request):

    all_task = Task.objects.all()

    context = {
        'all_task': all_task,
    }
    return render(request, "all_task.html", context)


def task(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task,
    }
    return render(request, "task.html", context)
