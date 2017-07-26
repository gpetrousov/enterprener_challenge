import datetime
import time

"""Find the closest prime integer (seconds) since the time you went out for a drink.""" 

def isprime(n):
    """Check if integer n>3 is a prime"""
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

if __name__ == "__main__":
    # say you went out on this date, yes you have remember the seconds too!
    last_date_out = datetime.datetime(year=2017, month=7, day=25, hour=21, minute=23, second=51)
    current_date = datetime.datetime.now()
    while True:
        timedelta = datetime.datetime.now() - last_date_out
        if isprime(timedelta.seconds):
            print timedelta.seconds
            break
        time.sleep(1)
