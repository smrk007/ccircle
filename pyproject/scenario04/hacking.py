import connection
import time

con = connection.create()
con.send('set_name', {'name': 'manifold'})

while True:
    con.send('get_player_id_by_name', {'name':'bazzlepadzorpiawejfoiwejfoaijsdfalkwejfoaisdjflkejf'})
    time.sleep(0.1)