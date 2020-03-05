#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test for hello_world module.

Testing sample.

* Author: YAMAGAMI Satoshi
"""
import hello_world

import pytest


class TestHelloWorld(object):
    """Test for HelloWorld."""

    class TestMessage(object):
        """Test for Property "message"."""

        @pytest.mark.parametrize(
            "message, expected",
            [("Hello, World", "Hello, World"),
             ("hello", "hello"), ("bye", "bye"), ],
        )
        def test_message_on_init(self, message: str, expected: str):
            """Test on initialize."""
            actual = hello_world.HelloWorld(message).message
            assert actual == expected, "コンストラクタで指定したmessageが取得できること"

        @pytest.mark.parametrize(
            "message, expected",
            [("Hello, World", "Hello, World"),
             ("hello", "hello"), ("bye", "bye"), ],
        )
        def test_message_with_setter(self, message: str, expected: str):
            """Test with setter."""
            target = hello_world.HelloWorld()

            actual = target.message
            assert actual is None, "コンストラクタで省略した場合はmessageはNoneであること"

            target.message = message
            actual = target.message
            assert actual == expected, "Setterで指定したMessageが取得できること"

    class TestSay(object):
        """Test for say()."""

        @classmethod
        def setup_method(cls):
            """Set up the class with test commons."""
            cls.target = hello_world.HelloWorld("")

        @pytest.mark.parametrize(
            "message, expected",
            [("Hello, World", "Hello, World\n"),
             ("hello", "hello\n"), ("bye", "bye\n"), ],
        )
        def test_print_message(self, capfd, message: str, expected: str):
            """Test print message."""
            self.target.message = message
            self.target.say()

            actual_out, actual_err = capfd.readouterr()

            expect_out, expect_err = [expected, ""]

            assert actual_out == expect_out, "標準出力にメッセージが表示されていること"
            assert actual_err == expect_err, "標準エラー出力にメッセージが表示されていないこと"
