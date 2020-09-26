from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError

blog = {'title' : 'test blog title','article_text' : 'test blog article'}
data = urlencode(blog)
data = data.encode('ascii')

request2 = Request('http://127.0.0.1:5000/blogs/1/', data=data, method='POST')
try:
    response2 = urlopen(request2)
    print(response2.read())
except HTTPError as e:
    print(e.code, e.read())
