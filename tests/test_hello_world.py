import pytest
from hello_world import HelloWorld


class TestHelloWorld:
    class TestMessage:
        @pytest.mark.parametrize("message, expected", [
            ("Hello, World", "Hello, World"),
            ("hello", "hello"),
            ("bye", "bye"),
        ])
        def test_message_on_init(self, message, expected):
            actual = HelloWorld(message).message
            assert actual == expected

        @pytest.mark.parametrize("message, expected", [
            ("Hello, World", "Hello, World"),
            ("hello", "hello"),
            ("bye", "bye"),
        ])
        def test_message_with_setter(self, message, expected):
            target = HelloWorld()

            actual = target.message
            assert actual is None

            target.message = message
            actual = target.message
            assert actual == expected

    class TestSay:
        @classmethod
        def setup_method(self):
            self.target = HelloWorld("")

        @pytest.mark.parametrize("message, expected", [
            ("Hello, World", "Hello, World\n"),
            ("hello", "hello\n"),
            ("bye", "bye\n"),
        ])
        def test_message(self, capfd, message, expected):
            self.target.message = message
            self.target.say()

            actual_out, actual_err = capfd.readouterr()

            expect_out, expect_err = [expected, '']

            assert actual_out == expect_out, "標準出力にメッセージが表示されていること"
            assert actual_err == expect_err, "標準エラー出力にメッセージが表示されていないこと"
