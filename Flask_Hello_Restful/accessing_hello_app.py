from urllib import request

request1 = request.Request('http://127.0.0.1:8000/')
request2 = request.Request('http://127.0.0.1:8000/home/')
request3 = request.Request('http://127.0.0.1:8000/index/')

try:
    response1 = request.urlopen(request1)
    response2 = request.urlopen(request2)
    response3 = request.urlopen(request3)
    print("\n response-1")
    print(response1.read())
    print("\n response-2")
    print(response2.read())
    print("\n response-3")
    print(response3.read())
    print("\n printing the status \n")
    print('STATUS :',response1.status)
    print(response1.info())

    
except urllib.error.HTTPError as e:
    print(e.code, e.read())