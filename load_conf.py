import toml
import sys

def query_config(config,key_list):
    if len(key_list)==1:
        return config[key_list[0]]
    return query_config(config[key_list[0]],key_list[1:])


if __name__=="__main__":
    config=toml.load("./computer_config.toml")
    if len(sys.argv)==1:
        print(config)
    for arg in sys.argv[1:]:
        key_list = arg.split('.')
        print(query_config(config,key_list))

