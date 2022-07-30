def format_duration(seconds):
    tim = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    ]

    if not seconds:
        return "now"
    parts = []

    for name, sec in tim:
        curr = seconds // sec
        if curr:
            if curr > 1:
                name += "s"
            parts.append(str(curr) + " " + name)
        seconds = seconds % sec
    return ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else parts[0]


print(format_duration(3662))
