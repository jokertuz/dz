import allure
import pytest
from requests import codes

from framework.check import (check_put_post_contains_id_response,
                             status_code_check)
from framework.jsonplaceholder_client import Client


@allure.suite('PUT /posts/id')
class TestPutPosts:

    @allure.title('Positive. Put posts valid id')
    @pytest.mark.parametrize('id', [1, 50, 100])
    def test_put_posts_by_id(self, id, body_json):
        response = Client().put_posts_by_id(id, body_json)
        status_code_check(response, codes.ok)

    @allure.title('Positive. Put posts by id')
    @pytest.mark.parametrize('id', [1, 50, 100])
    def test_put_posts_by_id_body(self, id, body_json):
        response = Client().put_posts_by_id(id, body_json)
        check_put_post_contains_id_response(response, id)

    @allure.title('Negative. Put posts by invalid id')
    @pytest.mark.parametrize('id', ['string', 0.5, ' ', ')('])
    def test_put_posts_by_invalid_id(self, id, body_json):
        response = Client().put_posts_by_id(id, body_json)
        status_code_check(response, codes.bad_request)

    @allure.title('Negative. Put posts by nonexistent id')
    @pytest.mark.parametrize('id', [0, 987987987])
    def test_put_posts_by_nonexistent_id(self, id, body_json):
        response = Client().put_posts_by_id(id, body_json)
        status_code_check(response, codes.not_found)
