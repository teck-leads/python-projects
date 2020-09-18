from flask_testing import TestCase
from myflaskproj import app
import os
import html

class BaseTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['BASE_DIR'] = os.path.dirname(os.path.dirname(__file__))

        return app


class TestAccessingPythonDataTypes(BaseTestCase):

    TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    TEMPLATE_NAME = 'accessingPythonDataTypes.html'

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(cls.TEMPLATES_FOLDER, cls.TEMPLATE_NAME)) as temp_fp:
            cls.template = temp_fp.read()


    def test_status_code(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertTemplateUsed('accessingPythonDataTypes.html')

    def test_string_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b'String : Sample String', response.data)
        self.assertIn('String : {{ data.str }}', self.template)

    def test_integer_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b'Integer : 56', response.data)
        self.assertIn('Integer : {{ data.int }}', self.template)

    def test_float_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b'Float : 8.9', response.data)
        self.assertIn('Float : {{ data.float }}', self.template)

    def test_list_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn("List : ['John', 'Priya', 'Rosy', 'Smith']", html.unescape(response.data.decode('utf-8')))
        self.assertIn('List : {{ data.list }}', self.template)

    def test_list_element_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"Second element of List : Priya", response.data)
        self.assertIn('Second element of List : {{ data.list.1 }}', self.template)

    def test_tuple_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn("Tuple : ('John', 'Priya', 'Rosy', 'Smith')", html.unescape(response.data.decode('utf-8')))
        self.assertIn('Tuple : {{ data.tuple }}', self.template)

    def test_tuple_element_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"Third element of Tuple : Rosy", response.data)
        self.assertIn('Third element of Tuple : {{ data.tuple.2 }}', self.template)

    def test_dictionary_element_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"Email of Dictionary Object : willy@abc.com", response.data)
        self.assertIn('Email of Dictionary Object : {{ data.dict.email }}', self.template)

    def test_boolean_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"Boolean : True", response.data)
        self.assertIn('Boolean : {{ data.bool }}', self.template)

    def test_none_access(self):
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"None : None", response.data)
        self.assertIn('None : {{ data.none }}', self.template)

    def test_set_access(self):
        set_access_syntax = '''<li> Elements of a Set :
<ul>
{% for element in data.set %}
<li> {{ element }} </li>
{% endfor %}
</ul>
</li>
'''
        response = self.client.get('/access_pydatatypes/')
        self.assertIn(b"Elements of a Set :", response.data)
        self.assertIn(b"<li> Basket Ball </li>", response.data)
        self.assertIn(b"<li> Cricket </li>", response.data)
        self.assertIn(b"<li> Foot Ball </li>", response.data)
        self.assertIn(b"<li> Tennis </li>", response.data)
        self.assertIn(set_access_syntax, self.template)

class TestUsingJinjaFilters(BaseTestCase):

    TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    TEMPLATE_NAME = 'usingfilters.html'

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(cls.TEMPLATES_FOLDER, cls.TEMPLATE_NAME)) as temp_fp:
            cls.template = temp_fp.read()

    def test_status_code(self):
        response = self.client.get('/filters/')
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get('/filters/')
        self.assertTemplateUsed('usingfilters.html')

    def test_filter_round_usage(self):
        response = self.client.get('/filters/')
        self.assertIn(b"Round : 100", response.data)
        self.assertIn('Round : {{ data.round | round(0, "ceil") }}', self.template)

    def test_filter_dictsort_usage(self):
        response = self.client.get('/filters/')
        self.assertIn("Dictsort : [('John', 188.976), ('Rosy', 176.784), ('Priya', 170.688), ('Akbar', 155.7528)]",
                      html.unescape(response.data.decode('utf-8')))
        self.assertIn("Dictsort : {{ data.dictsort | dictsort(by='value', reverse=True) }}", self.template)

    def test_filter_map_usage(self):
        response = self.client.get('/filters/')
        self.assertIn(b"Map : Hello, World!!!", response.data)
        self.assertIn("Map : {{ data.map | map('capitalize') | join(', ') }}", self.template)

    def test_filter_replace_usage(self):
        response = self.client.get('/filters/')
        self.assertIn(b"Replace : new is gnew", response.data)
        self.assertIn("Replace : {{ data.replace | replace('old', 'new') }}", self.template)

    def test_filter_tojson_usage(self):
        response = self.client.get('/filters/')
        self.assertIn(b'ToJson : [{"height": 188.976, "name": "John"}, {"height": 170.688, "name": "Priya"}, {"height": 176.784, "name": "Rosy"}, {"height": 155.7528, "name": "Akbar"}]', response.data)
        self.assertIn('ToJson : {{ data.tojson | tojson }}', self.template)

    def test_filter_evenFilter_usage(self):
        response = self.client.get('/filters/')
        self.assertIn(b"EvenFilter : [78, 22, 54, 68]", response.data)
        self.assertIn("EvenFilter : {{ data.evenfilter | evenFilter }}", self.template)  