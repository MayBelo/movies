class Hall:
    def __init__(self,num_hall,seats,vip,price=40,vip_price=140):
        self.num_hall = num_hall
        self.seats = seats # you are not using seats.
        self.vip = vip
        self.price = price # you dont need 2 prices. if its vip so the price is vip.
        self.vip_price = vip_price

    def __str__(self):
        return f"{self.num_hall},{self.seats},{self.vip},{self.price},{self.vip_price}"

class Screening:
    # I think you should have just one parameter like a dictionary of screening times
    # self.screen{"day":[times]}
    # or maybe even add a new class for that - that has day, time.
    # also - what about number of tickets?
    def __init__(self,name,sunday,monday,tuesday,wednesday,thursday,friday,saturday):
        self.name = name
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

    def __str__(self):
        return f"{self.name},{self.sunday},{self.monday}," \
               f"{self.tuesday},{self.wednesday},{self.thursday},{self.friday},{self.saturday}"


class Movie:
    def __init__(self,name,length,genre,pg,year,hall,screening):
        self.name = name
        self.length = length
        self.genre = genre
        self.pg = pg
        self.year = year
        self.hall = hall
        self.screening = screening

    def __str__(self):
        return f"{self.name},{self.length},{self.genre},{self.pg},{self.year}"




