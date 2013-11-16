from .constants import *

try:
    import requests
except:
    pass

class PyDataGovPH(object):

    def __init__(self, app_id):
        
        self.app_id = app_id


    def __dataGet(self, node, param={}):

        try:
            param['app_id'] = self.app_id
            res = requests.get("%s%s" % (API_ENDPOINT, node), data=param)
            return res.json() 
        except:
            return {}

    def getBudget(self, param={}):

        data = {
            'type': APP_TYPE_NEW,
            'department_code': '',
            'owner_code': '',
            'agency_type': '',
            'owner_desc': '',
            'department_desc': '',
            'year': '',
            'limit': '',
            'skip': ''
        }

        data.update(param)
        return self.__dataGet(API_NODE_BUDGET, data)

    def getBudgetCount(self):
        return self.__dataGet("%s%s" % (API_NODE_BUDGET, API_NODE_COUNT))

    def getSAOB(self, param={}):

        data = {
            'year': '',
            'period': '',
            'agency': '',
            'limit': '',
            'skip': ''
        }

        data.update(param)
        return self.__dataGet(API_NODE_SAOB, data)

    def getSAOBCount(self):
        return self.__dataGet("%s%s" % (API_NODE_SAOB, API_NODE_COUNT))

    def getSARO(self, param={}):

        data = {
            'department_code': '',
            'agency_code': '',
            'year': '',
            'region': '',
            'limit': '',
            'skip': ''
        }

        data.update(param)
        return self.__dataGet(API_NODE_SARO, data)

    def getSAROCount(self):
        return self.__dataGet("%s%s" % (API_NODE_SARO, API_NODE_COUNT))

    def getTotal(self):
        return self.__dataGet(API_NODE_TOTAL)

