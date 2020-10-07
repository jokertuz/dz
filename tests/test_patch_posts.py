import allure
import pytest
from requests import codes

from framework.check import (check_patch_post_body_in_response,
                             status_code_check)
from framework.jsonplaceholder_client import Client


@allure.suite('PATCH /posts/id')
class TestPatchPosts:

    @allure.title('Positive. Patch posts valid id')
    @pytest.mark.parametrize('id', [1, 50, 100])
    def test_patch_posts_by_id(self, id, body_json):
        response = Client().patch_posts_by_id(id, body_json)
        status_code_check(response, codes.ok)

    @allure.title('Positive. Patch posts by body')
    @pytest.mark.parametrize('id', [1, 50, 100])
    def test_patch_posts_by_id_body(self, id, body_json):
        response = Client().patch_posts_by_id(id, body_json)
        check_patch_post_body_in_response(response, body_json)
