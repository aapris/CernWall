# CernWall

Cernwall is a collection of Arduino and Python scripts, 
configuration files, documentation etc.,
designed to drive WS2812 LED strips.

Note that code for ESP8266 is in another github repository:
https://github.com/aapris/WS2812FX

# Installing everything on Raspberry Pi
Use ssh or local keyboard to log in Raspberry Pi 3 running 
Raspbian 2017-08-16-raspbian-stretch-lite.img
or perhaps some newer version.

On Mac Os X command might be something like this (it may take a couple of minutes):

```
time sudo dd bs=4m if=2017-08-16-raspbian-stretch-lite.img of=/dev/rdisk2
```

After successful installation of Raspbian, log in to Raspberry Pi and issue following commands:

## Install mandatory packages to install the rest
```
sudo apt update && sudo apt -y upgrade && sudo apt -y install git python-pip python-dev libyaml-dev libffi-dev libssl-dev cdbs sshpass
```

## Install Ansible
This will take some time, maybe more than 10 minutes.
```
sudo pip install "ansible<2.4"
```

# Clone this repository
```
cd /home/pi
git clone https://github.com/aapris/CernWall
```

# Run ansible playbook to install everything (this will take ~10-20 minutes)
```
cd CernWall/ansible
ansible-playbook -vv -i "cernwall," -c local cernwall.yml  --extra-vars "ap_ssid=SSID ap_passphrase=PASSWORD hostname=HOSTNAME"
```

*NOTE:* You *MUST* change correct `SSID`, `PASSWORD` and `HOSTNAME` in the command above! 
In other case things are not going to work! 
Consult the author or CernWall's management staff to get the right values.

*NOTE:* This will take some time, so crab a cup of coffee or tea.

# Updating ESP's firmware

If you ever have to update the firmware of ESP8266 which is controlling the LED lighs, 
you can do it from Raspi.

Get precompiled binary `esp8266_webinterface.ino.d1_mini.bin`.

Install esptool:
`pip install esptool`

Flash the firmware
`/home/pi/.local/bin/esptool.py --port /dev/ttyUSB0 write_flash 0x00000 esp8266_webinterface.ino.d1_mini.bin && screen /dev/ttyUSB0 115200`

