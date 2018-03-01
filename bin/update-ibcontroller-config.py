#!/usr/bin/env python3

import sys, os.path, re, argparse

parser = argparse.ArgumentParser(description='Update IBController configuration file.')
parser.add_argument('filepath', type=str, help='Absolute file path to IBController configuration file')
parser.add_argument('login', type=str, help='IB account login ID')
parser.add_argument('password', type=str, help='Unencrypted IB account password')
parser.add_argument('--enable-logging', help='Enable logging to console', action="store_true")
parser.add_argument('--mode', type=str, help='Specify trading mode', choices=['live', 'paper'])
parser.add_argument('--port', type=int, help='API port', default=4001)

args = parser.parse_args()

file_path = args.filepath
login = args.login
password = args.password
enable_logging = args.enable_logging
trading_mode = args.mode
api_port = args.port

if(not os.path.isfile(file_path)):
    print(file_path + " is not a file.", file=sys.stderr)
    exit(-1)

file_content = None

with open(file_path, "r") as file:
    file_content = file.read()
    file_content = re.sub("^IbLoginId=([a-zA-Z0-9]*)$", "IbLoginId=" + login,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^IbPassword=([a-zA-Z0-9]*)$", "IbPassword=" + password,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^LogToConsole=([a-zA-Z0-9]*)$", "LogToConsole=" + ("yes" if enable_logging else "no"),  file_content, 1, re.MULTILINE)
    file_content = re.sub("^TradingMode=([a-zA-Z0-9]*)$", "TradingMode=" + trading_mode,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^ForceTwsApiPort=([a-zA-Z0-9]*)$", "ForceTwsApiPort=" + str(api_port), file_content, 1, re.MULTILINE)


with open(file_path, "w") as file:
    file.write(file_content)