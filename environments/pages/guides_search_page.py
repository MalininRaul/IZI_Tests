from .base_page import BasePage

class GuidesSearchPage(BasePage):
    def should_be_guides_search_page(self):
        self.should_be_guides_search_url()

    def should_be_guides_search_url(self):
        assert "search" in self.browser.current_url, "Wrong url"
