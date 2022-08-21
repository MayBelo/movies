from models import Movie,Hall,Screening

def read_screening_from_file():
    with open("screening1.csv") as screening_file:
        screening_file.readline()
        all_screening = []
        for line0 in screening_file:
            templist = line0.split(",")
            screening = Screening(name=templist[0],
                                  sunday=templist[1],
                                  monday=templist[2],
                                  tuesday=templist[3],
                                  wednesday=templist[4],
                                  thursday=templist[5],
                                  friday=templist[6],
                                  saturday=templist[7])
            # better to do some logic here not just read strings to Class
            all_screening.append(screening)
    return all_screening

def read_movies_from_file():
    with open("movies1.csv") as movie_file:
        movie_file.readline()
        all_movies = []
        for line in movie_file:
            templist = line.split(",")
            hall = Hall(num_hall=templist[5], seats=templist[6], vip=templist[7], price=40, vip_price=140)
            movie = Movie(name=templist[0],
                          length=templist[1],
                          genre=templist[2],
                          pg=templist[3],
                          year=templist[4],
                          hall=hall,
                          screening=read_screening_from_file())
                        # you are adding all screenings to each movie? not a good idea :)
            all_movies.append(movie)
    return all_movies

