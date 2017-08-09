class Clock(object):
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)


    def __str__(self):
        if self.minutes > 59:
            self.hour = self.hour + (self.minutes/60)
            self.minutes = self.minutes % 60
        else:
            self.hour = self.hour
            self.minutes = self.minutes
        if self.hour > 12:
            self.hour = self.hour % 12
        else: self.hour = self.hour
        if self.minutes < 10:
            self.minutes = "0%s" % self.minutes
        else:
            self.minutes = self.minutes
        if self.hour < 10:
            self.hour = "0%s" % self.hour
        else:
            self.hour = self.hour
        time = "%s : %s" % (self.hour, self.minutes)
        return time

    def __add__(self, more_minutes):
        self.hour = int(self.hour)
        self.minutes = int(self.minutes)
        all_minutes = (self.hour * 60)+ self.minutes+ more_minutes
        self.hour = (all_minutes/60)
        self.minutes = (all_minutes % 60)
        if self.minutes > 59:
            self.hour = self.hour + (self.minutes/60)
            self.minutes = self.minutes % 60
        else:
            self.hour = self.hour
            self.minutes = self.minutes
        if self.hour > 12:
            self.hour = self.hour % 12
        else: self.hour = self.hour
        if self.minutes < 10:
            self.minutes = "0%s" % self.minutes
        else:
            self.minutes = self.minutes
        if self.hour < 10:
            self.hour = "0%s" % self.hour
        else:
            self.hour = self.hour
        time = "%s : %s" % (self.hour, self.minutes)
        return time


    def __sub__(self, more_minutes):
        self.hour = int(self.hour)
        self.minutes = int(self.minutes)
        all_minutes = (self.hour * 60)+ self.minutes- more_minutes
        self.hour = (all_minutes/60)
        self.minutes = (all_minutes % 60)
        if self.minutes > 59:
            self.hour = self.hour + (self.minutes/60)
            self.minutes = self.minutes % 60
        else:
            self.hour = self.hour
            self.minutes = self.minutes
        if self.hour > 12:
            self.hour = self.hour % 12
        else: self.hour = self.hour
        if self.minutes < 10:
            self.minutes = "0%s" % self.minutes
        else:
            self.minutes = self.minutes
        if self.hour < 10:
            self.hour = "0%s" % self.hour
        else:
            self.hour = self.hour
        time = "%s : %s" % (self.hour, self.minutes)
        return time

    def __eq__(self, other):
        return (self.hour == other.hour and self.minutes == other.minutes)

    def __ne__(self, other):
        return (self.hour != other.hour or self.minutes != other.minutes)
