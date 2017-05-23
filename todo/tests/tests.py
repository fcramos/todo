# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from todo.models import Todo


class TodoTest(TestCase):
    def setUp(self):
        self.todo = Todo(
            description='Do anything'
        )
        self.todo.save()

    def test_create(self):
        'Todo may be saved'
        self.assertEqual(1, self.todo.pk)

    def test_str(self):
        'Todo string representation may be the description.'
        self.assertEqual('Do anything', str(self.todo))

    def test_order(self):
        'Todos may be ordered by order field'
        todo_2 = Todo(
            description='Do other thing'
        )
        todo_2.save()
        self.assertEqual(1, self.todo.order)
        self.assertEqual(2, todo_2.order)

    def test_done(self):
        'Todo done may be unchecked'
        self.assertEqual(False, self.todo.done)
        self.todo.done = True
        self.assertEqual(True, self.todo.done)
