#Author: Gabriel Venegas
#Github:GVenegas1
#Date: Jan 21,2026
#Description: This file contains classes that represent movies,
#streaming services, and a guide that tracks which
#services are streaming which movies.

class Movie:
    """Stores information about a movie."""
    def __init__(self,title,genre,director,year):
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
    def __init__(self,name):
        self.__name= name
        self.__catalog ={}
    def get_name(self):
        return self.__name

    def add_movie(self, movie):
        title =movie.get_title()
        self.__catalog[title]= movie

    def delete_movie(self,title):
        if title in self.__catalog:
            self.__catalog.pop(title)

    def get_catalog(self):
        return self.__catalog

class StreamingGuide:
    """Manages multiple streaming services."""
    def __init__(self):
        self.__services = []
    def add_streaming_service(self,service):
        self.__services.append(service)

    def delete_streaming_service(self,name):
        for service in self.__services:
            if service.get_name()== name:
                self.__services.remove(service)
                break
    def who_streams_this_movie(self, title):
        service_names= []
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
