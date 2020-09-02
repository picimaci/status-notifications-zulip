import os
import zulip
import re


target_stream = os.environ['ZULIP_TARGET_STREAM']
target_topic = os.environ['ZULIP_TARGET_TOPIC']
source_stream = os.environ['ZULIP_SOURCE_STREAM']
# ZULIP_SITE - zulip client
# ZULIP_EMAIL - zulip client
# ZULIP_API_KEY - zulip client


client = zulip.Client()


def send_notification(content):
    request = {
        "type": "stream",
        "to": target_stream,
        "topic": target_topic,
        "content": content,
    }
    client.send_message(request)


def process_message(event):
    message = event.get('message', {})
    content = str(message.get('content', ''))
    sender = str(message.get('sender_full_name', ''))
    content_without_quote = re.sub('```quote\n(.*)\n```', '', content)
    print(content_without_quote)
    if ':fire:' in content_without_quote:
        send_notification(f"{sender} feladat nélkül! :fire: :fire: :fire:")
    elif ':warning' in content_without_quote:
        send_notification(f"{sender} hamarosan feladat nélkül! :warning: :warning: :warning:")


client.call_on_each_event(
    callback=lambda event: process_message(event),
    event_types=["message"],
    narrow=[["stream", source_stream]]
)
