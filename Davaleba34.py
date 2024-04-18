##1
# import mysql.connector


# conn = mysql.connector.connect(
#     host='localhost',
#     user='paata',
#     password='1234',
#     database="it_step_34_1"
# )

# cursor = conn.cursor()


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS User (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(100) UNIQUE NOT NULL,
#         email VARCHAR(100) UNIQUE NOT NULL
#     )
# """)


# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Profile (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         user_id INT,
#         bio TEXT,
#         profile_picture VARCHAR(100),
#         FOREIGN KEY (user_id) REFERENCES User(id)
#     )
# """)


# user_data = [
#     ("user1", "user1@example.com"),
#     ("user2", "user2@example.com"),
#     ("user3", "user3@example.com"),
#     ("user4", "user4@example.com"),
#     ("user5", "user5@example.com")
# ]

# for i, (username, email) in enumerate(user_data, 1):
#     unique_username = f"{username}_{i}"  
#     cursor.execute("INSERT INTO User (username, email) VALUES (%s, %s)", (unique_username, email))


# profile_data = [
#     (1, "Bio for user1", "profile_picture1.jpg"),
#     (2, "Bio for user2", "profile_picture2.jpg"),
#     (3, "Bio for user3", "profile_picture3.jpg"),
#     (4, "Bio for user4", "profile_picture4.jpg"),
#     (5, "Bio for user5", "profile_picture5.jpg")
# ]

# for user_id, bio, profile_picture in profile_data:
#     cursor.execute("INSERT INTO Profile (user_id, bio, profile_picture) VALUES (%s, %s, %s)", (user_id, bio, profile_picture))

# # ============================================
# conn.commit()
# conn.close()




##2
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship


# engine = create_engine('mysql+mysqlconnector://paata:1234@localhost/it_step_34_1')


# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'User'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(100), unique=True, nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     profile = relationship("Profile", back_populates="user", uselist=False)

# class Profile(Base):
#     __tablename__ = 'Profile'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('User.id'), unique=True)
#     bio = Column(Text)
#     profile_picture = Column(String(100))
#     user = relationship("User", back_populates="profile")


# Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()


# user_data = [
#     User(username="user1", email="user1@example.com"),
#     User(username="user2", email="user2@example.com"),
#     User(username="user3", email="user3@example.com"),
#     User(username="user4", email="user4@example.com"),
#     User(username="user5", email="user5@example.com")
# ]
# session.add_all(user_data)
# session.commit()


# profile_data = [
#     Profile(user_id=1, bio="Bio for user1", profile_picture="profile_picture1.jpg"),
#     Profile(user_id=2, bio="Bio for user2", profile_picture="profile_picture2.jpg"),
#     Profile(user_id=3, bio="Bio for user3", profile_picture="profile_picture3.jpg"),
#     Profile(user_id=4, bio="Bio for user4", profile_picture="profile_picture4.jpg"),
#     Profile(user_id=5, bio="Bio for user5", profile_picture="profile_picture5.jpg")
# ]
# session.add_all(profile_data)
# session.commit()
# session.close()