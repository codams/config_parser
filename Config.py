import configparser


class Config:
    """Simple configuration class"""

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.current_file = None

    def add_section(self, section_name):
        """
        Add a section to self.config
        :param section_name: explicit
        """
        self.config[section_name] = {}

    def add_data(self, section, key, data):
        """
        Add a key and data in section to self.config
        :param section: explicit
        :param key: explicit
        :param data: explicit
        """
        self.config[section][key] = data

    def get_file_config(self, file_name, ext=None):
        """
        Set self.config with ini file config
        format : https://docs.python.org/3.5/library/configparser.html#supported-ini-file-structure
        :param file_name: name of config file without extension
        """
        self.current_file = file_name
        if ext:
            self.config.read(file_name + "." + ext)
        else:
            self.config.read(file_name + ".ini")

    def write_in_file(self, file_name, ext=None):
        """
        Write configuration in a given file
        :param file_name: name of file without extension
        """
        self.current_file = file_name
        if ext:
            with open(file_name + "." + ext, 'w') as configfile:
                self.config.write(configfile)
        else:
            with open(file_name + ".ini", 'w') as configfile:
                self.config.write(configfile)

    def __config_as_string(self):
        """
        Give back a string to be written in file.ini
        :return: the string formatted
        """
        config_as_string = ""
        for section in self.config:
            config_as_string += "[" + section + "]\n"
            for el in self.config[section]:
                config_as_string += el + "=" + self.config[section][el] + "\n"
        return config_as_string

    def print_as_string(self):
        """
        print self.config well formatted
        """
        for section in self.config:
            print("[" + section + "]\n")
            for el in self.config[section]:
                print(el + "=" + self.config[section][el] + "\n")

    def get_current_file_name(self):
        """
        Give the current file name
        :return: string ; file name
        """
        return self.current_file

    def get_data(self, section, key):
        """
        Get a key value with a section and a key given
        :param section:  [section]
        :param key: [section][key]
        :return: data in [section][[key]
        """
        section_ok = False
        try:
            # To make sure section exist
            if self.config[section]:
                # To print the well error message
                section_ok = True
                if self.config[section][key]:
                    return self.config[section][key]

        except KeyError as key_error:
            if section_ok:
                print("Key : {wrong} does not exist, you should add it before trying to get it it.".format(wrong=key_error))
            else:
                print("Section : {wrong} does not exist, you should add it before trying to get it it.".format(wrong=key_error))







