from fbchat import log, Client
from fbchat.models import *
import apiai, json
import requests
import random
import time
from datetime import datetime
#import all new methods



#nohup python3 MargotMain.py &
#usersDict = {'100002542248681': "Shouen", '100006529086273': "Andrew", '100001756065113': "John"}
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
                bullyMessage = bully(author_id, message_object, client)
                self.send(Message(bullyMessage), thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("no bullying occurred")
            try:
                greeting = greetingResponse(author_id, message_object, client)
                self.send(Message(greeting), thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("no greeting occurred")

            try:
                apiaiReply = callApiAI(self, message_object, client)
                apiaiReplyAsMessage = Message(apiaiReply)
                self.send(apiaiReplyAsMessage, thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("apiai did not work")

            try:
                commandList = askForHelp(message_object, client)
                for command in commandList:
                    self.send(Message(command), thread_id=thread_id, thread_type=thread_type)
            except Exception:
                print("did not ask for !help")

            try:
                if "!duel" in message_object.text:
                    challengers = duel(self, author_id, message_object, threadID, client)
                    duelers[0] = challengers[0]
                    duelers[1] = challengers[1]
                    duelStartTime = time.time()
                    print(duelStartTime)
                    for i in range(3, 0, -1):
                        count = str(i)
                        self.send(Message(count), thread_id=thread_id, thread_type=thread_type)
                        time.sleep(1)
                    #d = duelers[0] + duelers[1]
                    #self.send(Message(d), thread_id=thread_id, thread_type=thread_type)
                    #else:
                    #    self.send(Message("No one shot"), thread_id=thread_id, thread_type=thread_type)
            except FBchatFacebookError:
                print("did not duel")

client = EchoBot("lkw_63@yahoo.com", "pearlhacks2019")

#add all new methods in here
def filterMessageForActions(author_id, message_object, thread_id, thread_type, client):
    messageText = message_object.text
    authorID = author_id
    bully(authorID, messageText, client)

#def searchForUsers(userID, client):


#takes in userID
#calls firstnameFromUserInfo()
#puts userID:first name into usersDictionary
#returns first name of userInfo
def usernameFromID(userID, client): #userID as string
    userInfo = client.fetchThreadInfo(userID)
    firstname = firstnameFromUserInfo(userInfo, userID, client)
    try:
        usersDictionary.update(userInfo)
    except:
        x=0
    return(firstname)

#takes in userInfo
#returns first name from userInfo
def firstnameFromUserInfo(userInfo, userID, client):
    firstSpaceIndex = str(userInfo[userID]).find(" ")
    secondSpaceIndex = str(userInfo[userID]).find(" ", firstSpaceIndex + 1)
    firstname = str(userInfo[userID])[firstSpaceIndex + 1 : secondSpaceIndex]
    return(firstname)


#takes in message_object
#returns a list the userIDs of all the mentions
def mentionsToUserID(message_object, client):
    mentions = []
    for mention in message_object.mentions:
        mentions.append(mention.thread_id)
    return(mentions[0])

def callApiAI(self, message_object, client):
    if "!margot" in message_object.text:
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