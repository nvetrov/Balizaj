from ldap3 import Server, Connection, SUBTREE
import json

class Auth:
    __SERVER = 'ad.lmru.tech:389'
    __AD_TREE = 'OU=Leroy Merlin Vostok,DC=hq,DC=ru,DC=corp,DC=leroymerlin,DC=com'

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.shop_verbose = self.__connect()['physicalDeliveryOfficeName']
        self.shop_number = self.__connect()['postOfficeBox']

    def __connect(self, attr={}):
        conn = Connection(Server(self.__SERVER), user=self.login + '@leroymerlin.ru', password=self.password)
        if conn.bind():
            search_filter = ('(&(objectCategory=Person)(sAMAccountName={}))').format(self.login)
            conn.search(self.__AD_TREE, search_filter, SUBTREE,
                        attributes=['physicalDeliveryOfficeName', 'postOfficeBox'])
            attr = json.loads(conn.response_to_json())
            attr = attr['entries'][0]['attributes']
            attr['postOfficeBox'] = attr['postOfficeBox'][0]
            return attr
        else:
            attr['physicalDeliveryOfficeName'] = None
            attr['postOfficeBox'] = None
            return attr

    def user_valid(self):
        if self.shop_verbose and self.shop_number is not None:
            return True
        else:
            return False