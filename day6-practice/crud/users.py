from db.database import get_connection


def create_user(name,age):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",(name,age))
    conn.commit()
    conn.close()

def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    return users

def update_user(user_id, age):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET age=? WHERE id=?",(age,user_id))

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?",(user_id,))

    conn.commit()
    conn.close()