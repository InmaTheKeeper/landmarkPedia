import database as db
import queryUtils as qu


if __name__ == '__main__':
    session = db.Session()
    try:
        # insert your query here
        pass
    except Exception as e:
        session.rollback()
        print("An error occurred", e)
    finally:
        session.close()
