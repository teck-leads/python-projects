from flask_testing import TestCase
from flask import escape
from helloapp import app, db
from .config import TestingConfig
from .models import Quotes
from .forms import QuoteForm


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(TestingConfig)

        return app

    @classmethod
    def setUpClass(cls):
        db.session.commit()
        db.drop_all()
        db.create_all()



class TestAddQuoteView(BaseTestCase):

    def test_status_code(self):
        response = self.client.get('/addquote/')
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get('/addquote/')
        self.assertTemplateUsed('addquote.html')

    def test_form_label1_name(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'label for="qstring"', response.data)

    def test_form_field1_id(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'input id="qstring"', response.data)

    def test_form_field1_name(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'input id="qstring" name="qstring"', response.data)

    def test_form_label2_name(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'label for="qauthor"', response.data)

    def test_form_field2_id(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'input id="qauthor"', response.data)

    def test_form_field2_name(self):
        response = self.client.get('/addquote/')
        self.assertIn(b'input id="qauthor" name="qauthor"', response.data)

    '''
    def test_form_field1_value(self):
        response = self.client.post('/addquote/', data=dict(qstring="Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                                                qauthor="Benjamin Franklin"))
        self.assertIn(b'value="Tell me and I forget. Teach me and I remember. Involve me and I learn."', response.data)

    def test_form_field2_value(self):
        response = self.client.post('/addquote/', data=dict(qstring="Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                                                qauthor="Benjamin Franklin"))
        self.assertIn(b'value="Benjamin Franklin"', response.data)
    '''

    def test_form_field1_validaton1(self):
        response = self.client.post('/addquote/', data=dict(qstring="",
                                                qauthor="Benjamin Franklin"))
        self.assertIn(b'[This field is required.]', response.data)

    def test_form_field1_validaton2(self):
        response = self.client.post('/addquote/', data=dict(qstring="Te",
                                                qauthor="Benjamin Franklin"))
        self.assertIn(b'[Field must be between 3 and 200 characters long.]', response.data)

    def test_form_field2_validaton1(self):
        response = self.client.post('/addquote/', data=dict(qstring="Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                                                qauthor=""))
        self.assertIn(b'[This field is required.]', response.data)

    def test_form_field2_validaton2(self):
        response = self.client.post('/addquote/', data=dict(qstring="Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                                                qauthor="Be"))
        self.assertIn(b'[Field must be between 3 and 100 characters long.]', response.data)

