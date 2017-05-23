# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import modelformset_factory

from .models import Todo


TodoFormSet = modelformset_factory(Todo, exclude=[], extra=1, can_delete=True)
