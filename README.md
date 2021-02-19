# yamlpyconfig
Library for parsing yaml config files in ML training pipelines. Based on [Artur Kuzin talk "DL Pipelines tips & tricks"](https://youtu.be/W5GFH1erQ4U?t=322).

#### Benefits:
1. Config files have yaml format.
2. All parameters in python code have form 'cfg.par_name'.
3. Any parameter could be set in command line prompt.


#### There are 3 levels of configuration:
1. Default config file is set during initialization: 
   - <code>yconf = YamlPyConfig('default_config', , conf_path='./configs')</code>
   - Config file 'default_config.yaml' should be placed in './configs' folder.
   - <code>python train_example.py</code>

2. Custom config file could be set with parameter *--config*:
   - <code>python train_example.py --config custom_config</code>

3. Custom parameters could be set with appropriate keys:
   - <code>python train_example.py --config custom_config --epochs 100 --lr 0.3</code>





#### Installing Dependencies :

<code>pip install -r requirements.txt</code>