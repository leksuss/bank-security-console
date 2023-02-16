STRANGE_DURATION_IN_HOURS = 1


def format_duration(duration):
    hours, rem = divmod(duration, 60*60)
    minutes, seconds = divmod(rem, 60)
    return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


def is_strange_visit(duration):
    return duration // 60*60 >= STRANGE_DURATION_IN_HOURS
