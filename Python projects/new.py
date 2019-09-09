import os, csv, pandas as pd
from imdb import IMDb
from IPython.display import display, HTML

def pretty_print(data):
    return display(HTML(data.to_html().replace("\\n","<br>")))

# create an instance of the IMDb class
ia = IMDb()

path='E:/Movies/English'

print("End of first print\nEnd of first print\nEnd of first print\nEnd of first print\n")

# For printing with filenames:
# with open('C:/Users/GamerTech/Desktop/sample2.csv', 'w+', newline='') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['Movie Name', 'Files'])
#   for dirpath, dirs, filenames in os.walk(path, topdown=True):
#     dirs.sort()
#     if filenames:
#       writer.writerow([os.path.basename(dirpath)] + sorted(filenames))

#For printing only foldernames (parent and subdirectory):
with open('C:/Users/GamerTech/Desktop/sample2.csv', 'w+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Movie Name'])
    for (dirpath, dirnames, filenames) in os.walk(path, topdown=True):
        dirnames.sort()
        if filenames:
            writer.writerow([os.path.basename(dirpath)])

# For Printing as "DirEntry" objects from the list
# with open('C:/Users/GamerTech/Desktop/sample2.csv', 'w+', newline='') as csvfile, os.scandir('E:/Movies/English') as entries:
#      writer = csv.writer(csvfile)
#      writer.writerow(['Movie Name'])
#      for entry in entries:
#         writer.writerow([entry])

#creating a dataframe to split the moviename from the rest of the string
data = pd.read_csv("C:/Users/GamerTech/Desktop/sample2.csv") 
  
# removing null values if any to avoid errors 
data.dropna(how ='all', inplace = True) 
  
data.head() 
new = data["Movie Name"].str.partition(" (", True) 

data["Movie Name"]= new[0] 
data["Rest Data"]= new[2] 
data["Cast Info"] = ""
print(data)
totalmovie=len(data["Movie Name"])
print(totalmovie)

#looping through dataframe's movie name column 

for i in range (0,totalmovie,1):
    for entry in data.iloc[i]:
        search_results = ia.search_movie(entry)
        if search_results:
            movieID = search_results[0].movieID
            movie = ia.get_movie(movieID)
            print(movieID," : ",movie)
            if movie:
                cast = movie.get('cast')
                actoriter=0
                topActors = 5
                emptylist=[]
        
                for actor in cast[actoriter:topActors]:
                    cast=("{0} as {1}".format(actor['name'], actor.currentRole))
                    print(cast)
                    emptylist.extend([cast])
                    actoriter=actoriter+1
            data.at[i,'Cast Info'] = emptylist
            
data.to_csv(r'C:/Users/GamerTech/Desktop/sample2.csv',index = None, header=True)
