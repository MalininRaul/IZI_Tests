from ..pages.main_page import MainPage
from ..pages.guides_search_page import GuidesSearchPage


def test_guest_can_go_to_audio_guide_page(browser):
    link = "https://www.izi.travel/en"
    page = MainPage(browser, link)
    page.open()
    page.go_to_guides_search_page()
    guides_search_page = GuidesSearchPage(browser, browser.current_url)
    guides_search_page.should_be_guides_search_page()

def test_guest_should_see_audio_guides_lnk(browser):
    link = "https://www.izi.travel/en"
    page = MainPage(browser, link)
    page.open()
    page.should_be_audio_guides_link()
