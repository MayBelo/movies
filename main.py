from reading_functions import read_movies_from_file,read_screening_from_file

#####searching functions#####

def search_by_name(all_movies):
    results = []
    while True:
        movie_by_name = input("please enter a movie name")
        for movie in all_movies:
            if movie_by_name in movie.name:
                results.append(movie)
        if results:
            break
        else:
            print("movie was not found")
    return results

def search_by_genre(all_movies):
    results = []
    while True:
        movie_by_genre = input("please enter a movie genre")
        for movie in all_movies:
            if movie_by_genre in movie.genre:
                results.append(movie)
        if results:
            break
        else:
            print("genre was not found")
    return results

def search_by_year(all_movies):
    results = []
    while True:
        movie_by_year = input("please enter a movie year")
        for movie in all_movies:
            if movie_by_year in movie.year:
                results.append(movie)
        if results:
            break
        else:
            print("year was not found")
    return results

####searching by category####

def search_movie():
    all_movies = read_movies_from_file()
    search_str = input("would you like to find a movie by name/genre/year or to show all the movies?")

    if search_str == "name":
        results = search_by_name(all_movies)
        for result in results:
            print(result)

    if search_str == "genre":
        results = search_by_genre(all_movies)
        for result in results:
            print(result)

    if search_str == "year":
        results = search_by_year(all_movies)
        for result in results:
            print(result)

    if search_str == "show all the movies":
        results = all_movies
        for result in results:
            print(result)

#####buying tickets functions######

def tickets(selected_movie,number_of_tickets):
    all_movies = read_movies_from_file()
    for movie in all_movies:
            if selected_movie in movie.name:
                    if movie.hall.vip == "yes\n":
                        print("this movie is at the VIP hall,you need to pay",int(number_of_tickets*140))
                    else:
                        print("you need to pay",int(number_of_tickets*40))

####printing the screening date####

def screening_movie(selected_movie):
    all_screening = read_screening_from_file()
    for screening in all_screening:
        if screening.name == selected_movie:
            print("the screenings are at this dates:")
            print(screening)

#####adding a movie#####

def add_movie():
    main = input("would you like to add a new movie to the list?")
    if main == "yes":
        print("please enter a movie name,length,genre,pg,year")
        new_movie_name = input("please enter a movie name")
        new_movie_length = input("please enter a movie length")
        new_movie_genre = input("please enter a movie genre")
        new_movie_pg = input("please enter a movie pg")
        new_movie_year = input("please enter a movie year")
        with open("movies1.csv","a") as new_movie_file:
            # do not forget to change the file to the original name
            new_movie_file.write(new_movie_name+","),
            new_movie_file.write(new_movie_length+","),
            new_movie_file.write(new_movie_genre+","),
            new_movie_file.write(new_movie_pg+","),
            new_movie_file.write(new_movie_year)

    else:
        print("ok! thank you!")

###### MAIN PROGRAM ######
search_movie()
selected_movie = input("which movie would you like to watch?")
screening_movie(selected_movie)
number_of_tickets = int(input("how many tickets would you like?"))
tickets(selected_movie,number_of_tickets)
add_movie()