#!/usr/bin/env python3

import sys, os.path, re, argparse

parser = argparse.ArgumentParser(description='Update IBC configuration.')
parser.add_argument('configpath', type=str, help='Absolute file path to IBC configuration file')
parser.add_argument('login', type=str, help='IB account login ID')
parser.add_argument('password', type=str, help='Unencrypted IB account password')
parser.add_argument('--enable-logging', help='Enable logging to console', action="store_true")
parser.add_argument('--mode', type=str, help='Specify trading mode', choices=['live', 'paper'])
parser.add_argument('--tws-version', type=str, help='TWS major version')
parser.add_argument('--port', type=int, help='API port', default=4000)
parser.add_argument('--accept-connections', type=str, help='How to handle incoming connections', choices=['accept', 'reject', 'manual'])

args = parser.parse_args()

config_path = args.configpath
launcher_path = "./gatewaystart.sh"
login = args.login
password = args.password
enable_logging = args.enable_logging
trading_mode = args.mode
tws_version = args.tws_version
api_port = args.port
accept_connections = args.accept_connections

if(not os.path.isfile(config_path)):
    print(config_path + " is not a file.", file=sys.stderr)
    exit(-1)

file_content = None

with open(config_path, "r") as file:
    file_content = file.read()
    file_content = re.sub("^IbLoginId=([a-zA-Z0-9]*)$", "IbLoginId=" + login,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^IbPassword=([a-zA-Z0-9]*)$", "IbPassword=" + password,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^LogToConsole=([a-zA-Z0-9]*)$", "LogToConsole=" + ("yes" if enable_logging else "no"),  file_content, 1, re.MULTILINE)
    file_content = re.sub("^TradingMode=([a-zA-Z0-9]*)$", "TradingMode=" + trading_mode,  file_content, 1, re.MULTILINE)
    file_content = re.sub("^OverrideTwsApiPort=([a-zA-Z0-9]*)$", "OverrideTwsApiPort=" + str(api_port), file_content, 1, re.MULTILINE)
    file_content = re.sub("^AcceptIncomingConnectionAction=([a-zA-Z0-9]*)$", "AcceptIncomingConnectionAction=" + str(accept_connections), file_content, 1, re.MULTILINE)

with open(config_path, "w") as file:
    file.write(file_content)

with open(launcher_path, "r") as file:
    file_content = file.read()
    file_content = re.sub("^TWS_MAJOR_VRSN=([a-zA-Z0-9]*)$", "TWS_MAJOR_VRSN=" + tws_version,  file_content, 1, re.MULTILINE)

with open(launcher_path, "w") as file:
    file.write(file_content)

