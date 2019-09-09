from imdb import IMDb
import imdb.helpers
import imdb.Movie

# create an instance of the IMDb class
ia = IMDb()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])

# # show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# # show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('runtime'))
print(imdb.helpers.fullSizeCoverURL(the_matrix))
m1 = Movie("Avengers")
print(m1.getID)


# search_results = ia.search_movie('A Star Is Born (2018)')

# if search_results:
#      movieID = search_results[0].movieID
#      movie = ia.get_movie(movieID)
#      if movie:
#          cast = movie.get('cast')
#          topActors = 5
#          for actor in cast[:topActors]:
#             print("{0} as {1}".format(actor['name'], actor.currentRole))