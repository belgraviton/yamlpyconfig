# yamlpyconfig
Library for parsing yaml config files in ML training pipelines. Based on [Artur Kuzin talk "DL Pipelines tips & tricks"](https://www.youtube.com/watch?v=W5GFH1erQ4U).

There are 3 levels of configuration:
1. Default config file is set during initialization: 
<code>yconf = YamlPyConfig('default_config')</code>

2. Custom config file could be set with parameter *--config*:
<code>python train_example.py --config custom_config</code>

3. Custom parameters could be set with selected keys:
<code>python train_example.py --config custom_config --epochs 100 --lr 0.3</code>





Install dependencies by:

<code>pip install -r requirements.txt</code>