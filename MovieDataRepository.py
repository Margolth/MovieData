import shelve
from collections import defaultdict

class Movie(object):
        def __init__(self):
                self.actors = []
                self.aka = []
                self.bio = ""
                self.business = []
                self.cinematographer = ""
                self.composer = ""
                self.costumer = ""
                self.countries = []
                self.director = ""
                self.distributors = []
                self.editors = []
                self.genres = []
                self.goofs = []
                self.languages = []
                self.literature = ""
                self.links = []
                self.locations = []
                self.plot = ""
                self.producers = []
                self.quotes = []
                self.rating = ""
                self.release = ""
                self.runtime = ""
                self.sound = ""
                self.soundtrack = []
                self.sfx = ""
                self.title = ""
                self.tagline = []
                self.trivia = []
                self.user_rating = ""
                self.writers = []


        def set_data(self, data, member):
                if member == 'actors':
                        self.actors = data
                elif member == 'director':
                        self.director = data
                elif member == 'goofs':
                        self.goofs = data
                elif member == 'release':
                        self.release == data
                elif member == 'runtime':
                        self.runtime = data
                elif member == 'soundtrack':
                        self.soundtrack = data
                elif member == 'title':
                        self.title = data
                elif member == 'trivia':
                        self.trivia = data
                else:
                        print "datatype does not exist in Movie class"
                

        def create_dictionary(self):
                return {"actors" : self.actors,
                        "director" : self.director,
                        "goofs" : self.goofs,
                        "release" : self.release,
                        "title" : self.title,
                        "trivia" : self.trivia}

        
class MovieDataRepository(object):
        def __init__(self, shelf, dictionary):
                self.shelf = shelve.open(shelf)
                if self.shelf.has_key(dictionary):
                        self.dictionary = shelf[dictionary]
                else:
                        self.dictionary = defaultdict(Movie)

        """
        Works for datafiles in the same format as trivia.list
        Parameters: takes the name of a datafile to pull the data out of and the
        name of the type of data in the Movie object you want to modify.
        """
        def set_trivia_data(self,datafile, datatype):
                f = open(datafile)
                lines = f.readlines()[:50]

                #first grab the first instance of a title - starts with '#'
                x = 0
                while not lines[x].startswith('#'):
                        x += 1

                title = lines[x]

                #then the first instance of some piece of data - starts with '-'
                while not lines[x].startswith('-'):
                        x += 1

                data = []
                currline = lines[x]

                for l in lines[x+1:]:
                        if l.startswith('#'):
                                data.append(currline.replace('\n', ''))
                                self.dictionary[title].set_data(data, datatype)
                                title = l
                                data = []
                                currline = ""
                        else:
                                if l != '\n':
                                        if l.startswith('-'):
                                                if len(currline) > 1:
                                                        data.append(currline.replace('\n', ''))
                                                currline = l
                                        else:
                                                currline += l

m = MovieDataRepository("MovieShelf", "MovieDict")
m.set_trivia_data("trivia.list", "trivia")
m.set_trivia_data("goofs.list", "goofs")


