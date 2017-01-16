from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 에디스가 메인 페이지에서 빈 아이템을 실수로 등록하려고 함
        # 빈 입력상자에서 엔터를 입력
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 페이지가 새로고침되고 빈 아이템 등록 거부 메세지 표시
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 다른거 입력하면 잘 입력됨
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # 다시 빈거를 입력
        self.get_item_input_box().send_keys('\n')

        # 다시 에러 메세지 표시
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 정상입력하면 잘 동작
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # 에디스는 메인 페이지로 돌아가서 신규 목록을 시작
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy Coke\n')
        self.check_for_row_in_list_table('1: Buy Coke')

        # 같은 아이템을 입력
        self.get_item_input_box().send_keys('Buy Coke\n')

        # Error Msg Print
        self.check_for_row_in_list_table('1: Buy Coke')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Duplicate Item')
