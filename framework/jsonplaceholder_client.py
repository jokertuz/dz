import allure
import requests as r

from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, data, json):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=data, json=json)

    def _put(self, path: str, data):
        return r.put(url=JSONPLACEHOLDER_HOST + path, data=data)

    def _patch(self, path: str, data):
        return r.patch(url=JSONPLACEHOLDER_HOST + path, data=data)

    def _delete(self, path: str):
        return r.delete(url=JSONPLACEHOLDER_HOST + path)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_all_posts_id_comments(self, posts_id):
        return self._get(path=f'/posts/{posts_id}/comments')

    @allure.step
    def get_posts_by_id(self, posts_id):
        return self._get(path=f'/posts/{posts_id}')

    @allure.step
    def get_posts_by_params(self, params: dict):
        params = [f'{name}={value}' for name, value in params.items()]
        query = str.join('&', params).replace(' ', '%20').replace('\n', '%0A')
        return self._get(path=f'/posts?{query}')

    @allure.step
    def post_posts_by_body(self, data=None, json=None):
        return self._post(path=f'/posts', data=data, json=json)

    @allure.step
    def post_posts(self, data=None, json=None):
        return self._post(path=f'/posts', data=data, json=json)

    @allure.step
    def put_posts_by_id(self, posts_id, data=None):
        return self._put(path=f'/posts/{posts_id}', data=data)

    @allure.step
    def patch(self, posts_id, data=None):
        return self._patch(path=f'/posts/{posts_id}', data=data)

    @allure.step
    def delete_posts_by_id(self, posts_id):
        return self._delete(path=f'/posts/{posts_id}')
