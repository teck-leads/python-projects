import pytest
from api import app, db
import json
import base64
from flask import Flask
import os
from src.models.UserModel import UserModel

class Test_API:
	client  = app.test_client()
	
	@pytest.fixture(autouse=True, scope='session')
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
		db.create_all()
		yield db
		# os.remove('testing1.db')

# 1. Query from the model and a check len of result and the result: Method name: test_user_in_db
	def test_user_in_db(self):
		result  = UserModel.query.all()
		assert len(result) == 0
		assert result == []
# 2.GET the result from endpoint users/ and check json response and status code. Method name: test_user_list
	def test_user_list(self):
		url = "users/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == []
# 3. POST user infomrmation with testname and testaddress to the endpoint /users/add and check the json message and status code. Method name: test_user_register
	def test_user_register(self):
		url = "users/add"
		payload = '{"id": 1,"user_name": "madhav" , "address": "Hyderabad"}'
		headers = { 'Content-Type': "application/json",  'cache-control': "no-cache"  }
		response = self.client.post(url, data=payload, headers=headers)
		assert response.status_code == 201
		assert response.json['message'] == 'Added user to the list'
# 4. GET user with id 1 and check the json response and status code. Method Name: test_get_user
	def test_get_user(self):
		url = "users/1"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == {"id": 1,"user_name": "madhav" , "address": "Hyderabad"}	

# 5. Query from the Usermodel and check len of result and the user name of the result: Method name: test_data_in_db_after_adding
	def test_data_in_db_after_adding(self):
		result  = UserModel.query.all()
		assert len(result) == 1
		assert result[0].user_name == 'madhav'

# 6. GET the result from endpoint users/ and check the json response and status code. Method Name: test_after_adding_users
	def test_after_adding_users(self):
		url = "users/"
		response = self.client.get(url)
		assert response.status_code == 200
		assert response.json == [{"id": 1,"user_name": "madhav" , "address": "Hyderabad"}]		

    # Test methods 	
	# 1. Query from the model and a check len of result and the result: Method name: test_user_in_db
	# 2.GET the result from endpoint users/ and check json response and status code. Method name: test_user_list
	# 3. POST user infomrmation with testname and testaddress to the endpoint /users/add and check the json message and status code. Method name: test_user_register
	# 4. GET user with id 1 and check the json response and status code. Method Name: test_get_user
	# 5. Query from the Usermodel and check len of result and the user name of the result: Method name: test_data_in_db_after_adding
	# 6. GET the result from endpoint users/ and check the json response and status code. Method Name: test_after_adding_users
