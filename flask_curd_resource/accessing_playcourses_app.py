from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError

course = {'course_name' : 'Machine Learning'}
data = urlencode(course)
data = data.encode('ascii')

request2 = Request('http://127.0.0.1:5000/Courses/1', data=data, method='POST')
try:
    response2 = urlopen(request2)
    print(response2.read())
except HTTPError as e:
    print(e.code, e.read())

course = {'course_name' : 'Artificial Intelligence'}
data = urlencode(course)
data = data.encode('ascii')
request3 = Request('http://127.0.0.1:5000/Courses/2', data=data, method='POST')
try:
    response3 = urlopen(request3)
    print(response3.read())
except HTTPError as e:
    print(e.code, e.read())

course = {'course_name' : 'Cloud Computing'}
data = urlencode(course)
data = data.encode('ascii')
request4 = Request('http://127.0.0.1:5000/Courses/3', data=data, method='POST')
try:
    response4 = urlopen(request4)
    print(response4.read())
except HTTPError as e:
    print(e.code, e.read())

request5 = Request('http://127.0.0.1:5000/Courses/')
try:
    response5 = urlopen(request5)
    print(response5.read())
except HTTPError as e:
    print(e.code, e.read())

request6 = Request('http://127.0.0.1:5000/Courses/1')
try:
    response6 = urlopen(request6)
    print(response6.read())
except HTTPError as e:
    print(e.code, e.read())

request7 = Request('http://127.0.0.1:5000/Courses/2', method='DELETE')
try:
    response7 = urlopen(request7)
    print(response7.read())
except HTTPError as e:
    print(e.code, e.read())
    
request8 = Request('http://127.0.0.1:5000/Courses/')
try:
    response8 = urlopen(request8)
    print(response8.read())
except HTTPError as e:
    print(e.code, e.read())

course = {'course_name' : 'Microservices'}
data = urlencode(course)
data = data.encode('ascii')
request9 = Request('http://127.0.0.1:5000/Courses/3', data=data, method='PUT')
try:
    response9 = urlopen(request9)
    print(response9.read())
except HTTPError as e:
    print(e.code, e.read())
    
request10 = Request('http://127.0.0.1:5000/Courses/')
try:
    response10 = urlopen(request10)
    print(response10.read())
except HTTPError as e:
    print(e.code, e.read())