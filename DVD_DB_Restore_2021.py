# Michael Gennery
# DVD Database
# July 2021
# Restore


import sqlite3



# Write records to the database


def add_films():
    for film in DVD_list:
        DVD_cursor.execute("""insert into DVD values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", film)



# Main Code



DVD_DB = sqlite3.connect('DVD_DB.db')
DVD_cursor = DVD_DB.cursor()


# DVD_List


DVD_list = [
(5037899058909, 'Hostage', '15', 'Thriller', 'War', 'Adam Smith', 'Eyles Gabel', 'Haeth Jones', 'Koralis Pictures', 98, 2014),
(5053083158798, 'Mission Impossible: Fallout', '12', 'Thriller', 'Spy', 'Tom Cruise', 'Simon Clegg', 'Christopher McQuarrie', 'Paramount', 141, 2018), (5051188120535, 'American Beauty', '18', 'Drama', 'Drama', 'Kevin Spacey', 'Annette Benning', 'Sam Mendes', 'Dreamworks', 117, 2006),
(5039036043885, 'Avatar', '12', 'Science Fiction', 'Adventure', 'Sam Worthington', 'Zoe Saldana', 'James Cameroon', '20th Century Fox', 180, 2009), (5051892186889, 'Focus', '15', 'Drama', 'Drama', 'Will Smith', 'Margot Robbie', 'Glen Ficarra', 'Di Novi', 100, 2014),
(5051159329653, 'Elysium', '15', 'Science Fiction', 'Earth based', 'Matt Damon', 'Jodie Foster', 'Meil Blomkamp', 'Tristar', 105, 2013),
(5039036014960, 'Minority Report', '12', 'Science Fiction', 'Future', 'Tom Cruise', 'Colin Farrell', 'Stephen Spielberg', '20th Century Fox', 139, 2002), (5060223768779, 'The Hunger Games', '12', 'Science Fiction', 'Future', 'Jennifer Lawrence', 'Josh Hutcherson', 'Gary Ross', 'Lionsgate', 137, 2012),
(5051188124137, 'Castaway', '12', 'Adventure', 'Adventure', 'Tom Hanks', 'Helen Hunt', 'Robert Zemickis', 'Dreamworks', 138, 2006),
(7321900219624, 'Training Day', '18', 'Thriller', 'Crime', 'Denzel Washington', 'Ethan Hawke', 'Antione Fuqua', 'Warner Bros', 118, 2001),
(5014437603135, 'Mission Impossible: Rogue Nation', '12', 'Thriller', 'Spy', 'Tom Cruise', 'Simon Clegg', 'Christopher McQuarrie', 'Paramount', 126, 2015),
(5051159892850, 'Captain Phillips', '12', 'True Story', 'Drama', 'Tom Hanks', 'Barkhad Abdi', 'Paul Greengrass', 'Columbia', 129, 2013),
(5035673007853, 'The Lonliness of the long distance runner', '12', 'Drama', 'Drama', 'Tom Courtenay', 'Michael Redgrave', 'Tom Richardson', 'Bryanston', 99, 1962),
(5055201825834, 'The Gunman', '15', 'Thriller', 'Crime', 'Sean Penn', 'Ray Winstone', 'Piere Morel', 'Studio Canal', 110, 2015),
(7321902144825, 'Blade Runner', '15', 'Science Fiction', 'Thriller', 'Harriosn Ford', 'Rutger Hauer', 'Ridley Scott', 'Warner Brothers', 117, 1982),
(8594160260999, 'Sunshine', '15', 'Science Fiction', 'Adventure', 'Rose Burn', 'Cliff Curtis', 'Danny Boyle', 'Fox Searchlight', 103, 2007),
(5053083028237, 'Fifty Shades of Grey', '18', 'Romance', 'Erotic', 'Dakota Johnson', 'Jamie Dornan', 'Sam Taylor-Johnson', 'Universal', 123, 2015),
(5039036074384, 'Dr. No', '15', 'Thriller', 'Spy', 'Sean Connery', 'Joseph Wiseman', 'Terence Young', 'Eon', 109, 1962),
(5039036074384, 'From Russia with Love', '15', 'Thriller', 'Spy', 'Sean Connery', 'Robert Shaw', 'Terence Young', 'Eon', 115, 1963),
(5039036074384, 'Goldfinger', '15', 'Thriller', 'Spy', 'Sean Connery', 'Gert Frobe', 'Guy Hamilton', 'Eon', 110, 1964),
(5039036074384, 'Thunderball', '15', 'Thriller', 'Spy', 'Sean Connery', 'Adolfo Celi ', 'Terence Young', 'United Artists', 130, 1965),
(5053083053390, 'Back to the Future Trilogy', 'PG', 'Science Fiction', 'Time Travel', 'Michael J. Fox', 'Christopher Lloyd', 'Robert Zemickis', 'Universal', 120, 1985),
(5039036074384, 'You Only Live Twice', '18', 'Thriller', 'Spy', 'Sean Connery', 'Donald Pleasence', 'Lewis Gilbert', 'Eon', 117, 1967),
(5039036074384, 'On Her Majestys Secret Service', '18', 'Thriller', 'Spy', 'George Lazenby', 'Telly Savalas', 'Peter R. Hunt', 'United Artists', 142, 1969),
(7321902294476, 'I am Legend', '15', 'Science Fiction', 'Future', 'Will Smith', 'Alice Braga', 'Francis Lawrence', 'Village Roadshow Pictures', 96, 2007),
(5035822007147, 'Being John Malkovich', '15', 'Drama', 'Drama', 'John Malkovich', 'John Cusack', 'Spike Jonze', 'Gramercy Pictures', 108, 2000),
(5039036074384, 'Diamonds are Forever', '18', 'Thriller', 'Spy', 'Sean Connery', 'Charles Grey', 'Guy Hamilton', 'United Artists', 120, 1971),
(5039036074384, 'Live and Let Die', '18', 'Thriller', 'Spy', 'Roger Moore', 'Yaphet Kotto', 'Guy Hamilton', 'Eon', 121, 1973),
(5055761906851, 'The Hunger Games: Mocking Jay Part 2', '12', 'Future', 'Adventure', 'Jennifer Lawrence', 'Josh Hutcherson', 'Francis Lawrence', 'Lionsgate', 131, 2015),
(5039036074384, 'The Man with the Golden Gun', '18', 'Thriller', 'Spy', 'Roger Moore', 'Christopher Lee', 'Guy Hamilton', 'United Artists', 125, 1974),
(5039036074384, 'The Spy who loved me', '18', 'Thriller', 'Spy', 'Roger Moore', 'Curd Jurgens', 'Lewis Gilbert', 'United Artists', 125, 1977),
(5039036074384, 'Moonraker', '18', 'Thriller', 'Spy', 'Roger Moore', 'Michael Lonsdale', 'Lewis Gilbert', 'Eon', 126, 1979),
(5039036074384, 'For your eyes only', '18', 'Thriller', 'Spy', 'Roger Moore', 'Julian Glover', 'John Glen', 'Eon', 127, 1981),
(5039036074384, 'Octopussy', '18', 'Thriller', 'Spy', 'Roger Moore', 'Louis Jourdan', 'John Glen', 'Eon / United Artists', 131, 1983),
(5039036074384, 'A View to a Kill', '18', 'Thriller', 'Spy', 'Roger Moore', 'Christopher Walken', 'John Glen', 'MGM', 131, 1985),
(5039036074384, 'The Living Daylights', '18', 'Thriller', 'Spy', 'Timothy Dalton', 'Joe Don Baker', 'John Glen', 'MGM/UA', 131, 1987),
(5039036074384, 'License to Kill', '18', 'Thriller', 'Spy', 'Timothy Dalton', 'Robert Davi', 'John Glen', 'Eon/UA', 133, 1989),
(5039036074384, 'Goldeneye', '18', 'Thriller', 'Spy', 'Pierce Brosnan', 'Sean Bean', 'Martin Campbell', 'Eon/UA', 130, 1995),
(5039036074384, 'Tomorrow never dies', '18', 'Thriller', 'Spy', 'Pierce Brosnan', 'Jonathan Pryce', 'Roger Spottiswoode', 'Eon/UA', 119, 1997),
(5039036074384, 'The World is not enough', '18', 'Thriller', 'Spy', 'Pierce Brosnan', 'Robert Carlyle', 'Michael Apted', 'Eon/MGM', 125, 1999),
(5039036074384, 'Die another day', '18', 'Thriller', 'Spy', 'Pierce Brosnan', 'Toby Stephens', 'Lee Tamahori', 'Eon/MGM', 133, 2002),
(5039036074384, 'Casino Royale', '18', 'Thriller', 'Spy', 'Daniel Craig', 'Mads Mikkelsen', '\tMartin Campbell', 'Eon/MGM', 144, 2006),
(5039036074384, 'Quantum of Solace', '18', 'Thriller', 'Spy', 'Daniel Craig', 'Mathieu Amalric', 'Marc Forster', 'Eon/MGM', 106, 2008),
(5051892010214, 'Before Sunrise', '15', 'Romance', 'Adventure', 'Ethan Hawke', 'Julie Deply', 'Richard Linklater', 'Castle Rock Entertainment', 97, 1995),
(5051892010214, 'Before Sunset', '15', 'Romance', 'Adventure', 'Ethan Hawke', 'Julie Deply', 'Richard Linklater', 'Castle Rock Entertainment', 77, 2009),
(5050582529401, 'The Kingdom', '15', 'Thriller', 'Crime', 'Jamie Foxx', 'Chris Cooper', 'Peter Berg', 'Universal Pictures', 105, 2007),
(5050582554892, 'In Bruges', '18', 'Thriller', 'Crime', 'Collin Farrell', 'Brenden Gleeson', 'Martin McDonagh', 'Focus Features', 102, 2008),
(5050582487190, 'Hot Fuzz', '15', 'Thriller', 'Comedy', 'Simon Pegg', 'Nick Frost', 'Edgar Wright', 'Universal Pictures', 116, 2007),
(5039036038034, 'Jumper', '15', 'Thriller', 'Adventure', 'Hayden Christiansen', 'Jamie Bell', 'Doug Liman', 'Universal Pictures', 116, 2007),
(8717418566104, 'Star Wars Episode I - The Phantom Menace', '12', 'Science Fiction', 'Adventure', 'Ewan McGregor', 'Liam Neeson', 'George Lucas', 'Lucasfilm', 131, 1999),
(8717418566104, 'Star Wars Episode II - Attack of the clones', '12', 'Science Fiction', 'Adventure', 'Ewan McGregor', 'Hayden Christiansen', 'George Lucas', 'Lucasfilm', 137, 2002),
(8717418566104, 'Star Wars Episode III - Revenge of the Sith', '12', 'Science Fiction', 'Adventure', 'Ewan McGregor', 'Hayden Christiansen', 'George Lucas', 'Lucasfilm', 134, 2005),
(859406706049, 'The Game', '18', 'Thriller', 'Suspense', 'Michael Douglas', 'Sean Penn', 'David Fincher', 'Polygram Filmed Entertainment', 123, 1997),
(8717418566104, 'Star Wars Episode IV - A New Hope', '12', 'Science Fiction', 'Adventure', 'Mark Hamill', 'Alec Guiness', 'George Lucas', 'Lucasfilm', 120, 1977),
(8717418566104, 'Star Wars Episode V - The Empire Strikes Back', '12', 'Science Fiction', 'Adventure', 'Mark Hamill', 'Alec Guiness', 'George Lucas', 'Lucasfilm', 122, 1980),
(8717418566104, 'Star Wars Episode VI - Return of the Jedi', '12', 'Science Fiction', 'Adventure', 'Mark Hamill', 'Alec Guinness', 'George Lucas', 'Lucasfilm', 129, 1983),
(8717418566104, 'Star Wars Episode VII - The Force Awakens', '12', 'Science Fiction', 'Adventure', 'Daisy Ridley', 'John Boyega', 'J J Abrams', 'Lucasfilm', 133, 2015),
(5050582508291, 'The Bourne Ultimatum', '12', 'Thriller', 'Spy', 'Matt Damon', 'Julia Stiles', 'Paul Greengrass', 'Universal Pictures', 110, 2007),
(8717418566104, 'Star Wars Episode VIII - The Last Jedi', '12', 'Scence Fiction', 'Adventure', 'Daisy Ridley', 'John Boyega', 'J J Abrams', 'Lucasfilm', 146, 2017),
(8717418566104, 'Star Wars Episode IX - The Rise of Skywalker', '12', 'Science Fiction', 'Adventure', 'Daisy Ridley', 'John Boyega', 'J J Abrams', 'Lucasfilm', 135, 2019),
(9780471778646, 'Python for Dummies', 'BOOK', 'Non-Fiction', 'Self Teach Manual', 'Stef Maruch', 'Aahz Maruch', 'Wiley Publishing', 'Wiley Publishing', 0, 2006),
(9780749310189, 'When am I going to be happy?', 'BOOK', 'Non-Fiction', 'Self Help', 'Dr. Penelope Russainoff', '', 'Mandarin', 'Octopus Publishing Group', 0, 1988),
(5039036012898, 'Antwone Fischer', '15', 'Drama', 'Drama', 'Denzel Washington', 'Derek Luke', 'Denzel Washington', 'Fox Searchlight Pictures', 115, 2002),
(5060052418753, 'Harry Brown', '18', 'Thriller', 'Crime', 'Michael Caine', 'Noel Winters', 'Daniel Barber', 'Samuel Goldwyn Films', 99, 2009),
(5035822887435, 'Concussion', '12', 'True Story', 'Drama', 'Will Smith', 'Alec Baldwin', 'Peter Landesman', 'Columbia Pictures', 118, 2015),
(5017188815604, 'The Aviator', '12', 'True Story', 'Biopic', 'Leonardo DiCaprio', 'Cate Blanchett', 'Martin Scorsese', 'Warner Brothers', 163, 2004),
(7321900680578, 'The Last Samurai', '15', 'Period Drama', 'Battle', 'Tom Cruise', 'Ken Wantanabe', 'Edward Zwick', 'Radar Pictures', 148, 2003),
(5060116727456, 'Lawless', '18', 'Thriller', 'Drama', 'Shia Lebeouf', 'Tom Hardy', 'John Hillcoat', 'Benaroya Pictures', 110, 2012),
(5050582383706, 'The Bourne Identity', '15', 'Thriller', 'Spy', 'Matt Damon', 'Franka Potente', 'Doug Liman', 'Universal Pictures', 114, 2002),
(5050582383706, 'The Bourne Supremacy', '12', 'Thriller', 'Spy', 'Matt Damon', 'Joan Allen', 'Paul Greengrass', 'Universal Pictures', 110, 2004),
(5050582383706, 'Paycheck', '12', 'Thriller', 'Drama', 'Ben Affleck', 'Uma Thurman', 'John Woo', 'Davis Entertainment', 119, 2003),
(8594157780028, 'Capricorn One', '12', 'Thriller', 'Drama', 'James Brolin', 'O J Simpson', 'Peter Hyams', 'Associated General Films', 110, 1977),
(5055201814227, 'Unknown', '15', 'Thriller', 'Suspense', 'Liam Needson', 'Diane Kruger', 'Jaume Collet-Serra', 'Dark Castle Entertainment', 108, 2011),
(5014437119636, 'Shutter Island', '15', 'Thriller', 'Suspense', 'Leonardo DiCaprio', 'Mark Buffalo', 'Martin Scorcese', 'Paramount Pictures', 132, 2010),
(5051892032988, 'Inception', '12', 'Thriller', 'Suspense', 'Leonardo DiCaprio', 'Kate Watanabe', 'Christopher Nolan', 'Warner Brothers', 142, 2010),
(5039036034685, 'Predator', '18', 'Science Fiction', 'Thriller', 'Arnold Schwarzenegger', 'Carl Weathers', 'John McTiernan', '20th Century Fox', 106, 1987),
(5039036034685, 'Commando', '18', 'Thriller', 'Action', 'Arnold Schwarzenegger', 'Rae Dawn Chong', 'Joel Silver', '20th Century Fox', 85, 1985),
(5039036034685, 'Conan the Barbarian', '15', 'Adventure', 'Fantasy', 'Arnold Schwarzenegger', 'James Earl Jones', 'John Milius', 'Dino de Laurentiis', 125, 1981),
(5060262859049, 'Vanquish', '15', 'Thriller', 'Action', 'Morgan Freeman', 'Ruby Rose', 'George Gallo', 'Capstone Pictures', 94, 2021),
(5050070006476, 'When Harry met Sally', '15', 'Comedy', 'Romance', 'Billy Crystal', 'Meg Ryan', 'Rob Reiner', 'Castle Rock Entertainment', 92, 1989),
(7321900934718, 'The Mothman Prophecies', '12', 'Horror', 'Drama', 'Richard Gere', 'Laura Linney', 'Mark Pellington', 'Lakeside Entertainment', 114, 2001),
(5051892226806, 'Tenet', '12', 'Thriller', 'Drama', 'John David Washington', 'Robert Pattinson', 'Christopher Nolan', 'Warner Brothers', 144, 2020),
(5051429101040, 'Starter for 10', '15', 'Comedy', 'Drama', 'James McAvoy', 'Rebecca Hall', 'Tom Vaughan', 'HBO Films', 92, 2006)
]



# Re-write Records



add_films()



# Close DB



DVD_DB.commit()
DVD_cursor.close()
