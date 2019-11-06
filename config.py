import ssl
import os
import urllib
from pymongo import MongoClient

username = 'neargroup'
password = 'neargroup@1234'
mongoURI = f'mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@ngapp-qfeen.mongodb.net/neargroup?retryWrites=true'
myclient = MongoClient(mongoURI, ssl_cert_reqs=ssl.CERT_NONE)

db = myclient['locationDatabase']
