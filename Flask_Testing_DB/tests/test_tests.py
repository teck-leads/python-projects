import os
import pytest
import requests
from api import app



class Test_API:
    client = app.test_client()

    def test_file_contents(self):
        with open('tests/test_routes.py', 'r') as f:
            content = f.read()
            assert "test_user_in_db" in content
            assert "test_user_list" in content
            assert "test_user_register" in content
            assert  "test_get_user" in content
            assert "test_data_in_db_after_adding" in content
            assert "test_after_adding_users" in content
            assert "@pytest.fixture" in content
        
            count_of_as = content.count("assert")
            assert count_of_as == 12