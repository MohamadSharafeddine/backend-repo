import yaml
import os

class Server:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.server_ip = self.config['ServerIPAddress']

    def run(self):
        print(f'Current Server IP: {self.server_ip}')

if __name__ == "__main__":
    client = Server()
    client.run()