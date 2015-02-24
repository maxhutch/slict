from slict.core import Slict, CachedSlict


def test_basic_1d():
    d = {"a": "b", 1: "1.0"}
    sd = Slict(d)
    assert len(d) == len(sd)
    assert len(d) == len(sd[:])
    assert "a" in sd
    assert 1 in sd[:]
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
    assert 1 in sd1
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
    assert 3 in sd1
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
    assert (2, 3) in sd2
    assert len(sd2) == 3
    assert sd2[2, 2] == 6
    assert sd2[2, 3] == 7
    assert sd2[3, 3] == 8


def test_keys():
    d = {}
    d[2, 2, 2] = 6
    d[2, 2, 3] = 7
    d[2, 3, 3] = 8
    sd = Slict(d)
    sd2 = sd[2, :, :]
    keys = sd2.keys()
    for k in sd2:
        assert k in keys


def test_items():
    d = {}
    d[2, 2, 2] = 6
    d[2, 2, 3] = 7
    d[2, 3, 3] = 8
    sd = Slict(d)
    sd2 = sd[2, :, :]
    d2 = dict(sd2.items())
    for key in sd2:
        assert sd2[key] == d2[key]


def test_slice_bounds():
    d = {}
    for i in range(10):
        d[i] = i
    sd = Slict(d)
    assert len(sd[:2]) == 2
    assert len(sd[1:3]) == 2
    assert len(sd[8:]) == 2


def test_CachedSlict_1d():
    d = {}
    d[3] = 3
    d[2] = 2
    d[1] = 1
    d[8] = 8
    d[2] = 2
    sd = CachedSlict(d)
    sd2 = sd[:]
    for k in sd2:
        assert sd2[k] == k
    last = 0
    for k in sd2.keys():
        assert k > last
        last = k
    items = sd2.items()
    vals = sd2.values()
    for k, v in items:
        assert v == sd2[k]
        assert v in vals


def test_CachedSlict_2d():
    d = {}
    d[3, 2] = 5
    d[2, 2] = 4
    d[1, 2] = 3
    d[8, 2] = 10
    d[2, 3] = 5
    sd = CachedSlict(d)
    sd2 = sd[:, 2]
    for k in sd2:
        assert sd2[k] == k + 2
    last = (0,)
    for k in sd2.keys():
        assert k > last
        last = k
    items = sd2.items()
    vals = sd2.values()
    for k, v in items:
        assert v == sd2[k]
        assert v in vals


def test_CachedSlict_3d():
    d = {}
    d[2, 2, 2] = 6
    d[2, 2, 3] = 7
    d[1, 2, 8] = 11
    d[8, 2, 1] = 11
    d[2, 3, 3] = 8
    sd = CachedSlict(d)
    sd2 = sd[:, 2, :]
    for k in sd2:
        assert sd2[k] == sum(k) + 2
    last = (0, 0)
    for k in sd2.keys():
        assert k > last
        last = k
    items = sd2.items()
    vals = sd2.values()
    for k, v in items:
        assert v == sd2[k]
        assert v in vals
