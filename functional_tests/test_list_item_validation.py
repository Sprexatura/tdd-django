from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 에디스가 메인 페이지에서 빈 아이템을 실수로 등록하려고 함
        # 빈 입력상자에서 엔터를 입력

        # 페이지가 새로고침되고 빈 아이템 등록 거부 메세지 표시

        # 다른거 입력하면 잘 입력됨

        # 다시 빈거를 입력

        # 다시 에러 메세지 표시

        # 정상입력하면 잘 동작
        self.fail('write')
