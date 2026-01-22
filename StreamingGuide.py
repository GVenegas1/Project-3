# StreamingGuide.py
# Project 3
# Author: Gabriel Venegas
#
# This file contains classes that represent movies,
# streaming services, and a guide that tracks which
# services are streaming which movies.


class Movie:
    """Stores information about a movie."""

    def __init__(self,title, genre, director, year):
        self.__title =title
        self.__genre =genre
        self.__director = director
        self.__year =year

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def get_director(self):
        return self.__director

class StreamingService:
    """Represents one streaming service."""

    def __init__(self, name):
        self.__name = name
        self.__catalog = {}
    def get_name(self):
        return self.__name

    def add_movie(self, movie):
        title = movie.get_title()
        self.__catalog[title] = movie

    def delete_movie(self, title):
        if title in self.__catalog:
            self.__catalog.pop(title)

    def get_catalog(self):
        return self.__catalog


class StreamingGuide:
    """Manages multiple streaming services."""

    def __init__(self):
        self.__services = []
    def add_streaming_service(self, service):
        self.__services.append(service)

    def delete_streaming_service(self, name):
        for service in self.__services:
            if service.get_name() == name:
                self.__services.remove(service)
                break
    def who_streams_this_movie(self, title):
        service_names = []
        year = None

        for service in self.__services:
            catalog = service.get_catalog()

            if title in catalog:
                service_names.append(service.get_name())

                # only need the year once
                if year is None:
                    year = catalog[title].get_year()
        if len(service_names) == 0:
            return None

        return {
            'title': title,
            'year': year,
            'services': service_names
        }
if __name__ == "__main__":
    movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
    movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
    movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
    movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

    stream_serv_1 = StreamingService('Netflick')
    stream_serv_1.add_movie(movie_2)

    stream_serv_2 = StreamingService('Hula')
    stream_serv_2.add_movie(movie_1)
    stream_serv_2.add_movie(movie_4)
    stream_serv_2.delete_movie('The Seventh Seal')
    stream_serv_2.add_movie(movie_2)

    stream_serv_3 = StreamingService('Dizzy+')
    stream_serv_3.add_movie(movie_4)
    stream_serv_3.add_movie(movie_3)
    stream_serv_3.add_movie(movie_1)

    stream_guide = StreamingGuide()
    stream_guide.add_streaming_service(stream_serv_1)
    stream_guide.add_streaming_service(stream_serv_2)
    stream_guide.add_streaming_service(stream_serv_3)
    stream_guide.delete_streaming_service('Hula')

    result = stream_guide.who_streams_this_movie('Little Women')
    print(result)