from bs4 import BeautifulSoup
from app.locators.section_locators import SectionLocator

class SlideSection:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    
    def slides(self):
        locator = SectionLocator.SLIDE_SECTION
        return self.soup.select_one(locator)
    