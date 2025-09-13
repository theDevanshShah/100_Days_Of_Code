import tempfile
from pathlib import Path

import pytest

from DailySparks import app


def test_get_spark_deterministic():
    s1 = app.get_spark(seed=1)
    s2 = app.get_spark(seed=1)
    assert s1 == s2
    assert s1 in app.SPARKS


def test_favorites_lifecycle(tmp_path: Path, monkeypatch):
    # point data dir to tmp
    tmp_data = tmp_path / "data"
    monkeypatch.setattr(app, "DATA_DIR", tmp_data)
    monkeypatch.setattr(app, "FAV_FILE", tmp_data / "favorites.json")

    # start empty
    assert app.list_favorites() == []

    spark = app.SPARKS[0]
    app.add_favorite(spark)
    assert app.list_favorites() == [spark]

    # adding same spark doesn't duplicate
    app.add_favorite(spark)
    assert app.list_favorites() == [spark]


def test_favorites_file_corrupt(tmp_path: Path, monkeypatch):
    tmp_data = tmp_path / "data"
    tmp_data.mkdir()
    fav = tmp_data / "favorites.json"
    fav.write_text("not-a-json")

    monkeypatch.setattr(app, "DATA_DIR", tmp_data)
    monkeypatch.setattr(app, "FAV_FILE", fav)

    # should handle corrupt file by returning empty list and not crashing
    assert app.list_favorites() == []
