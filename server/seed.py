#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Message

fake = Faker()

def make_messages():
    print("Deleting old messages...")
    Message.query.delete()

    usernames = [fake.first_name() for _ in range(4)]
    if "Duane" not in usernames:
        usernames.append("Duane")

    print("Seeding new messages...")
    messages = []

    for _ in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames)
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()
    print("Done seeding!")

if __name__ == '__main__':
    with app.app_context():
        make_messages()
