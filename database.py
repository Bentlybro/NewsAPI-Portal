
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///news.db')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_news(self, news_post):
        # Add news post to database
        pass

    def get_all_news(self):
        # Retrieve all news posts
        pass

    def get_news_by_id(self, id):
        # Retrieve specific news post
        pass