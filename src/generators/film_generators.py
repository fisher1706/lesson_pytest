from src.baseclasses.builder import BuilderBaseClass
from faker import Faker


fake = Faker()


class FilmBuilder(BuilderBaseClass):
    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_film_status(self, status=fake.word()):
        self.result['status'] = status
        return self

    def set_film_title(self, title=fake.word()):
        self.result['title'] = title
        return self

    def set_film_is_premiere(self, is_premiere=True):
        self.result['is_premiere'] = is_premiere
        return self

    def reset(self):
        self.set_film_status()
        self.set_film_title()
        self.set_film_is_premiere()

    def build(self):
        return self.result


z = FilmBuilder().build()
print(z)