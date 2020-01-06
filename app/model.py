from app import db


def add_data (data):
    db.insert("INSERT INTO tmp_table (val) VALUES(%(val)s)", val=str(data))

def check_user (login):
    user_info = db.query_one("""
        SELECT user_id
        FROM passwords
        WHERE login = %(login)s
    """, login=login)
    if len(user_info):
        return user_info['user_id']
    else:
        return None

def check_password (user_id, password):
    is_valid = db.query_one("""
        SELECT user_id
        FROM passwords
        WHERE user_id=%(user_id)s and password=%(password)s
    """, user_id=user_id, password=password)

    if is_valid:
        return True
    return False
