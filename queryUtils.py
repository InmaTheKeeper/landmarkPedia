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


def clear_all_database():
    session = db.Session()

    lands = session.query(db.Landmark).all()
    addresses = session.query(db.Address).all()
    categories = session.query(db.Category).all()
    hrefs = session.query(db.HistoricalReference).all()
    land_cat = session.query(db.LandmarkCategory).all()
    photos = session.query(db.Photo).all()

    for land in lands:
        session.delete(land)
    for addr in addresses:
        session.delete(addr)
    for categs in categories:
        session.delete(categs)
    for hrs in hrefs:
        session.delete(hrs)
    for lc in land_cat:
        session.delete(lc)
    for photo in photos:
        session.delete(photo)
    session.commit()


def add_landmark(address, name, descr, history, latitude, longtitude):
    session = db.Session()
    try:
        new_land = db.Landmark(address=address, name=name, descr=descr, history=history, latitude=latitude,
                               longtitude=longtitude)
        session.add(new_land)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Could not add landmark", e)
    finally:
        session.close()


def delete_landmark(land_id):
    session = db.Session()
    try:
        land = session.query(db.Landmark).filter_by(id=land_id)
        session.delete(land)
    except Exception as e:
        session.rollback()
        print("Could not delete landmark", e)
    finally:
        session.close()
