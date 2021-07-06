import yaml

if __name__ == '__main__':
    stream = open("config.yaml", 'r')
    config = yaml.load(stream, Loader=yaml.FullLoader)



