class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if hasattr(self, '_title'):
            return
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value

class Author:
    def __init__(self, name):
        if hasattr(self, '_name'):
            return
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    all = []
    
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_counts = {}
        for article in Article.all:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
        return max(magazine_counts, key=magazine_counts.get) if magazine_counts else None