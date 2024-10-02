#!/usr/bin/env python3
import toml
import sys
import pprint
CONFIG_FILENAME="./computer_config.toml"

def first(l):
    return l[0]
def rest(l):
    return l[1:]

def query_config(config:dict,key_list:list[str]):
    assert(len(key_list)>0) # key_list should not be empty
    if len(key_list)==1:
        return config[first(key_list)]
    return query_config(config[first(key_list)],rest(key_list))
def get_package_list(appconfig:dict):
    pacman_repos=["official","archlinuxcn"]
    pacman_list=[]
    for repo in pacman_repos:
        for app_list in appconfig[repo].values():
            pacman_list.extend(app_list)
    aur_list=[]
    for app_list in appconfig['aur'].values():
        aur_list.extend(app_list)
    return {'pacman':pacman_list,'aur':aur_list}

if __name__=="__main__":
    config=toml.load(CONFIG_FILENAME)
    if len(sys.argv)==1:
        pprint.pp(config)
    for arg in rest(sys.argv):
        key_list = arg.split('.')
        pprint.pp(query_config(config,key_list))
    # pprint.pp(get_package_list(config['applications']))

