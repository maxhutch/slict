from slict.core import Slict


def test_basic_1d():
    d = {"a": "b", 1: "1.0"}
    sd = Slict(d)
    assert len(d) == len(sd)
    for key in d:
        assert d[key] == sd[key]
    for key in sd:
        assert d[key] == sd[key]


def test_basic_2d():
    d = {("a", "b"): "c", (1., 2.): 3.}
    sd = Slict(d)
    assert len(d) == len(sd)
    for key in d:
        assert d[key] == sd[key]
    for key in sd:
        assert d[key] == sd[key]


def test_2d_leading():
    d = {}
    d[1, 2] = 3
    d[1, 3] = 4
    d[2, 2] = 4
    sd = Slict(d)
    sd1 = sd[:, 2]
    assert len(sd1) == 2
    assert sd1[1] == 3
    assert sd1[2] == 4


def test_2d_trailing():
    d = {}
    d[1, 2] = 3
    d[1, 3] = 3
    d[2, 2] = 4
    d[2, 3] = 5
    sd = Slict(d)
    sd1 = sd[2, :]
    assert len(sd1) == 2
    assert sd1[2] == 4
    assert sd1[3] == 5


def test_3d():
    d = {}
    d[2, 2, 2] = 6
    d[2, 2, 3] = 7
    d[2, 3, 3] = 8
    sd = Slict(d)
    sd2 = sd[2, :, :]
    assert len(sd2) == 3
    assert sd2[2, 2] == 6
    assert sd2[2, 3] == 7
    assert sd2[3, 3] == 8
