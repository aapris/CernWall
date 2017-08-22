# CernWall

Cernwall is a collection of Arduino and Python scripts, 
configuration files, documentation etc.,
designed to drive WS2812 LED strips.

# Installing everything on Raspberry Pi
Use ssh or local keyboard to log in Raspberry Pi 3 running 
Raspbian 2017-08-16-raspbian-stretch-lite.img
or perhaps some newer version.

# Install mandatory packages to install the rest
Log in to Raspberry pi and issue following commands:

## Install mandatory packages to install the rest
```
sudo apt update && sudo apt -y install git python-pip python-dev libyaml-dev libffi-dev libssl-dev cdbs sshpass
```

## Install Ansible (this will take some time)
```
sudo pip install "ansible<=2.4"
```

# Clone the repository
```
cd /home/pi
git clone https://github.com/aapris/CernWall
```

# Run ansible playbook to install everything
```
cd CernWall/ansible
ansible-playbook -i "cernwallcam," -c local cernwall.yml  --extra-vars "ap_ssid=SSID ap_passphrase=PASSWORD hostname=HOSTNAME"
```

This will take some time, so crab a cup of coffee or tea.
