# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import View
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Todo
from .forms import TodoFormSet


class TodoView(View):
    def get(self, request):
        context = {
            'todo_formset': TodoFormSet()
        }
        return render(request, 'todo/index.html', context)

    def post(self, request):
        todo_formset = TodoFormSet(request.POST)
        if todo_formset.is_valid():
            todo_formset.save()

        return HttpResponseRedirect(reverse('todo'))
