import dbcreds
import mariadb as db


def db_connect():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print('Something is wrong with the DB')
    except:
        print('Something went wrong connecting to the DB')
    return conn, cursor
# Disconnect function that takes in the conn and cursor and attempts to close both


def db_disconnect(conn, cursor):
    try:
        cursor.close()
    except:
        print('Error closing cursor')
    try:
        conn.close()
    except:
        print('Error closing connection')

# Get posts function gets the posts from the DB and returns them.


def get_posts():
    posts = []
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "SELECT id, content, username, created_at FROM post")
        posts = cursor.fetchall()
    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    except:
        print('Error with the DB')
    db_disconnect(conn, cursor)

    return posts

# Add posts function takes in title and content args and inserts a new post into the DB, returns true.


def add_post(username, content):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "INSERT INTO post (username, content) VALUES (?, ?)", [username, content])
    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:

        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)
    return True
