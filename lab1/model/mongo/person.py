from mongoengine import *


class Person(Document):
    id = DecimalField(required=True)
    name = StringField(required=True, max_length=200)
    isBeneficiary = BooleanField(required=True)
    isContractStudent = BooleanField(required=True)
