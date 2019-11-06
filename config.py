import ssl
import os
import urllib
from pymongo import MongoClient

username = '*********'
password = '*************'
mongoURI = f'mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@ngapp-qfeen.mongodb.net/neargroup?retryWrites=true'
myclient = MongoClient(mongoURI, ssl_cert_reqs=ssl.CERT_NONE)

db = myclient['locationDatabase']
