import database as db


def get_photo_by_landmark_id(landmark_id):
    session = db.Session()
    try:
        photos = session.query(db.Photo).filter_by(landmark_id=landmark_id).all()
        if photos:
            print("Found " + str(len(photos)) + " photo")
            return photos
        else:
            print("No photo found for landmark_id = " + str(landmark_id))
    except Exception as e:
        session.rollback()
        print("An error occurred", e)
    finally:
        session.close()
def get_land_by_address_id(address_id):
    session = db.Session()
    try:
        lands = session.query(db.Landmark).filter_by(address_id=address_id).all()
        if lands:
            print("Found " + str(len(lands)) + " landmarks")
            return lands
        else:
            print("No landmarks found for address_id = " + str(address_id))
    except Exception as e:
        session.rollback()
        print("An error occurred", e)
    finally:
        session.close()
