from collections import Mapping


def key_in_slice(k, s):
    """Check if the key k is part of the slice s."""
    if not isinstance(k, tuple):
        k = (k,)
    for i in range(len(s)):
        if (not isinstance(s[i], slice)) and k[i] != s[i]:
            return False
        if isinstance(s[i], slice):
            if s[i].start is not None and k[i] < s[i].start:
                return False
            if s[i].stop is not None and k[i] >= s[i].stop:
                return False
    return True


def key_from_slice(k, s):
    """Take a slice s of the key k."""
    if not isinstance(k, tuple):
        k = (k,)
    ans = []
    for i in range(len(s)):
        if isinstance(s[i], slice):
            ans.append(k[i])
    if len(ans) > 1:
        return tuple(ans)
    else:
        return ans[0]


class Slict(Mapping):
    """Sliceable interface to wrap the Mapping d

    Slict wraps an existing Mapping (e.g. dictionary) with a sliceable
    interface to tuple keys.  The slice argument sl is used internally
    when returning a slice.
    """
    def __init__(self, d, sl=None):
        self.d = d
        if sl is None:
            self.dim = max([len(key)
                            if isinstance(key, tuple) else 1 for key in d])
            self.locs = [i for i in range(self.dim)]
            self.pins = []
            self.sl = tuple([slice(None, None, None)]*self.dim)
        else:
            self.dim = len(sl)
            self.sl = sl
            self.locs = []
            self.pins = []
            j = 0
            k = 0
            for i in range(self.dim):
                if isinstance(sl[i], slice):
                    self.locs.append(j)
                    j = j+1
                else:
                    self.locs.append(-k - 1)
                    self.pins.append(sl[i])

    def __getitem__(self, key):
        """If the key contains slices, return a new Slict."""
        if not isinstance(key, tuple):
            key = (key,)
        full_key = tuple([
          key[self.locs[i]] if self.locs[i] >= 0
          else self.pins[-self.locs[i]-1]
          for i in range(self.dim)])

        if not any([isinstance(k, slice) for k in key]):
            if len(full_key) == 1:
                full_key = full_key[0]
            return self.d[full_key]

        return Slict(self.d, sl=full_key)

    def __iter__(self):
        return iter([key_from_slice(k, self.sl)
                     for k in self.d if key_in_slice(k, self.sl)])

    def __len__(self):
        return len([k for k in self.d if key_in_slice(k, self.sl)])

    def __contains__(self, key):
        if not isinstance(key, tuple):
            key = (key,)
        full_key = tuple([
          key[self.locs[i]] if self.locs[i] >= 0
          else self.pins[-self.locs[i]-1]
          for i in range(self.dim)])
        return key_in_slice(full_key, self.sl)

    def keys(self):
        return [key_from_slice(k, self.sl)
                for k in self.d if key_in_slice(k, self.sl)]

    def items(self):
        return [(key_from_slice(k, self.sl), v)
                for (k, v) in self.d.items() if key_in_slice(k, self.sl)]
