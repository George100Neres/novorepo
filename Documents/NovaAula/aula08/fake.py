from faker import Faker
import random

faker = Faker('pt_BR')

print(faker.name())
print(faker.address)