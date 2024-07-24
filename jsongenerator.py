import json
from faker import Faker
import os

fake = Faker()

def generate_dummy_data():
    return {
        "title": fake.sentence(),
        "description": fake.paragraph(),
        "date": str(fake.date_this_year()),
        "author": fake.name(),
        "tags": fake.words(nb=3),
        "content": fake.text(max_nb_chars=200),
        "number_of_views": fake.random_int(min=100, max=10000),
        "is_published": fake.boolean(),
        "rating": round(fake.random.uniform(1, 5), 1)
    }

def create_json_file(filename):
    data = generate_dummy_data()
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

# Generate 5 JSON files
for i in range(5):
    filename = f"dummy_data_{i+1}.json"
    create_json_file(filename)
    print(f"Created {filename}")