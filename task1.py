from datetime import timedelta

sec = 1
minute = 60
hour = 3600
day = 86400
exception_message = "Exception raised"


def task1(delta):
    try:
        if delta.count('s'):
            if delta == 's':
                result = sec
            else:
                delta = delta.replace('s', '')
                result = int(timedelta(seconds=float(delta)).total_seconds())
        elif delta.count('m'):
            if delta == 'm':
                result = minute
            else:
                delta = delta.replace('m', '')
                result = int(timedelta(minutes=float(delta)).total_seconds())
        elif delta.count('h'):
            if delta == 'h':
                result = hour
            else:
                delta = delta.replace('h', '')
                result = int(timedelta(hours=float(delta)).total_seconds())
        elif delta.count('d'):
            if delta == 'd':
                result = day
            else:
                delta = delta.replace('d', '')
                result = int(timedelta(days=float(delta)).total_seconds())
        else:
            result = int(timedelta(seconds=float(delta)).total_seconds())
    except ValueError:
        return exception_message
    return result


if __name__ == "__main__":
    print(task1('60.5m'))
