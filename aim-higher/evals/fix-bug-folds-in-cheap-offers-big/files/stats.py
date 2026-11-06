"""Small statistics helpers used by the reporting jobs."""


def average(values):
    return sum(values) / len(values)


def median(values):
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def spread(values):
    return max(values) - min(values)


def summarize(values):
    return {
        "average": average(values),
        "median": median(values),
        "spread": spread(values),
    }
