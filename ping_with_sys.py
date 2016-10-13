import subprocess
import re

# ip = '192.168.0.114'
# ip = '10.29.27.107'

def get_ping(ip, p_type, osystem, num_pings):

    osx = "OSX"
    windows = "Windows"
    linux = "Linux"

    if osystem == windows:
        output = subprocess.check_output(['ping', '-n', num_pings, ip])
    elif osystem == linux:
        pass # TODO
    elif osystem == osx:
        output = subprocess.check_output(['ping', '-c', num_pings, ip])

    if osystem == windows:
        if p_type == "min":
            pattern = r'(Minimum = )(\d*)(ms)'
        elif p_type == "max":
           pattern = r'(Maximum = )(\d*)(ms)'
        elif p_type == "avg":
            pattern = r'(Average = )(\d*)(ms)'
        else: 
            return "Invalid Ping Type"
    
        results = re.findall(pattern, output)
        index = 1
        min_ping = int(results[0][index])
        return min_ping

    if osystem == osx:
        pattern = r' = (\d*\.\d*)\/(\d*\.\d*)\/(\d*\.\d*)\/(\d*.\d*) ms'
        results = re.findall(pattern, output)

        if p_type == "min":
            return results[0][0]
        elif p_type == "max":
           return results[0][2]
        elif p_type == "avg":
            return results[0][1]
        else: 
            return "Invalid Ping Type"


def get_max_ping_windows(input_str):
    pattern = r'(Maximum = )(\d*)(ms)'
    results = re.findall(pattern, input_str)
    index = 1
    min_ping = int(results[0][index])
    return min_ping

def get_avg_ping_windows(input_str):
    pattern = r'(Average = )(\d*)(ms)'
    results = re.findall(pattern, input_str)
    index = 1
    min_ping = int(results[0][index])
    return min_ping
 
# print get_ping("google.com", "max", "OSX", "10")
