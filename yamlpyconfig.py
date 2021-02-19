import yaml
import os


class YamlPyConfig:
    '''
    Class is based on Artur Kuzin talk "DL Pipelines tips & tricks" (https://www.youtube.com/watch?v=W5GFH1erQ4U)
    '''
    def __init__(self, base_config, conf_path='./configs', logs_path='./logs', save_conf=True,
                 log_name_key='log_name', log_dir_key='log_dir'):
        '''
        Config parameters initialization
        :param base_config: default config file (without 'yaml' extension) name from conf_path folder
        :param conf_path: folder with configuration files
        :param logs_path: path to folder with logging data
        :param save_conf: flag to save final config to logging data folder
        :param log_name_key: key (parameter) name for logging or experiment name
        :param log_dir_key: key name for parameter with full path to logging data folder
        '''
        self.base_config = base_config
        self.conf_path = conf_path
        self.logs_path = logs_path
        self.save_conf = save_conf
        self.log_name_key = log_name_key
        self.log_dir_key = log_dir_key

    def _update_config(self, config, params):
        for k, v in params.items():
            *path, key = k.split(".")
            print(f'Overwriting {k} = {v} (was {config.get(key)})')
            config.update({k: v})
        return config

    def fit_config(self, **kwargs):
        # Read base config
        with open(os.path.join(self.conf_path, self.base_config + '.yml'), 'r') as f:
            main_cfg = yaml.load(f, Loader=yaml.FullLoader)
        # Update config with yaml data config file specified in command line
        if 'config' in kwargs.keys():
            cfg_name = kwargs['config']
            with open(os.path.join(self.conf_path, cfg_name + '.yml'), 'r') as f:
                read_cfg = yaml.load(f, Loader=yaml.FullLoader)
                main_cfg = self._update_config(main_cfg, read_cfg)

        # Update config with command line options
        update_cfg = self._update_config(main_cfg, kwargs)

        update_cfg[self.log_dir_key] = os.path.join(self.logs_path, update_cfg[self.log_name_key])
        os.makedirs(update_cfg[self.log_dir_key], exist_ok=True)
        # Save yaml
        if self.save_conf:
            with open(os.path.join(update_cfg[self.log_dir_key], 'config.yaml'), 'w') as f:
                yaml.dump(update_cfg, f)
        return update_cfg

