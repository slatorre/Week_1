#!/usr/bin/env python

import yaml


sergios_list = range(3)
sergios_list.append({})
sergios_list[-1]['ip1'] = "192.168.1.1"
sergios_list.append({})
sergios_list[-1]['ip2'] = "192.168.1.2"
sergios_list.append({})
sergios_list[-1]['ip3'] = ['10.1.1.1', '10.1.1.2', '10.1.1.2']


with open("ex6_yaml.yml", "w") as f:
    f.write(yaml.dump(sergios_list, default_flow_style=False))



