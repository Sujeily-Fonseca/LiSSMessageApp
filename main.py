from flask import Flask, request
from handlers.group import GroupHandler
from handlers.contact import ContactHandler
from handlers.message import MessageHandler
from handlers.user import UserHandler
from handlers.reaction import ReactionHandler
from handlers.participants import ParticipantsHandler
from handlers.hashtag import HashtagHandler
from handlers.hashtagInMessage import HashtagInMessage
app = Flask(__name__)


@app.route('/')
def root():
    return "ola k ase?"

@app.route('/MessageApp')                                                   #WORKS
def messageApp():
    return "Welcome to DB Messaging App!"


@app.route('/MessageApp/Auth/login')                                        #WORKS
def login():
    #store user ID
    return "You are now logged in."

@app.route('/MessageApp/Auth/register')                                     #WORKS
def register():
    return "You are now registered as name and last name"

#USER

@app.route('/MessageApp/users')                                             #WORKS
def getAllUsers():
    return UserHandler().getAllUsers()

#CONTACT

@app.route('/MessageApp/contacts/<int:id>')
def getAllContactsFor(id):
    return ContactHandler.getAllContacts(id)

#CHATS

@app.route('/MessageApp/chats/add')                                         #WORKS
def addToGroup():
    return 'Contact has been added to the group chat!'

@app.route('/MessageApp/chats/<int:id>')                                    #WORKS
def getGroupByID(id):
    return GroupHandler().getGroupById(id)

@app.route('/MessageApp/chats')                                             #WORKS
def searchGroupByName():
    if request.args:
        return GroupHandler().searchGroupByName(request.args)
    else:
        handler = GroupHandler()
        return handler.getAllGroups()


@app.route('/MessageApp/chats/user/<int:uid>')
def UsersOfGroupId(uid):
    return ParticipantsHandler().getAllGroupsForUser(uid)

@app.route('/MessageApp/user/chats/<int:cid>')
def GroupsOfUserId(cid):
    return ParticipantsHandler().getAllUsersOnGroup(cid)


@app.route('/MessageApp/chats/<int:id>/owner')                              #WORKS
def getOwnerFromChatId(id):
    return UserHandler().getUserById(GroupHandler().getOwnerOfGroup(id))


#MESSAGES AND CHATS

@app.route('/MessageApp/messages/chats/<int:cid>')                          #WORKS
def messagesFromGroupId(cid):
    return MessageHandler().searchMessagesByGroupId(cid)

@app.route('/MessageApp/messages/chats/<int:cid>/user/<int:uid>')           #WORKS
def messagesOfUserFromGroup(cid,uid):
    return MessageHandler().searchMessagesOfUserFromGroup(cid,uid)

@app.route('/MessageApp/messages')                                          #WORKS
def messagesByChatName():
    handler = MessageHandler()
    return handler.getAllMessages()

@app.route('/MessageApp/messages/<int:uid>')                                #WORKS
def messagesByUserId(uid):
    return MessageHandler().searchMessagesByUserId(uid)

#REACTIONS

@app.route('/MessageApp/likes/<int:id>')                                    #WORKS
def likesFromUser(id):
    return ReactionHandler().getAllUserLikes(id)

@app.route('/MessageApp/dislikes/<int:id>')                                 #WORKS
def dislikesFromUser(id):
    return ReactionHandler().getAllUserDislikes(id)

@app.route('/MessageApp/messageslikes/<int:mid>')                           #WORKS
def allMessagesLikes(mid):
    return ReactionHandler().getAllMessageLikes(mid)

@app.route('/MessageApp/messagesdislikes/<int:mid>')                        #WORKS
def allMessagesDisslikes(mid):
    return ReactionHandler().getAllMessageDislikes(mid)

@app.route('/MessageApp/hashtags')                                          #WORKS
def getAllHashtagsByName():
    if request.args:
        return HashtagHandler().getHashtagByName(request.args)
    else:
        handler = HashtagHandler()
        return handler.getAllHashtags()

@app.route('/MessageApp/hashtags/messages/<int:id>')                         #WORKS
def hashtagInMessages(id):
    return HashtagHandler().getHashtagsInMessage(id)


if __name__ == '__main__':
    app.run()
