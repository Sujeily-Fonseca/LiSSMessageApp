#contains table: containsID, msgID, hashtagID
from dao.containsDAO import ContainsDAO

from flask import jsonify

class ContainsHandler:

    def mapToDict(self, row):
        result = {}
        result['containsID'] = row[0]
        result['msgID'] = row[1]
        result['hashtagID'] = row[2]
        return result

    def hashtagsToDict(self, row):
        result = {}
        result['hashString'] = row[0]
        return result

    def messagesToDict(self, row):
        result = {}
        result['message'] = row[0]
        return result

    def getHashIn(self, msgID):
        dao = ContainsDAO()
        results = dao.getHashIn(msgID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.hashtagsToDict(r))
        return jsonify(Hashtags=mapped_results)

    def getMsgsWith(self,hashtagID):
        dao = ContainsDAO()
        results = dao.getMsgsWith(hashtagID)
        mapped_results = []
        for r in results:
            mapped_results.append(self.messagesToDict(r))
        return jsonify(Hashtags=mapped_results)