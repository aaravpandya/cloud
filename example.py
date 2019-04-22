from azure.storage.blob import BlockBlobService, PublicAccess
from azure.storage.queue import QueueService, QueueMessage, QueueMessageFormat
import base64
import json
# from urllib import urlretrieve

block_blob_service = BlockBlobService(account_name='aarav', account_key='Fg9og9EvCCDhlA5Xm2fzO9OZbFCc5MB8gylGBfbaU0J2uUuhd3ytMmgpq0Mm/eHpJxEQDXC91QFooYeLdtT1tg==')
block_blob_service.create_blob_from_path("detectedimages","guid","1.jpg")

# queue_service = QueueService(account_name="aarav", account_key="Fg9og9EvCCDhlA5Xm2fzO9OZbFCc5MB8gylGBfbaU0J2uUuhd3ytMmgpq0Mm/eHpJxEQDXC91QFooYeLdtT1tg==")

# # queue_service.put_message("jsonqueue","hello world")
# messages = queue_service.peek_messages("jsonqueue")
# d = {}
# for message in messages:
#     d = json.loads(QueueMessageFormat.text_base64decode(message.content))
#     print(d["uri"])

# urlretrieve(d["uri"], "1.jpg")