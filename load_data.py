import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abra.settings")
django.setup()

from django.contrib.auth.models import User
from messaging_system.models import Message
from abra.settings import ADMIN


def load_data_from_json(file_path):
    # Create Admin user
    admin_user = User.objects.create(
        username=ADMIN["USER_NAME"],
        email=ADMIN["EMAIL"],
        first_name="Admin",
        is_superuser=ADMIN["IS_SUPERUSER"],
        is_staff=ADMIN["IS_STAFF"],
    )
    admin_user.set_password(ADMIN["PASSWORD"])
    admin_user.save()

    # Extract users and messages data from JSON
    with open(file_path, "r") as file:

        data = json.load(file)

        users = data.get("users", [])
        messages = data.get("messages", [])

        # Create user
        for user_data in users:
            user = User.objects.create(
                username=user_data.get("username"),
                email=user_data.get("email"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
            )
            # Set password using set_password method
            user.set_password(user_data.get("password"))
            user.save()

        # Create message
        for message_data in messages:
            message = Message.objects.create(
                sender_id=message_data.get("sender_id"),
                receiver_id=message_data.get("receiver_id"),
                message=message_data.get("message"),
                subject=message_data.get("subject"),
            )


if __name__ == "__main__":
    file_path = "data.json"
    load_data_from_json(file_path)
