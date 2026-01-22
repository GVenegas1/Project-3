# project-3

**Remember that classes must not directly access the private data members of other classes, but instead must call the appropriate get methods.**

First, write a class named **Movie** that has four data members: **title**, **genre**, **director**, and **year**. It should have:
* an init method that takes as arguments the title, genre, director, and year (in that order) and assigns them to the data members. The year is an integer and the others are strings.
* get methods for each of the data members (**get_title**, **get_genre**, **get_director**, and **get_year**).

Hint: Remember the difference between a **class** and an **object**. The class is just a blueprint for making objects. For example, don't try to ask the Movie class for its title. It doesn't have one and it doesn't know anything about any Movie objects that may have been created.

Next write a class named **StreamingService** that has two data members: **name** and **catalog**. The catalog is a dictionary of Movies, with the titles as the keys and the Movie objects as the corresponding values (you can assume there aren't any Movies with the same title). The StreamingService class should have:
* an init method that takes the name as an argument, and assigns it to the name data member. The catalog data member should be initialized to an empty dictionary.
* get methods for each of the data members (**get_name** and **get_catalog**).
* a method named **add_movie** that takes a Movie object as an argument and adds it to the catalog.
* a method named **delete_movie** that takes a movie title as an argument and if that Movie is in the catalog, removes it.

Lastly, write a class named **StreamingGuide** that has one data member, a list of StreamingService **objects** (you can assume there aren't any StreamingServices with the same name). It should have:
* an init method that takes no arguments and initializes the data member to an empty list.
* a method called **add_streaming_service** that takes a StreamingService object as an argument and adds it to the list.
* a method named **delete_streaming_service** that takes the name of a streaming service as an argument and if it's in the list, removes it.
* a method named **who_streams_this_movie** that takes a movie title as a parameter and returns either a dictionary or the value None. The dictionary should contain 3 key-value pairs with the keys 'title', 'year', and 'services'. The value for 'title' should be the title of the movie (which was passed to this function as a parameter). The value for 'year' should be the year of that movie, as an integer. The value for 'services' should be a list of the names of the streaming services showing that movie. If the movie is not available on any of the StreamingServices, then instead of returning a dictionary, the method should return None.

So a StreamingGuide will have a list of StreamingService objects, and a Streaming Service will have a dictionary of Movie objects. The who_streams_this_movie method needs to use this nested information to determine which StreamingServices, if any, have the desired movie available.

All the data members should be private.

Here's a simple example of how your code might be used:
```
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
search_results = stream_guide.who_streams_this_movie('Little Women')
```

Your file must be named **StreamingGuide.py**.

