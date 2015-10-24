from faker import Faker

from faker.providers import BaseProvider


class MyProvider(BaseProvider):
    
    def render_template(self, pattern):
        return self.generator.parse(pattern)

    # more method goes here
        