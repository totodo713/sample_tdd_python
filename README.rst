===========
TDDサンプル
===========

テスト駆動開発のサンプル
::::::::::::::::::::::::

利用しているライブラリのリファレンスリンク
::::::::::::::::::::::::::::::::::::::::::

* python : 3.7.0
* `poetry`_ : 1.0.5
* `pytest`_

コマンド
::::::::

* 依存関係のインストール

.. code-block:: shell

    $ pip install --user poetry
    $ poetry --version
    $ poetry install

* テスト実行

.. code-block:: shell

    $ pytest

* テストカバレッジの取得（HTML）

.. code-block:: shell

    $ pytest --cov=sample_tdd --cov-report=html


外部参照リンク
==============
.. _`poetry`: https://python-poetry.org/docs/
.. _`pytest`: https://docs.pytest.org/en/latest/
