import pymongo

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

#print findBorough('Manhattan')
#print findZip('10017')
#print findZipWithGrade('10017', 'A')
print findZipWithScore('10017', 5)
