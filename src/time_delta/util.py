from datetime import datetime

def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    
    difference = abs((time1 - time2).total_seconds())
    return str(int(difference))