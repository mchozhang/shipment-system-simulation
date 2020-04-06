#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Database Schema of Record
"""
from mongoengine import Document, StringField, IntField, FloatField, ListField


class Record(Document):
    user = StringField(required=True)
    age = IntField()
    product = StringField(required=True)
    latitude = FloatField()
    longitude = FloatField()
    hierarchy = ListField()

    def to_json(self):
        return {
            "id": str(self.pk),
            "user": self.user,
            "age": self.age,
            "product": self.product,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "hierarchy": ", ".join(self.hierarchy),
        }

