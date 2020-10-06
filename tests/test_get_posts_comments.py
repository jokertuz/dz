import allure
import pytest
from requests import codes

from framework.check import check_get_all_comments_response, status_code_check
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts/id/comments')
class TestGetCommentsPosts:

    @allure.title('Positive. Get comments by id')
    def test_get_comments_by_id(self):
        id = 2
        response = Client().get_all_posts_id_comments(id)
        check_get_all_comments_response(response)

    @allure.title('Negative. Get comments by nonexistent id')
    @pytest.mark.parametrize("id", [0, 987654321])
    def test_get_comments_by_nonexistent_id(self, id):
        response = Client().get_all_posts_id_comments(id)
        status_code_check(response, codes.not_found)

    @allure.title('Negative. Get comments by nonexistent id')
    @pytest.mark.parametrize("id", ['string', 0.5, '100', ' ', ')(', ])
    def test_get_comments_by_invalid_id(self, id):
        response = Client().get_all_posts_id_comments(id)
        status_code_check(response, codes.bad_request)
