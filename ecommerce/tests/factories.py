import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()
from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    # name = fake.lexify(text="cat_name_?????")produces random text name
    name = factory.Sequence(
        lambda n: "cat_slug_%d" % n
    )  # produces unique random name
    slug = fake.lexify(text="cat_slug_?????")


register(CategoryFactory)
