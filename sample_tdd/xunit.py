class TestCase(object):
    name: str

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    wasRun: int

    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def test_method(self):
        self.wasRun = 1


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert (not test.wasRun)
        test.run()
        assert test.wasRun


TestCaseTest("test_running").run()
