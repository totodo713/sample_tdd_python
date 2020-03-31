class TestResult(object):
    runCount: int

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"

    def test_started(self):
        self.runCount += 1

    def test_failed(self):
        self.errorCount += 1


class TestCase(object):
    name: str

    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_up(self):
        pass

    def run(self) -> TestResult:
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()
        return result

    def tear_down(self):
        pass


class WasRun(TestCase):
    log: str
    wasRun: int

    def __init__(self, name):
        super().__init__(name)
        self.log = ""

    def set_up(self):
        self.log = "Set up "

    def test_method(self):
        self.wasRun = 1
        self.log += "Test Method "

    def tear_down(self):
        self.log += "Tear Down "

    def test_broken_method(self):
        raise Exception()


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "Set up Test Method Tear Down " == test.log

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()


print(TestCaseTest("test_template_method").run().summary())
print(TestCaseTest("test_result").run().summary())
print(TestCaseTest("test_failed_result").run().summary())
print(TestCaseTest("test_failed_result_formatting").run().summary())
