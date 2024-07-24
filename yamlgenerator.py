import yaml
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
        "content": fake.text(max_nb_chars=200)
    }

def create_yaml_file(filename):
    data = generate_dummy_data()
    
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# Generate 5 YAML files
for i in range(5):
    filename = f"dummy_data_{i+1}.yaml"
    create_yaml_file(filename)
    print(f"Created {filename}")