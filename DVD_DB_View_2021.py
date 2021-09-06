# Michael Gennery
# DVD Database
# July 2021
# View DVDs

import sqlite3
import pickle

"""
    (
        barcode int,      -- Barcode
        name varchar,     -- Name of Film
        cert varchar,     -- Certification
        genre_1 varchar,  -- Type of film
        genre_2 varchar,  -- Sub Type
        actor_1 varchar,  -- Main Actor
        actor_2 varchar,  -- Supporting Actor
        director varchar, -- Director
        company varchar,  -- Production Company
        run_time int,     -- Running Time in minutes
        year int          -- Year of release
    )
    """


# Display DVD Database



def display_DVD_DB(DVD_list):

    spaces =['',
           ' ',
           '  ',
           '   ',
           '    ',
           '     ',
           '      ',
           '       ',
           '        ',
           '         ',
           '          ',
           '           ',
           '            ',
           '             ',
           '              ',
           '               ',
           '                ',
           '                 ',
           '                  ',
           '                   ',
           '                    ',
           '                     ',
           '                      ',
           '                       ',
           '                        ',
           '                         ',
           '                          ',
           '                           ',
           '                            ',
           '                             ',
           '                              ',
           '                               ',
           '                                ',
           '                                 ',
           '                                  ',
           '                                   ',
           '                                    ',
           '                                     ',
           '                                      ',
           '                                       ',
           '                                        ',
           '                                         ']

    """
        film / headings [0] -- Barcode
        film / headings [1] -- Name of Film
        film / headings [2] -- Certification
        film / headings [3] -- Type of film
        film / headings [4] -- Sub Type
        film / headings [5] -- Main Actor
        film / headings [6] -- Supporting Actor
        film / headings [7] -- Director
        film / headings [8] -- Production Company
        film / headings [9] -- Running Time in minutes
        film / headings [10] -- Year of release
    """
    
    print('\n\n',headings_1[1],spaces[36],spaces[18],headings_1[3],spaces[28],'Actors',spaces[29],headings_1[7])
    print(headings_2)

    for film in DVD_list:
        print(film[1],'-',film[2],'(',film[10],')',spaces[41-len(film[1])],spaces[3],film[3],'&',film[4],spaces[30-len(film[3])-len(film[4])],film[5],'&',film[6],spaces[33-len(film[5])-len(film[6])],film[7])   
        
    if len(DVD_list) == 0:
        print('\n\tNo records to display')

"""
    print('\n\n',headings_1)
    print(headings_2)
    for film in DVD_list:
        print(film)
    if len(DVD_list) == 0:
        print('\n\tNo records to display')
"""


# Open database file


DVD_DB = sqlite3.connect('DVD_DB.db')
DVD_cursor = DVD_DB.cursor()


# Variabl list


search_text = ''
search_field_no = ''
search_field = ''
valid_input = False
sql_script = ''
sql_script_1 = ''
sql_script_2 = ''
sql_script_2 = ''
display_option = ''
filter_option = ''
headings_1 = ('Barcode', 'Name', 'Cert', 'Genre', 'Sub-Genre', 'Main Actor', 'Support Actor', 'Director', 'Company', 'Minutes','Year')
headings_2 = '_______________________________________________________________________________________________________________________________________________\n'
quit_prog = False
select_option = ''


# MAIN CODE


print('DVD Database')
print('____________')
print('\nView a list of records based on the entered search criteria')

valid_input = False # Reset the error flag

while not quit_prog:

    # Dose the user wish to display the whole table?
    
    valid_input = False # Reset the error flag
   
    while not valid_input: 
        display_option = input('\nDo you wish to display the whole DVD database? (Y = YES, N = NO): ')
        display_option = display_option.lower()
        if display_option == 'y' or display_option == 'n':
            valid_input = True
        else:
            valid_input = False
            print('You Must Enter Y or N!')

    if display_option == 'y':

        # Display the whole database

        DVD_cursor.execute("""select * from DVD""")
        DVD_list = DVD_cursor.fetchall()
        display_DVD_DB(DVD_list)

    else:

        # Filter the database
    
        valid_input = False # Reset the error flag

        # Does the user wish to filter the table?
    
        while not valid_input: 
            filter_option = input('\nDo you wish to filter the DVD database? (Y = YES, N = NO): ')
            filter_option = filter_option.lower()
            if filter_option == 'y' or filter_option == 'n':
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter Y or N!')

        if filter_option == 'y':

        # Filter the database

            search_text = ''
            search_field_no = ''
            search_field = ''

            print('\nWhich field do you wish to search?\n')

            print('Choose from the following: -\n')

            print(0,' - \t',headings_1[0])
            print(1,' - \t',headings_1[1])
            print(2,' - \t',headings_1[2])
            print(3,' - \t',headings_1[3])
            print(4,' - \t',headings_1[4])
            print(5,' - \t',headings_1[5])
            print(6,' - \t',headings_1[6])
            print(7,' - \t',headings_1[7])
            print(8,' - \t',headings_1[8])
            print(9,' - \t',headings_1[9])
            print(10,' - \t',headings_1[10])
            
            valid_input = False # Reset the error flag

            while not valid_input:                        
                search_field = input('\nPlease select a number from 0 - 10: ')
                try:
                    search_field_no = int(search_field)
                except ValueError:
                    valid_input = False
                    print('Invalid Input!')
                    search_field_no = -1
                except TypeError:
                    valid_input = False
                    print('Invalid Input!')
                    search_field_no = -1
                if search_field_no < 0 or search_field_no > 10:
                    valid_input = False
                    print('You must enter a number between 0 - 10!')
                else:
                    valid_input = True

            search_text = input('Enter search text: ')

            # Construct the SQL script

            if search_field_no == 0:
                sql_script_2 = 'barcode' # Barcode
            elif search_field_no == 1:
                sql_script_2 = 'name' # Name of Film
            elif search_field_no == 2:
                sql_script_2 = 'cert' # Certification
            elif search_field_no == 3:
                sql_script_2 = 'genre_1' # Type of film
            elif search_field_no == 4:
                sql_script_2 = 'genre_2' # Sub Type
            elif search_field_no == 5:
                sql_script_2 = 'actor_1' # Main Actor
            elif search_field_no == 6:
                sql_script_2 = 'actor_2' # Supporting Actor
            elif search_field_no == 7:
                sql_script_2 = 'director' #Director
            elif search_field_no == 8:
                sql_script_2 = 'company' # Production Company
            elif search_field_no == 9:
                sql_script_2 = 'run_time' # Running Time in minutes
            elif search_field_no == 10:
                sql_script_2 = 'year' # Year of release
            else:
                sql_script_2 = ''

            sql_script = 'select * from DVD where ' + sql_script_2 + ' LIKE \'%' + search_text + '%\''
            
            print('\n\t',sql_script)

            # Disply filtered database

            DVD_cursor.execute(sql_script)
            DVD_list = DVD_cursor.fetchall()
            display_DVD_DB(DVD_list)


    valid_input = False # Reset the error flag

    # Ask the user if they would like to use the program again

    while not valid_input:
        quit_prog_option = input('\nDo you wish to use the program again? (Y = YES, N = NO): ')
        if quit_prog_option == 'Y' or quit_prog_option == 'y' or quit_prog_option == 'N' or quit_prog_option == 'n':
            valid_input = True
        else:
            valid_input = False
            print('You Must Enter Y or N!')

    if quit_prog_option == 'Y' or quit_prog_option == 'y':
        quit_prog = False
    else:
        quit_prog = True





DVD_cursor.close() # Close the DVD database

