from sample_tdd import __version__, __all__


def test_version():
    assert __version__ == '0.1.0'


def test_all():
    assert __all__ == ["__version__", "hello_world"]
