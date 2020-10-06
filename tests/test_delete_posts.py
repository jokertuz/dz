import allure
import pytest
from requests import codes

from framework.check import status_code_check
from framework.jsonplaceholder_client import Client


@allure.suite('DELETE /posts')
class TestDeletePosts:

    @allure.title('Positive. Delete by id')
    @pytest.mark.parametrize("id", [2, 50, 100])
    def test_delete_by_id(self, id):
        response = Client().delete_posts_by_id(id)
        status_code_check(response, codes.ok)

    @allure.title('Negative. Delete by nonexistent id')
    @pytest.mark.parametrize("id", [0, 987987987])
    def test_delete_by_nonexistent_id(self, id):
        response = Client().delete_posts_by_id(id)
        status_code_check(response, codes.not_found)

    @allure.title('Negative. Delete posts by invalid id')
    @pytest.mark.parametrize("id", ['string', 0.5, ' ', ')('])
    def test_delete_posts_by_invalid_id(self, id):
        response = Client().delete_posts_by_id(id)
        status_code_check(response, codes.bad_request)
