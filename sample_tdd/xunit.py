class TestCase(object):
    name: str

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    wasSetUp: int
    wasRun: int

    def test_method(self):
        self.wasRun = 1

    def set_up(self):
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert self.test.wasSetUp


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
