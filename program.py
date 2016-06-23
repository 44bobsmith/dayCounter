import datetime
import os

def main():
    # check for existing file with previous start, if not create file when counter is started
    # first time start
    # if file exists, capture current time and report how long since last counter reset
    print('Welcome to the day counter...')
    filename = os.path.abspath(os.path.join('.', 'dayCounterData.txt'))
    if os.path.exists(filename):
        with open(filename) as fin:
            start_date = datetime.datetime.strptime(fin.readline(), '%Y-%m-%d %H:%M:%S')
            report_time_since_start(start_date)
            start_date = start_counter()
            write_date_to_file(filename, start_date)
    else:
        start_date = start_counter()
        write_date_to_file(filename, start_date)


def start_counter():
    cmd = input('Would you like to start/reset the counter (please press y/n)?')
    if cmd.lower().strip() == 'y':
        now = datetime.datetime.now()
        start_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
        print('You started your counter at {}:{} on {}'.format(start_time.hour, start_time.minute, start_time.date()))
        return start_time
    elif cmd.lower().strip() == 'n':
        quit()



def write_date_to_file(filename, start_date):
    with open(filename, 'w') as fout:
        fout.write(start_date.__str__())

def report_time_since_start(start_date):
    currentTime = datetime.datetime.now()
    dt = currentTime - start_date
    days = float(dt.total_seconds()/60/60/24)
    print('It has been {0:.2f} days since you reset the counter.'.format(days))


if __name__ == '__main__':
    main()