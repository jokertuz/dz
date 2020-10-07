import allure
from hamcrest import assert_that, equal_to
from requests import codes


@allure.step
def status_code_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    status_code_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_all_comments_response(response):
    status_code_check(response)
    assert_that(len(response.json()), equal_to(5))


@allure.step
def check_get_post_contains_id_response(response, expected_id):
    actual_id = response.json()['id']
    status_code_check(response)
    assert_that(actual_id, equal_to(expected_id),
                f'Expected id: {expected_id}. Actual id: {actual_id}. URL {response.url}')


@allure.step
def check_put_post_contains_id_response(response, expected_id):
    actual_id = response.json()['id']
    status_code_check(response)
    assert_that(actual_id, equal_to(expected_id),
                f'Expected id: {expected_id}. Actual id: {actual_id}. URL {response.url}')


@allure.step
def check_get_post_contains_id_response_by_params(response, expected_id):
    actual_id = response.json()[0]['id']
    status_code_check(response)
    assert_that(actual_id, equal_to(expected_id),
                f'Expected id: {expected_id}. Actual id: {actual_id}. URL {response.url}')


@allure.step
def check_post_posts_to_the_body(response, expected_code):
    status_code_check(response)
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_posts_the_same(response, expected_post, expected_code=codes.ok):
    status_code_check(response, expected_code)
    actual_post = response.json()
    assert_that(actual_post(['userId']), equal_to(expected_post['userId']),
                f'Expected userId: {expected_post["userId"]}. Actual userId: {actual_post["userId"]}.'
                f' Url: {response.url}')
    assert_that(actual_post['title'], equal_to(expected_post['title']),
                f'Expected title: {expected_post["title"]}. Actual title: {actual_post["title"]}.'
                f' Url: {response.url}')
    assert_that(actual_post['body'], equal_to(expected_post['body']),
                f'Expected body: {expected_post["body"]}. Actual body: {actual_post["body"]}.'
                f' Url: {response.url}')


@allure.step
def check_post_post_contains_id_response(response, expected_post, expected_code=codes.ok):
    status_code_check(response, expected_code)
    assert_that(expected_post in response.json(),
                f'Expected: response contains {expected_post}. Actual: {response.json()}. Url: {response.url}')


@allure.step
def check_patch_post_body_in_response(response, expected_post):
    actual_post = response.json()
    assert_that(actual_post['userId'], equal_to(str(expected_post['userId'])),
                f'Expected userId: {expected_post["userId"]}. Actual userId: {actual_post["userId"]}.'
                f' Url: {response.url}')
    assert_that(actual_post['title'], equal_to(expected_post['title']),
                f'Expected title: {expected_post["title"]}. Actual title: {actual_post["title"]}.'
                f' Url: {response.url}')
    assert_that(actual_post['body'], equal_to(expected_post['body']),
                f'Expected body: {expected_post["body"]}. Actual body: {actual_post["body"]}.'
                f' Url: {response.url}')
