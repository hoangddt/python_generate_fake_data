from faker import Faker
import yaml
from MyProvider import MyProvider

def example_use():
    fake = Faker()
    fake.add_provider(MyProvider)

    # load data to dict
    raw_data = open("sample_data.yaml").read()
    pydict_data = yaml.load(raw_data)
    print("Original data:")
    print_dict(pydict_data)
    # render data
    for key, value in pydict_data.items():
        pydict_data[key] = fake.render_template(value)

    print("Data after process:")
    print_dict(pydict_data)

def print_dict(dict):
    for key, value in dict.items():
        print("[{}] => {}".format(key, value))

if __name__ == "__main__":
    example_use()