from fbchat import log, Client
from fbchat.models import *
import apiai
# import dialogflow_v2 as dialogflow

import json
import requests

thread_id = '2193282257398154'
thread_type = ThreadType.GROUP

# Subclass fbchat.Client and override required methods
class EmBot(Client):
    def dialogflow(self):
        self.ClientAccessToken = 'cb9d7af798954065a44ce742b24baf28'     #fixed
        self.ai = apiai.ApiAI(self.ClientAccessToken)
        self.request = self.ai.text_request()
        self.request.lang = 'en'
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        self.reply = ''

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        if author_id != self.uid:
            try:
                apiaiReply = callApiAI(self, message_object, client)
                apiaiReplyAsMessage = Message(apiaiReply)
                self.send(apiaiReplyAsMessage, thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("ApiAi failed.")

def callApiAI(self, message_object, client):
    # message = message_object.text[7:]
    message = message_object.text

    #setting up connection with apiai
    self.dialogflow()
        #sending the query (message received)
    self.request.query = message
        #getting the json response
    api_response = self.request.getresponse()
    json_reply = api_response.read()
        #decoding to utf-8 (converting byte object to json format)
    decoded_data = json_reply.decode("utf-8")
        #loading it into json
    response = json.loads(decoded_data)
        #taking out the reply from json

    reply = response['result']['fulfillment']['speech']
    return reply

client = EmBot('em_mpltrxe_power@tfbnw.net', 'pearlhacks')
client.listen()