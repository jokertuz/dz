import allure
import pytest
from requests import codes

from framework.check import (check_posts_the_same, status_code_check)
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestPostPosts:

    @allure.title('Positive. Post json')
    def test_post_posts_by_json_body(self, body_json):
        response = Client().post_posts_by_body(body_json)
        status_code_check(response, codes.created)

    @allure.title('Positive. Post non body')
    def test_post_posts_non_body(self):
        response = Client().post_posts()
        status_code_check(response, codes.created)

    @allure.title('Negative. Post invalid json')
    def test_post_posts_by_invalid_json_body(self, post_invalid_json):
        response = Client().post_posts_by_body(post_invalid_json)
        status_code_check(response, codes.bad_request)

    @allure.title('Negative. Post invalid body')
    @pytest.mark.parametrize('body', ['string', ' ', ')('])
    def test_post_posts_by_invalid_str_body(self, body):
        response = Client().post_posts_by_body(body)
        status_code_check(response, codes.bad_request)

    @allure.title('Positive. Post created')
    def test_post_post(self, body_json):
        client = Client()
        response = client.post_posts_by_body(body_json)
        response_new_post = client.get_posts_by_id(response.json()['id'])
        check_posts_the_same(response_new_post, body_json)
