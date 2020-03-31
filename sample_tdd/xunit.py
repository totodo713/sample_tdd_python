class TestResult(object):
    runCount: int

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def summary(self) -> str:
        return f"{self.runCount} run, {self.errorCount} failed"

    def test_started(self):
        self.runCount += 1

    def test_failed(self):
        self.errorCount += 1


class TestCase(object):
    name: str

    def __init__(self, name: str):
        assert isinstance(name, str)
        self.name = name

    def set_up(self):
        pass

    def run(self, result: TestResult):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()

    def tear_down(self):
        pass


class TestSuite(object):
    def __init__(self):
        self.tests = []

    def add(self, test: TestCase):
        self.tests.append(test)

    def run(self, result: TestResult):
        for test in self.tests:
            test.run(result)


class WasRun(TestCase):
    log: str
    wasRun: int

    def __init__(self, name: str):
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

    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "Set up Test Method Tear Down " == test.log

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


if __name__ == '__main__':
    _suite = TestSuite()
    _suite.add(TestCaseTest("test_template_method"))
    _suite.add(TestCaseTest("test_result"))
    _suite.add(TestCaseTest("test_failed_result"))
    _suite.add(TestCaseTest("test_failed_result_formatting"))
    _suite.add(TestCaseTest("test_suite"))
    _result = TestResult()
    _suite.run(_result)
    print(_result.summary())
