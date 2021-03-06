#reaction table: lID, lvalue, isValid, userID, msgID

import psycopg2

class ReactionsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllUserLikes(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='1' AND isValid='1' AND users.userID=%s"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllUserLikesIllegal(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='1' AND users.userID=%s"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserDislikesIllegal(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='0' AND users.userID=%s"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageLikes(self, msgID):
        cursor = self.conn.cursor()
        query = "SELECT fname, lname FROM users NATURAL INNER JOIN reactions WHERE lvalue='1' AND isValid='1' AND msgID=%s;"
        cursor.execute(query, (msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserDislikes(self, userID):
        cursor = self.conn.cursor()
        query = "SELECT msgID FROM (users NATURAL INNER JOIN reactions) INNER JOIN messages using(msgID) " \
                "WHERE lvalue='0' AND isValid='1' AND users.userID=%s"
        cursor.execute(query, (userID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessageDislikes(self, msgID):
        cursor = self.conn.cursor()
        query = "SELECT fname, lname FROM users NATURAL INNER JOIN reactions WHERE lvalue='0' AND isValid='1' AND msgID=%s;"
        cursor.execute(query, (msgID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfLikes(self,msgID):
        cursor = self.conn.cursor()
        query = "SELECT num from (SELECT m.message, count(*) as num FROM reactions INNER JOIN messages AS m USING(msgID) WHERE lvalue='1' AND isValid='1' AND msgID=%s GROUP BY m.message) as A;"
        cursor.execute(query, (msgID,))
        result = cursor.fetchone()
        return result

    def getNumberOfDislikes(self,msgID):
        cursor = self.conn.cursor()
        query = "SELECT num from (SELECT m.message, count(*) as num FROM reactions INNER JOIN messages AS m USING(msgID) WHERE lvalue='0' AND isValid='1' " \
                "AND msgID=%s GROUP BY m.message) as A;"
        cursor.execute(query,(msgID,))
        result = cursor.fetchone()
        return result

    def validateReaction(self, msgID, userID):
        cursor = self.conn.cursor()
        query = "SELECT isValid from reactions where msgID = %s and userID = %s;"
        cursor.execute(query,(msgID,userID,))
        result = []
        for row in cursor:
            result.append(row)
        if(len(result) != 0 and '0' in result[0]):
            return False
        return True

    def insertReactionToMsg(self, reactionVal, userID, msgID):
        cursor = self.conn.cursor()
        liked = self.getAllUserLikes(userID)
        disliked = self.getAllUserDislikes(userID)
        likedIllegal = self.getAllUserLikesIllegal(userID)
        dislikedIllegal = self.getAllUserDislikesIllegal(userID)

        if (len(liked) != 0 and ((int(msgID),) in liked and int(reactionVal) == 1))\
                or (len(disliked) != 0 and ((int(msgID),) in disliked and int(reactionVal) == 0)):
            print("was liked and pressed like or was disliked and pressed dislike")
            query = "UPDATE reactions SET isValid= B'0', dateStamp = current_date AT TIME ZONE 'AST' where UserID = %s and msgID = %s;"
            cursor.execute(query, (userID, msgID,))


        elif len(liked) != 0 and ((int(msgID),) in liked and int(reactionVal) == 0):
            print("was liked and pressed dislike")
            query = "UPDATE reactions SET lValue= B'0', dateStamp =  current_date AT TIME ZONE 'AST' where UserID = %s and msgID = %s;"
            cursor.execute(query, (userID, msgID,))

        #
        elif len(disliked) != 0 and ((int(msgID),) in disliked and int(reactionVal) == 1):
            print("was disliked and pressed like")
            query = "UPDATE reactions SET lValue= B'1', dateStamp = current_date AT TIME ZONE 'AST' where UserID = %s and msgID = %s;"
            cursor.execute(query, (userID, msgID,))

        #
        elif ((len(likedIllegal) != 0 or len(dislikedIllegal) != 0)) and not self.validateReaction(msgID, userID):
            print("pressed like on a message that had been liked before,etc")
            query = "UPDATE reactions SET lValue = %s, isValid = B'1', dateStamp = current_date AT TIME ZONE 'AST' where userID = %s and msgID = %s;"
            cursor.execute(query,(reactionVal, userID, msgID,))

        #
        else:
            print("new reaction")
            query = "INSERT INTO reactions (isValid, lValue, msgId, userId, dateStamp) values (B'1', %s, %s, %s, current_date AT TIME ZONE 'AST');"
            cursor.execute(query, (reactionVal, msgID, userID,))
        self.conn.commit()
        result = []
        x = self.getNumberOfLikes(msgID)
        y = self.getNumberOfDislikes(msgID)
        if not x is None:
            result.append(x)
        else:
            result.append (0)

        if not y is None:
            result.append(y)
        else:
            result.append(0)

        return result