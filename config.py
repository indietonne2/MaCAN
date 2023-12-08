import configparser

class Config:
    def __init__(self):
        self.parameter_config = configparser.ConfigParser()
        self.mode_config = configparser.ConfigParser()

    def read_parameter_config(self):
        self.parameter_config.read('parameter.cfg')
        return self.parameter_config['Modus']

    def read_mode_config(self):
        self.mode_config.read('mode.cfg')
        selected_mode = self.mode_config.get('selected mode', 'mode', fallback=None)
        return selected_mode

    def write_mode_config(self, mode):
        self.mode_config['selected mode'] = {'mode': mode.upper()}
        with open('mode.cfg', 'w') as configfile:
            self.mode_config.write(configfile)
