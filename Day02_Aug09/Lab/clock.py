class Clock(object):
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def at(cls, hour, minutes=0):
        if minutes > 59:
            hour = hour + (minutes/60)
            minutes = minutes % 60
        else:
            hour = hour
            minutes = minutes
        if hour > 12:
            hour = hour % 12
        else: hour = hour
        time = "%s : %s" % (hour, minutes)
        return time


    def __str__(self):
        if minutes < 10:
            minutes = "0%s" % minutes
        else:
            minutes = minutes
        if hours < 10:
            hours = "0%s" % hours
        else:
            hours = hours
        time = "%s : %s" % (hour, minutes)
        return time

    def __add__(self,minutes):
        int(minutes)
        if minutes > 59:
            hour = hour + (minutes/60)
            minutes = minutes % 60
        else:
            hour = hour
            minutes = minutes
        if hour > 12:
            hour = hour % 12
        else: hour = hour
        time = "%s : %s" % (hour, minutes)
        return time

    def __sub__(self,minutes):
        int(minutes)
        if minutes < 0:
            minutes = (minutes % 60) - minutes

    def __eq__(self, other):

    def __ne__(self, other):


def Clock(hour, minutes):
    if minutes > 59:
        hour = hour + (minutes/60)
        minutes = minutes % 60
    else:
        hour = hour
        minutes = minutes
    if minutes < 10:
        minutes = "0%s" % minutes
    if hour > 12:
        hour = hour % 12
    else: hour = hour
    time = "%s : %s" % (hour, minutes)
    return time
