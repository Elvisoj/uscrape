from app.locators.post_locator import PostLocator

class PostParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"PostParser(title={self.title}, description={self.description}, thumbnail={self.thumbnail}, url={self.url})"

    @property
    def title(self):
        locator = PostLocator.TITLE
        return self.parent.select_one(locator).string

    @property
    def description(self):
        locator = PostLocator.DESCRIPTION
        return self.parent.select_one(locator).string

    @property
    def thumbnail(self):
        locator = PostLocator.THUMBNAIL
        return self.parent.select_one(locator).attrs['src']
    
    @property
    def url(self):
        locator = PostLocator.URL
        return self.parent.select_one(locator).attrs['href']