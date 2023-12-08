import configparser

class Config:
    def __init__(self):
        self.parameter_config = configparser.ConfigParser()
        self.mode_config = configparser.ConfigParser()  # Initialize mode_config

    def read_parameter_config(self):
        print("Reading parameter.cfg")  # Debug print
        self.parameter_config.read('parameter.cfg')
        print("Sections found:", self.parameter_config.sections())  # Debug print
        if 'Modus' in self.parameter_config:
            print("Modus section found")
        else:
            print("Modus section not found")
        return self.parameter_config

    def read_mode_config(self):
        print("Reading mode.cfg")  # Debug print
        self.mode_config.read('mode.cfg')
        selected_mode = self.mode_config.get('selected mode', 'mode', fallback=None)
        if selected_mode:
            print("Selected mode found:", selected_mode)  # Debug print
        else:
            print("No selected mode found in mode.cfg")  # Debug print
        return selected_mode

    def write_mode_config(self, mode):
        print("Writing mode to mode.cfg:", mode)  # Debug print
        self.mode_config['selected mode'] = {'mode': mode.upper()}
        with open('mode.cfg', 'w') as configfile:
            self.mode_config.write(configfile)
