import sqlite3

class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_tables()

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interesting_articles (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            date_of_creation TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image TEXT NOT NULL,
            link TEXT NOT NULL
            )
        ''')

        cursor.close()
        self.db.commit()

    def add_interesting_article(self, author, date_of_creation, title, description, image, link):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO interesting_articles(author, date_of_creation, title, description, image, link) VALUES(?, ?, ?, ?, ?, ?)',
                       [author, date_of_creation, title, description, image, link])
        cursor.close()
        self.db.commit()

    def get_interesting_articles(self):
        cursor = self.db.cursor()
        query = "SELECT * FROM interesting_articles "
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result