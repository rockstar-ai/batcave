from imdb import IMDb
import imdb.helpers

# create an instance of the IMDb class
ia = IMDb()

# get a movie
movie = ia.get_movie('0133093')

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)

# search for a person name
people = ia.search_person('Mel Gibson')
for person in people:
   print(person.personID, person['name'])


# ia = IMDb('http')
# m = ia.get_movie('0499549') # Avatar.
# print(m['cover url']) # the 'small-sized' cover.
# print(imdb.helpers.fullSizeCoverURL(m))


# print(access.get_poster(movie))

movie = ia.get_movie(1132626)

print("title: %s year: %s" % (movie['title'], movie['year']))
print("Cover url: %s" % movie['cover url'])