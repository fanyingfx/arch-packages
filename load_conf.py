#!/usr/bin/env python3
import toml
import sys
import pprint

def first(l):
    return l[0]
def rest(l):
    return l[1:]

def query_config(config,key_list):
    if len(key_list)==1:
        return config[first(key_list)]
    return query_config(config[first(key_list)],rest(key_list))


if __name__=="__main__":
    config=toml.load("./computer_config.toml")
    if len(sys.argv)==1:
        pprint.pp(config)
    for arg in rest(sys.argv):
        key_list = arg.split('.')
        pprint.pp(query_config(config,key_list))

