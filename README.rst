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

* 依存関係の追加

.. code-block:: shell

    // 本番にも適用する場合
    $ poetry add <パッケージ>
    // 開発環境のみの場合
    $ poetry add <パッケージ> --dev

* 依存関係の削除

.. code-block:: shell

    // 本番にも適用する場合
    $ poetry remove <パッケージ>
    // 開発環境のみの場合
    $ poetry remove <パッケージ> --dev

外部参照リンク
==============
.. _`poetry`: https://python-poetry.org/docs/
.. _`pytest`: https://docs.pytest.org/en/latest/
