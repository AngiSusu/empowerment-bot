from fbchat import Client
from fbchat.models import *
# client = Client('lkw_63@yahoo.com','pearlhacks2019')
client = Client('pandadude8@hotmail.com', 'guacamole')

# ''' Begin Testing '''

# print('Own id: {}'.format(client.uid))

# client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)

# thread_id = '100012852966935'
# thread_type = ThreadType.USER

thread_id = '2432226196801795'
thread_type = ThreadType.GROUP

# # Will send a message to the thread
# client.send(Message(text='t e s t i n g'), thread_id=thread_id, thread_type=thread_type)

# # Will send the default `like` emoji
# client.send(Message(emoji_size=EmojiSize.LARGE), thread_id=thread_id, thread_type=thread_type)

# # Will send the sticker with ID `767334476626295`
# client.send(Message(sticker=Sticker('767334476626295')), thread_id=thread_id, thread_type=thread_type)

# # Will send a message with a mention
# client.send(Message(text='This is a @mention', mentions=[Mention(thread_id, offset=10, length=8)]), thread_id=thread_id, thread_type=thread_type)

# # Will send the image located at `<image path>`
# client.sendLocalImage('/home/tuanyuan2008/empowerment-bot/empower.png', message=Message(text='This is a local image'), thread_id=thread_id, thread_type=thread_type)

# # Will download the image at the url `<image url>`, and then send it
# client.sendRemoteImage('https://www.mexicanplease.com/wp-content/uploads/2016/12/roasted-poblano-soup-six-poblano-peppers-after-roasting.jpg', message=Message(text='This is a remote image'), thread_id=thread_id, thread_type=thread_type)


# Only do these actions if the thread is a group
# if thread_type == ThreadType.GROUP:
    # Will remove the user with ID `<user id>` from the thread
    # client.removeUserFromGroup('100012769301046', thread_id=thread_id)

    # Will add the user with ID `<user id>` to the thread
    # client.addUsersToGroup('100012769301046', thread_id=thread_id)

    # Will add the users with IDs `<1st user id>`, `<2nd user id>` and `<3th user id>` to the thread
    # client.addUsersToGroup(['<1st user id>', '<2nd user id>', '<3rd user id>'], thread_id=thread_id)


# # Will change the nickname of the user `<user_id>` to `<new nickname>`
# client.changeNickname("Power Em", client.uid, thread_id=thread_id, thread_type=thread_type)

# Will change the title of the thread to `<title>`
# client.changeThreadTitle('Android', thread_id=thread_id, thread_type=thread_type)

# # Will set the typing status of the thread to `TYPING`
# client.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)

# Will change the thread color to `MESSENGER_BLUE`
# client.changeThreadColor(ThreadColor.BILOBA_FLOWER, thread_id=thread_id)

# client.reactToMessage(thread_id, MessageReaction.LOVE)

# ''' End Testing '''

message_id = client.send(Message(text='ligma'), thread_id='100012769301046', thread_type=ThreadType.USER)

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

print("users' IDs: {}".format([user.uid for user in users]))
print("users' names: {}".format([user.name for user in users]))


# If we have a user id, we can use `fetchUserInfo` to fetch a `User` object
user = client.fetchUserInfo('100006039725095')['100006039725095']
# We can also query both mutiple users together, which returns list of `User` objects
# users = client.fetchUserInfo('<1st user id>', '<2nd user id>', '<3rd user id>')

print("user's name: {}".format(user.name))
# print("users' names: {}".format([users[k].name for k in users]))


# `searchForUsers` searches for the user and gives us a list of the results,
# and then we just take the first one, aka. the most likely one:
user = client.searchForUsers('Sarah')[0]

print('user ID: {}'.format(user.uid))
print("user's name: {}".format(user.name))
print("user's photo: {}".format(user.photo))
print("Is user client's friend: {}".format(user.is_friend))


# Fetches a list of the 20 top threads you're currently chatting with
threads = client.fetchThreadList()
# Fetches the next 10 threads
threads += client.fetchThreadList(offset=20, limit=10)

print("Threads: {}".format(threads))


# Gets the last 10 messages sent to the thread
messages = client.fetchThreadMessages(thread_id=thread_id, limit=10)
# Since the message come in reversed order, reverse them
messages.reverse()

# Prints the content of all the messages
for message in messages:
    print(message.text)


# If we have a thread id, we can use `fetchThreadInfo` to fetch a `Thread` object
thread = client.fetchThreadInfo(thread_id)[thread_id]
print("thread's name: {}".format(thread.name))
print("thread's type: {}".format(thread.type))


# `searchForThreads` searches works like `searchForUsers`, but gives us a list of threads instead
thread = client.searchForThreads('Android')[0]
print("thread's name: {}".format(thread.name))
print("thread's type: {}".format(thread.type))


# Here should be an example of `getUnread`
client.logout()