class Event:
    def __init__(self, title, start, end):
        self.title = title
        self.start = start
        self.end = end
        self.duration = self.end - self.start
    def print(self):
        print(f"Titlu: {self.title}")
        print(f"{self.start}  ->  {self.end}")
        print(f"Durata:", end=' ')
        if self.duration.days != 0:
            print(f"{self.duration.days}", end=' ')
            if self.duration.days == 1:
                print(" zi", end=' ')
            else:
                print(" zile", end=' ')
        if self.duration.seconds != 0:
            minutes = self.duration.seconds // 60
            hours = minutes // 60
            minutes %= 60
            if hours != 0:
                print(f"{hours}", end=' ')
                if hours == 1:
                    print(" ora", end=' ')
                else:
                    print(" ore", end=' ')
            if minutes != 0:
                print(f"{minutes}", end=' ')
                if minutes == 1:
                    print(" minut")
                else:
                    print(" minute")
        print("\n")
    def inBounds(self, st, en):
        if st.year < self.start.year and self.end.year < en.year:
            return True
        elif st.year == self.start.year and self.end.year == en.year:
            if st.month < self.start.month and self.end.month < en.month:
                return True
            elif st.month == self.start.month and self.end.month == en.month:
                if st.day < self.start.day and self.end.day < en.day:
                    return True
                elif st.day == self.start.day and self.end.day == en.day:
                    if st.hour < self.start.hour and self.end.hour < en.hour:
                        return True
                    elif st.hour == self.start.hour and self.end.hour == en.hour:
                        if st.minute < self.start.minute and self.end.minute < en.minute:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False