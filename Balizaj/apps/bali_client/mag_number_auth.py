from ldap3 import Server, Connection, SUBTREE
from ldap3.core.exceptions import LDAPPasswordIsMandatoryError
import json


class Auth:
    # __SERVER = 'ad.lmru.tech:389'
    __SERVER = '10.220.8.235:389'
    __AD_TREE = 'OU=Leroy Merlin Vostok,DC=hq,DC=ru,DC=corp,DC=leroymerlin,DC=com'

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.shop_verbose = self.__connect()['physicalDeliveryOfficeName']
        self.shop_number = self.__connect()['postOfficeBox']
        self.group = self.__group()

    def __connect(self):
        attr = {}
        conn = Connection(Server(self.__SERVER), user=self.login + '@leroymerlin.ru', password=self.password)
        try:
            conn.bind()
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
        except LDAPPasswordIsMandatoryError:
            attr['physicalDeliveryOfficeName'] = None
            attr['postOfficeBox'] = None
            return attr

    def user_valid(self):
        if self.shop_verbose and self.shop_number is not None:
            return True
        else:
            return False

    def __group(self):
        self.group = ''
        if self.user_valid():
            group_attr = self.login
            if group_attr[:11] == 'bali001.mag':
                self.group = 'bali'
                return self.group
            else:
                self.group = 'client'
                return self.group
