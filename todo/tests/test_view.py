# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from todo.forms import TodoFormSet


class TodoTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('todo'))

    def test_get(self):
        """
        GET / should return status 200
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'todo/index.html')

    def test_html(self):
        'Should contain html elements'
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 11)
        self.assertContains(self.response, 'type="text"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        'Hmtl must contain csrf token'
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the todo_formset'
        form = self.response.context['todo_formset']
        self.assertIsInstance(form, TodoFormSet)
