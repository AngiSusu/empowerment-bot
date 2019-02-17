# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *

# Change this to your group id
old_thread_id = '2432226196801795'

# Change these to match your liking
old_color = ThreadColor.BILOBA_FLOWER
# old_emoji = '👍'
old_title = 'Android'
old_nicknames = {
    '100006039725095': "Sarah Chen",
    '100000922881557': "Francine Luo",
    '100012769301046': "Evan Mi",
}

class KeepBot(Client):
    def onColorChange(self, author_id, new_color, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and old_color != new_color:
            log.info("{} changed the thread color. It will be changed back".format(author_id))
            self.changeThreadColor(old_color, thread_id=thread_id)

    # def onEmojiChange(self, author_id, new_emoji, thread_id, thread_type, **kwargs):
    #     if old_thread_id == thread_id and new_emoji != old_emoji:
    #         log.info("{} changed the thread emoji. It will be changed back".format(author_id))
    #         self.changeThreadEmoji(old_emoji, thread_id=thread_id)

    def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
        if old_thread_id == thread_id and author_id != self.uid:
            log.info("{} got added. They will be removed".format(added_ids))
            for added_id in added_ids:
                self.removeUserFromGroup(added_id, thread_id=thread_id)

    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        # No point in trying to add ourself
        if old_thread_id == thread_id and removed_id != self.uid and author_id != self.uid:
            log.info("{} got removed. They will be re-added".format(removed_id))
            self.addUsersToGroup(removed_id, thread_id=thread_id)

    def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and old_title != new_title:
            log.info("{} changed the thread title. It will be changed back".format(author_id))
            self.changeThreadTitle(old_title, thread_id=thread_id, thread_type=thread_type)

    def onNicknameChange(self, author_id, changed_for, new_nickname, thread_id, thread_type, **kwargs):
        if old_thread_id == thread_id and changed_for in old_nicknames and old_nicknames[changed_for] != new_nickname:
            log.info("{} changed {}'s' nickname. It will be changed back".format(author_id, changed_for))
            self.changeNickname(old_nicknames[changed_for], changed_for, thread_id=thread_id, thread_type=thread_type)

client = KeepBot('pandadude8@hotmail.com', 'guacamole')
client.listen()