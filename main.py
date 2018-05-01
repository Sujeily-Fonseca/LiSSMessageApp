from flask import Flask, request
from handlers.group import GroupHandler
from handlers.contact import ContactHandler
from handlers.message import MessageHandler
from handlers.user import UserHandler
from handlers.reactions import ReactionsHandler
from handlers.participants import ParticipantsHandler
from handlers.hashtag import HashtagHandler
from handlers.contains import ContainsHandler

app = Flask(__name__)


###################################################################
@app.route('/')
def root():
    return "Home"


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
###################################################################


#REPLIES
@app.route('/MessageApp/replies/<int:id>')                                  #WORKS REMOTE DB
def repliesOfMessage(id):
    return MessageHandler().getRepliesForMessage(id)


@app.route('/MessageApp/messages/<int:id>')                                 #WORKS REMOTE DB
def getMessageBymsgId(id):
    return MessageHandler().getMessageByMsgId(id)


@app.route('/MessageApp/messages/replied/<int:id>')                         #WORKS REMOTE DB
def getMessageThatReplied(id):
    return MessageHandler().getMessageThatReplied(id)


#USERS
@app.route('/MessageApp/users/<int:id>')                                    #WORKS REMOTE DB
def getUserByID(id):
    return UserHandler().getUserById(id)


@app.route('/MessageApp/users')                                             #WORKS REMOTE DB
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUser(request.args)

#CONTACT
@app.route('/MessageApp/contacts/<int:id>')                                 # WORKS REMOTE DB
def getAllContactsFor(id):
    return UserHandler().getUserContacts(id)


#MESSAGES AND CHATS
@app.route('/MessageApp/messages/groups/<int:cid>')                         #WORKS REMOTE DB
def messagesFromGroupId(cid):
    return MessageHandler().searchMessagesByGroupId(cid)


@app.route('/MessageApp/messages/groups/<int:cid>/user/<int:uid>')          #WORKS REMOTE DB
def messagesOfUserFromGroup(uid,cid):
    return MessageHandler().searchMessagesOfUserFromGroup(uid,cid)


@app.route('/MessageApp/messages')                                          #WORKS REMOTE DB
def messagesByChatName():
    return MessageHandler().getAllMessages()


@app.route('/MessageApp/messages/user/<int:uid>')                           #WORKS REMOTE DB
def messagesByUserId(uid):
    return MessageHandler().searchMessagesByUserId(uid)


@app.route('/MessageApp/groups/<int:id>/owner')                             #WORKS REMOTE DB
def getOwnerFromGroupId(id):
    return GroupHandler().getOwnerOfGroup(id)

#CHATS
@app.route('/MessageApp/groups/add')                                        #WORKS REMOTE DB
def addToGroup():
    return 'Contact has been added to the group chat!'


@app.route('/MessageApp/groups/<int:id>')                                   #WORKS REMOTE DB
def getGroupByID(id):
    return GroupHandler().getGroupById(id)


@app.route('/MessageApp/groups')                                            #WORKS REMOTE DB
def searchGroupByName():
    if request.args:
        return GroupHandler().searchGroupByName(request.args)
    else:
        handler = GroupHandler()
        return handler.getAllGroups()

#HASHTAGS
@app.route('/MessageApp/hashtags')                                          #WORKS REMOTE DB
def getAllHashtags():
    if request.args:
        return HashtagHandler().getHashtagByName(request.args)
    else:
        return HashtagHandler().getAllHashtags()


#PARTICIPANTS
@app.route('/MessageApp/chats/user/<int:uid>')                              #WORKS REMOTE DB
def UsersOfGroupId(uid):
    return ParticipantsHandler().getAllGroupsForUser(uid)

@app.route('/MessageApp/user/chats/<int:cid>')                              #WORKS REMOTE DB
def GroupsOfUserId(cid):
    return ParticipantsHandler().getAllUsersOnGroup(cid)

@app.route('/MessageApp/participants')                           #WORKS REMOTE DB
def getAllParticipants():
    return ParticipantsHandler().getAllParticipants()

#REACTIONS
@app.route('/MessageApp/likes/<int:id>')                        #WORKS REMOTE DB
def likesFromUser(id):
    return ReactionsHandler().getAllUserLikes(id)


@app.route('/MessageApp/dislikes/<int:id>')                     #WORKS REMOTE DB
def dislikesFromUser(id):
    return ReactionsHandler().getAllUserDislikes(id)


@app.route('/MessageApp/messageslikes/<int:mid>')               #WORKS REMOTE DB
def allMessagesLikes(mid):
    return ReactionsHandler().getAllMessageLikes(mid)


@app.route('/MessageApp/messagesdislikes/<int:mid>')            #WORKS REMOTE DB
def allMessagesDislikes(mid):
    return ReactionsHandler().getAllMessageDislikes(mid)


#CONTAINS
@app.route('/MessageApp/hashtags/message/<int:mid>')            #WORKS REMOTE DB
def HashIn(mid):
    return ContainsHandler().getHashIn(mid)

@app.route('/MessageApp/message/hashtag/<int:hid>')             #WORKS REMOTE DB
def MsgsWith(hid):
    return ContainsHandler().getMsgsWith(hid)


if __name__ == '__main__':
    app.run()
