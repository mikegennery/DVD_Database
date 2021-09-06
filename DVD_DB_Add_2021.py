# Michael Gennery
# DVD / Books Database
# July 2021
# Add DVD & Books

import sqlite3
import pickle

"""
    create table DVD
    (
        barcode int,      -- Barcode / ISBN Number
        name varchar,     -- Name of Film / Book
        cert varchar,     -- Certification / BOOK
        genre_1 varchar,  -- Type of film / Book
        genre_2 varchar,  -- Sub Type
        actor_1 varchar,  -- Main Actor / Author
        actor_2 varchar,  -- Supporting Actor / Supporting Author OR leave blank
        director varchar, -- Director / Publisher
        company varchar,  -- Production Company / Publisher OR leave blank
        run_time int,     -- Running Time in minutes / 0 for books
        year int          -- Year of release / Publicarion
    )
    """


# Write records to the database


def add_films():
    for film in DVD_list:
        DVD_cursor.execute("""insert into DVD values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", film)


# Variables


quit_prog = False
valid_input = False
option = ''
DVD_list = []
film_list = []
cert_list = ['U', 'UC', 'PG', '12', '15', '18', 'EX','BOOK']

barcode = 0             ## Barcode / ISBN Number
name = '',              ## Name of Film / Book
cert = '',              ## Certification / BOOK
genre_1 = '',           ## Type of film / Book
genre_2 = '',           ## Sub Type
actor_1 = '',           ## Main Actor / Author
actor_2 = '',           ## Supporting Actor / Supporting Author OR leave blank
director = '',          ## Director / Publisher
company = '',           ## Production Company / Publisher OR leave blank
run_time = 0,           ## Running Time / 0 for books
year = 0                ## Year of release / Publication

DVD_dict = {
        'barcode' : 0,          ## Barcode / ISBN Number
        'name' : '',            ## Name of Film / Book
        'cert' : '',            ## Certification / BOOK
        'genre_1' : '',         ## Type of film / Book
        'genre_2' : '',         ## Sub Type
        'actor_1' : '',         ## Main Actor / Author
        'actor_2' : '',         ## Supporting Actor / Supporting Author OR leave blank
        'director' : '',        ## Director / Publisher
        'company' : '',         ## Production Company / Publisher OR leave blank
        'run_time' : 0,         ## Running Time / 0 for books
        'year' : 0              ## Year of release / Publication
    }


# Open database file


DVD_DB = sqlite3.connect('DVD_DB.db')
DVD_cursor = DVD_DB.cursor()


# Enter details of the film to be added to the database


print('DVD & Books Database')
print('____________')
print('\nEnter the details of the DVD / Book to add to the database')
print('\t - Enter 999 to quit')
print('\t - Enter 666 to restore DVD / Book database')


while not quit_prog:

    valid_input = False

    # Barcode
    
    while not valid_input:
        valid_input = True
        barcode = input('\nBARCODE............................: ')
        try:
            DVD_dict['barcode'] = int(barcode)
        except ValueError:
            valid_input = False
            print('Invalid Input!')
        except TypeError:
            valid_input = False
            print('Invalid Input!')

    # This checks to see if the barcode already exists and allows entry for boxsets

    film_list = []
    compare_text_1 = """select * from DVD where barcode="""
    compare_text_2 = str(barcode)
    compare_text = compare_text_1 + compare_text_2
    film_list = DVD_cursor.execute(compare_text)
    for film in film_list:
        print('WARNING! This barcode is already in your database!')
        break

    if barcode == '999': # The use enters 999 if they have finished entering records
        quit_prog = True

    elif barcode == '666' and DVD_list != []:
        print('\nCannot restore\nYou have unsaved records in your database!')

    elif barcode == '666' and DVD_list == []:

        # Unpickle the database file
        
        DVD_list = []
        DVD_DB_pickle = open('DVD_DB_pickle', 'rb')
        DVD_list = pickle.load(DVD_DB_pickle)
        DVD_DB_pickle.close() # Close the file

        print('\nDVD / BOOK DATABASE RESTORED!!\n')
        quit_prog = True
        
    else:
    
        name = input('NAME...............................: ')             ## NAME OF FILM / BOOK
        DVD_dict['name'] = name

        valid_input = False
    
        while not valid_input:
            cert = input('CERTIFICATION......................: ')         ## Certification
            cert = cert.upper()
            if cert in cert_list:
                valid_input = True
                DVD_dict['cert'] = cert
            else:
                print('Please Enter a valid certification!')
                valid_input = False
        
        genre_1 = input('MAIN GENRE.........................: ') ## Type of film / Book
        DVD_dict['genre_1'] = genre_1
        genre_2 = input('SUB GENRE..........................: ') ## Sub Type
        DVD_dict['genre_2'] = genre_2
        actor_1 = input('MAIN ACTOR / AUTHOR................: ') ## Main Actor / Author
        DVD_dict['actor_1'] = actor_1
        actor_2 = input('SUPPORTING ACTOR / AUTHOR..........: ') ## Supporting Actor / Supporting Author
        DVD_dict['actor_2'] = actor_2
        director = input('DIRECTOR / PUBLISHER...............: ') ## Director / Publisher
        DVD_dict['director'] = director
        company = input('PRODUCTION COMPANY / PUBLISHER.....: ') ## Production Company / Publisher
        DVD_dict['company'] = company
    
        valid_input = False

        while not valid_input:
            valid_input = True
            run_time = input('RUNNING TIME - MINS.(0 for books)..: ') ## Running Time - Minutes
            try:
                DVD_dict['run_time'] = int(run_time)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
            except TypeError:
                valid_input = False
                print('Invalid Input!')
            if valid_input == True:
                if (int(run_time) < 0 or int(run_time) > 300):
                    valid_input = False
                    print('Minutes must be between 0 - 300')

        valid_input = False

        while not valid_input:
            valid_input = True
            year = input('YEAR...............................: ')  ## Year of release / Publication
            try:
                DVD_dict['year'] = int(year)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
            except TypeError:
                valid_input = False
                print('Invalid Input!')
            if valid_input == True:
                if (int(year) < 1900 or int(year) > 2099):
                    valid_input = False
                    print('Year must be between 1900 - 2099')

    # Add this record?

        option = ''
        valid_input = False

        while not valid_input:
            option = input('\nDo you wish to add this record to the database? (Y/N): ')
            option = option.lower()
            if option == 'y' or option == 'yes':
                option = 'y'
                valid_input = True
            elif option == 'n' or option == 'no':
                option = 'n'
                valid_input = True
            else:
                print('You must reply Y - YES or N - NO!')

        ## Barcode / ISBN Number
        ## Name of Film / Book
        ## Certification / BOOK
        ## Type of film / Book
        ## Sub Type
        ## Main Actor / Author
        ## Supporting Actor / Supporting Author OR leave blank
        ## Director / Publisher
        ## Production Company / Publisher OR leave blank
        ## Running Time / 0 for books
        ## Year of release / Publication

        if option == 'y':
            DVD_list.append((
            DVD_dict['barcode'],          ## Barcode
            DVD_dict['name'],             ## Name of Film / Book
            DVD_dict['cert'],             ## Certification
            DVD_dict['genre_1'],          ## Type of film / Book
            DVD_dict['genre_2'],          ## Sub Type
            DVD_dict['actor_1'],          ## Main Actor / Author
            DVD_dict['actor_2'],          ## Supporting Actor / Author
            DVD_dict['director'],         ## Director / Publisher
            DVD_dict['company'],          ## Production Company / Publisher
            DVD_dict['run_time'],         ## Running Time / 0 for books
            DVD_dict['year']              ## Year of release / Publication
            ))

    
    # Quit the program?

        option = ''
        valid_input = False

        while not valid_input:
            option = input('\nDo you wish to add any more records to the database? (Y/N): ')
            option = option.lower()
            if option == 'y' or option == 'yes':
                option = 'y'
                valid_input = True
            elif option == 'n' or option == 'no':
                option = 'n'
                valid_input = True
                quit_prog = True
            else:
                print('You must reply Y - YES or N - NO!')



# Write records to the database



add_films()

if len(DVD_list) > 0:
    print('\nList of records added: -\n')
    for film in DVD_list:
        print(film)
    print('\n',len(DVD_list),' record/s written to the database')



# Pickle the database in a seperate file



valid_input = False # Reset the error flag

while not valid_input:
    select_option = input('\nDo you wish to save the database in a seperate binary file? (Y = YES, N = NO): ')
    select_option = select_option.lower()
    if select_option == 'y' or select_option == 'yes' or select_option == 'n' or select_option == 'no':
        valid_input = True
    else:
        valid_input = False
        print('You Must Enter Y or N!')

if select_option == 'y' or select_option == 'yes':

    DVD_list = []
    DVD_cursor.execute("""select * from DVD""") # Ensure all records are pickled
    DVD_list = DVD_cursor.fetchall()
    DVD_DB_pickle = open('DVD_DB_pickle', 'wb')
    pickle.dump(DVD_list, DVD_DB_pickle)
    print('\nDVD / Book Database pickled in file - DVD_DB_pickle')
    DVD_DB_pickle.close() # Close the file



# Save and close the database



DVD_DB.commit()
DVD_cursor.close()

quit = input('\nPlease ENTER to continue')
