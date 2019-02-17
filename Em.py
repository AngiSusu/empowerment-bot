from fbchat import log, Client
from fbchat.models import *
import apiai
import dialogflow_v2 as dialogflow
import json
import requests
import random
#import all new methods

#nohup python3 Em.py
usersDictionary = {}
#thread_id = '2037755022931734'
thread_type = ThreadType.GROUP
#2037755022931734
#1425006337609029

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def apiai(self):
        self.ClientAccessToken = 'cb9d7af798954065a44ce742b24baf28' #fixed
        self.ai = apiai.ApiAI(self.ClientAccessToken)
        self.request = self.ai.text_request()
        self.request.lang = 'de'
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        self.reply = ''

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        #filterMessageForActions(author_id, message_object, thread_id, thread_type, client)
        threadID = thread_id
        # If you're not the author, echo
        if author_id != self.uid:
            #self.send(message_object, thread_id=thread_id, thread_type=thread_type)
            try:
                apiaiReply = callApiAI(self, message_object, client)
                apiaiReplyAsMessage = Message(apiaiReply)
                self.send(apiaiReplyAsMessage, thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("apiai did not work")


client = Client("pandadude8@hotmail.com", "guacamole")

#add all new methods in here
def filterMessageForActions(author_id, message_object, thread_id, thread_type, client):
    messageText = message_object.text
    authorID = author_id


def callApiAI(self, message_object, client):
    message = message_object.text[7:]
    #setting up connection with apiai
    self.apiai()
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
    return(reply)


client.listen()