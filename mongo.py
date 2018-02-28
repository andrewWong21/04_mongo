''' 
A collection of happy GIFs from Giphy

http://api.giphy.com/v1/gifs/search?q=happy&api_key=dc6zaTOxFJmzC

Creates db called neverGonnaGifYouUp with a collection called gifs
'''

import pymongo
import urllib2
import json

connection = pymongo.MongoClient('homer.stuy.edu')

db = connection.test
collection = db.restaurants

def findBorough(borough):
    restaurants = []
    for restaurant in db.restaurants.find({'borough': borough}):
        restaurants.append(restaurant)
    return restaurants
def findZip(zipcode):
    restaurants = []
    for restaurant in db.restaurants.find({'address.zipcode': zipcode}):
        restaurants.append(restaurant)
    return restaurants

def findZipWithGrade(zipcode, grade):
    restaurants = []
    for restaurant in db.restaurants.find({'address.zipcode': zipcode, 'grades.grade': grade}):
        restaurants.append(restaurant)
    return restaurants
    
def findZipWithScore(zipcode, score):
    restaurants = []
    for restaurant in db.restaurants.find({'address.zipcode': zipcode, 'grades.score': {'$lt': score}}):
        restaurants.append(restaurant)
    return restaurants

# does something clever - finds restaurants with a certain zipcode and cuisine
def doSomethingClever():
    restaurants = []
    for restaurant in db.restaurants.find({'address.zipcode': zipcode, 'grades.score': {'$lt': score}}):
        restaurants.append(restaurant)
    return restaurants

#print findBorough('Manhattan')
#print findZip('10017')
#print findZipWithGrade('10017', 'A')
#print findZipWithScore('10017', 5)

db = connection.neverGonnaGifYouUp

collection = db.gifs

u = urllib2.urlopen("http://api.giphy.com/v1/gifs/search?q=happy&api_key=dc6zaTOxFJmzC")
x = u.read()
data = json.loads(x)
data = data['data']
collection.insert_many(data)

