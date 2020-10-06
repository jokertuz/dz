import allure
import pytest
from requests import codes

from config import POST_FOR_TEST
from framework.check import check_get_all_posts_response, status_code_check, check_get_post_contains_id_response, \
    check_get_post_contains_id_response_by_params
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check_get_all_posts_response(response)

    @allure.title('Positive. Get posts by id')
    @pytest.mark.parametrize("id", [1, 50, 100])
    def test_get_posts_by_id(self, id):
        response = Client().get_posts_by_id(id)
        check_get_post_contains_id_response(response, id)

    @allure.title('Negative. Get posts by invalid id')
    @pytest.mark.parametrize("id", ['string', 0.5, ' ', ')('])
    def test_get_posts_by_invalid_id(self, id):
        response = Client().get_posts_by_id(id)
        status_code_check(response, codes.bad_request)

    @allure.title('Negative. Get posts by nonexistent id')
    @pytest.mark.parametrize("id", [0, 987987987])
    def test_get_posts_by_nonexistent_id(self, id):
        response = Client().get_posts_by_id(id)
        status_code_check(response, codes.not_found)

    @allure.title('Positive. Get posts by params')
    def test_get_posts_by_params(self):
        response = Client().get_posts_by_params(POST_FOR_TEST)
        id = POST_FOR_TEST['id']
        check_get_post_contains_id_response_by_params(response, id)
