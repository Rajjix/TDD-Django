from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        self.browser.set_window_size(1240, 768)
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width']/2,
                620,
                delta=20
                )
