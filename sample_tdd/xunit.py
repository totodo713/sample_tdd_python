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
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    wasRun: int

    def set_up(self):
        self.log = "Set up "

    def test_method(self):
        self.wasRun = 1
        self.log += "Test Method "

    def tearDown(self):
        self.log += "Tear Down "


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "Set up Test Method Tear Down " == test.log


TestCaseTest("test_template_method").run()
