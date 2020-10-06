from datetime import datetime

from faker import Faker

fake = Faker()
Faker.seed(datetime.now().microsecond)

generatorJsonPut = {
    'userId': fake.pyint(),
    'title': fake.pystr(),
    'body': fake.pystr()
}
