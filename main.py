import database as db
import queryUtils as qu


def fill_landmarks():
    names = [
        "Eiffel Tower", "Statue of Liberty", "Big Ben", "Colosseum", "Machu Picchu",
        "Great Wall", "Taj Mahal", "Pyramids of Giza", "Mount Rushmore", "Sydney Opera House"
    ]

    descriptions = [
        "red", "blue", "green", "yellow", "purple",
        "orange", "black", "white", "gray", "brown"
    ]

    histories = [
        "1800", "1850", "1900", "1920", "1950",
        "1960", "1970", "1980", "1990", "2000"
    ]
    sess = db.Session()
    try:
        for name in names:
            for descr in descriptions:
                for history in histories:
                    new_landmark = db.Landmark(name=name, descr=descr, history=history)
                    sess.add(new_landmark)
        sess.commit()
    except Exception as e:
        session.rollback()
        print("An error occurred", e)
    finally:
        session.close()


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
