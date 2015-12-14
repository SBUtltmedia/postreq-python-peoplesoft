def trim(s):
    if s:
        return s.strip()
    else:
        return None


def trim_leading_zeroes(s):
    if s:
        return s.lstrip('0')
    else:
        return None
