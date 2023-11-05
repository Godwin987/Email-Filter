from simplegmail import Gmail
from simplegmail.query import construct_query
from messagehandler import telegram_bot_sendtext

gmail = Gmail(client_secret_file='client_secret.json')

labels = gmail.list_labels()

# Messages that are: newer than 2 days old, unread, labeled "Finance" or both "Homework" and "CS"
query_params = {
    "newer_than": (2, "day"),
    "unread": True,
    "labels":[["updates"]]
}

messages = gmail.get_messages(query=construct_query(query_params))
senders = set(message.sender.split('<', 1)[0] for message in messages if 'McKinsey' in message.sender or 'James Clear' in message.sender or 'Quora' in message.sender)

for name in senders:
    telegram_bot_sendtext(f"You've got a message from {name}")
    