import time

class AlarmClock:
    def __init__(self):
        self.current_time = time.strftime('%H:%M:%S')
        self.alarm_time = None
        self.is_alarm_set = False
        self.snooze_time = None
        self.alarm_message = ""

    def set_alarm(self, time, message):
        self.alarm_time = time
        self.alarm_message = message
        self.is_alarm_set = True

    def toggle_alarm(self):
        self.is_alarm_set = not self.is_alarm_set

    def snooze(self, minutes):
        self.snooze_time = time.strftime('%H:%M:%S', time.localtime(time.time() + minutes * 60))
        self.is_alarm_set = True

    def update_time(self):
        self.current_time = time.strftime('%H:%M:%S')

    def display_time(self):
        print(self.current_time)

def main():
    clock = AlarmClock()

    while True:
        clock.update_time()
        clock.display_time()

        if clock.is_alarm_set and clock.current_time >= clock.alarm_time:
            print("Alarm:", clock.alarm_message)
            clock.is_alarm_set = False

        if clock.snooze_time is not None and clock.current_time >= clock.snooze_time:
            print("Snooze:", clock.alarm_message)
            clock.snooze_time = None

        time.sleep(1)

if __name__ == "__main__":
    main()
