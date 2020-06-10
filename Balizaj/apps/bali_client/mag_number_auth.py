from ldap3 import Server, Connection, SUBTREE
import json


class Auth:
    server = 'ad.lmru.tech:389'

    def __init__(self, login, password):
        self.login = login + '@leroymerlin.ru'
        self.password = password

    def connect(self):
        conn = Connection(Server(Auth.server), user=self.login, password=self.password)
        return conn.bind()

    def search(self):
        if self.connect():
            print('Yeap')
        else:
            print('Nope')

a = Auth('60075381', '528465Aza!')

a.search()