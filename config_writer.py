from config_parser.Config import Config

conf = Config()
conf.get_file_config('test')
conf.get_data('TEST', 'hello')
conf.get_data('TEST', 'yolo')
conf.get_data('NIMP', 'wut')

# conf.write_in_file('test2')


