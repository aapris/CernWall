Automated CernWall install to Raspbian Stretch
==============================================================
This repository contains Ansible-playbooks for automatically
install and configure CernWall systemäs Raspberry pi 3 computer

Usage
-----

ansible-playbook -vvvv -i "cernwall," -c local cernwall.yml  --extra-vars "ap_ssid=SSID ap_passphrase=PASS hostname=cernwall"
