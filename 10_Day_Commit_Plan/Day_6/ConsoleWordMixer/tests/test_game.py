import builtins
import io
import sys
import pytest
from ConsoleWordMixer import game


def test_scramble_changes_when_possible():
    # deterministic seed should scramble differently for most words
    w = "python"
    s = game.scramble_word(w, seed=1)
    assert s != w
    assert sorted(s) == sorted(w)


def test_scramble_short_word():
    assert game.scramble_word("a") == "a"


def test_pick_random_words_count():
    src = ["a", "b", "c", "d"]
    res = game.pick_random_words(src, 2, seed=5)
    assert len(res) == 2
    assert all(r in src for r in res)


def test_play_round_correct(monkeypatch, capsys):
    # simulate correct input
    monkeypatch.setattr('builtins.input', lambda prompt='': 'python')
    won, scrambled = game.play_round('python', seed=2)
    captured = capsys.readouterr()
    assert won is True
    assert 'Correct!' in captured.out


def test_play_round_incorrect(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda prompt='': 'wrong')
    won, scrambled = game.play_round('python', seed=2)
    captured = capsys.readouterr()
    assert won is False
    assert 'Nope' in captured.out
