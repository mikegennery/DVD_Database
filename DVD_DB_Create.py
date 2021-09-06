# Michael Gennery
# DVD Database
# August 2020
# Create Table

import sqlite3

DVD_DB = sqlite3.connect('DVD_DB.db')

DVD_cursor = DVD_DB.cursor()

DVD_fields = """
    create table DVD
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

DVD_cursor.execute(DVD_fields)





