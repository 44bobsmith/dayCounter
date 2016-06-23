import datetime
import os

def main():
    # check for existing file with previous start, if not create file when counter is started
    # first time start
    # if file exists, capture current time and report how long since last counter reset
    now = datetime.datetime.now()
    start_date = first_run(now)
    write_date_to_file(start_date)

def first_run(now):
    cmd = input('Welcome to Day Counter. Would you like to start the counter for the first time (press y)? ')
    if cmd.lower().strip() == 'y':
        start_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
        print('You started your first counter at {}:{} on {}'.format(start_time.hour, start_time.minute, start_time.date()))
    return start_time

def write_date_to_file(start_date):
    filename = os.path.abspath(os.path.join('.','dayCounterData.txt'))
    with open(filename, 'w') as fout:
        fout.write(start_date.__str__())


if __name__ == '__main__':
    main()