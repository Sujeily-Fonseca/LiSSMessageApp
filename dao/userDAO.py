#user table: userID, fName, lName, email, phone, password

import psycopg2

class UserDAO:
    def __init__(self):
        self.conn = psycopg2.connect(database='postgres', user='liss',
                                     password='LiSSMsgApp', host='35.193.157.126')

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE userID=%s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE phone=%s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE email=%s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByfName(self, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s;"
        cursor.execute(query, (fName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByEmailAndFname(self, email, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s AND email=%s;"
        cursor.execute(query, (fName, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByPhoneAndFname(self, phone, fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE fName=%s AND phone=%s;"
        cursor.execute(query, (fName, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUsersByPhoneAndEmail(self, phone, email):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM users WHERE phone=%s AND email=%s;"
        cursor.execute(query, (phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByPhoneEmailAndfName(self,phone,email,fName):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName, email, phone FROM users WHERE phone=%s AND email=%s AND fName=%s;"
        cursor.execute(query, (phone, email,fName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserContacts(self,uid):
        cursor = self.conn.cursor()
        query = "SELECT fName, lName FROM contacts, users WHERE contactID=userID AND contactOfID=%s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
