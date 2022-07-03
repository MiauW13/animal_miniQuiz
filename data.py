import sqlite3
from unittest import result
from player import Player



conn = sqlite3.connect('Players')

c = conn.cursor()

#c.execute("""CREATE TABLE Players (
#            name text,
#            score integer )""")

def insert_plyr(plyr):
    with conn:
        c.execute("INSERT INTO Players VALUES (:name, :score)",{'name': plyr.name, 'score': plyr.score})
        
def get_plyr_by_name(name):
    c.execute("SELECT * FROM Players WHERE name=:name",{'name':name})
    return c.fetchall()

def update_score(plyr, score):
    with conn:
        c.execute("UPDATE Players SET score = :score WHERE name = :name", 
        {'name': plyr.name, 'score': score})

def remove_plyr(plyr):
    with conn:
        c.execute("DELETE from Players WHERE name = :name", {'name': plyr.name})
def get_table_score():
     c.execute("SELECT * FROM Players ORDER BY score DESC;")
     return c.fetchall()




# conn.close()
