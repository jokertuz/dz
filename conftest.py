from datetime import datetime

import pytest
from faker import Faker

from framework.helper import generatorJsonPut

fake = Faker()
Faker.seed(datetime.now().microsecond)


@pytest.fixture(scope='session')
def body_json():
    return generatorJsonPut


@pytest.fixture(scope='session')
def post_invalid_json():
    return {
        fake.pystr(): fake.pystr()

    }
