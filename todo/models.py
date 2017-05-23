# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):
    description = models.CharField(verbose_name=_(u'descrição'), max_length=100)
    order = models.PositiveIntegerField(verbose_name=_('ordem'))
    done = models.BooleanField(verbose_name=_('feita'), default=False)

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = Todo.objects.last().order + 1 if Todo.objects.count() else 1

        super(Todo, self).save(*args, **kwargs)
