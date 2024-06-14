import json
import random
from faker import Faker
from .models import Person

def generate_fake_person():
    """
    Generate a fake Person instance using Faker library.
    """
    fake = Faker()
    person = {
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'skills': ', '.join(fake.words(nb=random.randint(1, 5))),
        'experience': fake.sentence(nb_words=random.randint(5, 15)),
        'education': fake.sentence(nb_words=random.randint(5, 15)),
    }
    return person

def generate_fake_persons(num_persons=10):
    """
    Generate fake Person instances.
    """
    fake_persons = []
    for _ in range(num_persons):
        fake_persons.append(generate_fake_person())
    return fake_persons

def add_persons_from_json_list(json_list):
    """
    Create Person instances from a list of JSON data.
    """
    persons = []
    for json_data in json_list:
        person = add_person_from_json(json_data)
        persons.append(person)
    return persons

# Generate fake Person data
fake_persons = generate_fake_persons()

# Convert fake Person data to JSON format
json_persons = [json.dumps(person) for person in fake_persons]

# Create Person instances from JSON data
persons = add_persons_from_json_list(json_persons)
