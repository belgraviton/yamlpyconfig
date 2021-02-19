import os
import torch
from addict import Dict
from fire import Fire
from yamlpyconfig import YamlPyConfig

def main(cfg):

    # Path
    ds_path = os.path.join('./ds', cfg.ds_name)
    device = 'cuda' if int(cfg.gpu) >= 0 else 'cpu'

    # ------------ M O D E L ------------------------
    # model = BaseModel(cfg.model_name, pool_type=cfg.model_pool, head_type=cfg.model_head,
    #                  dropout_prob=cfg.model_do, input_size=cfg.aug_crop_size, model_pretrained=cfg.model_pretrained)
    #
    # model.to(device)

    # ------------ D A T A ------------------------
    # Set data_transforms and data_loaders

    # ------------ T R A I N I N G   S C H E D U L E R ------------------------
    # if cfg.opt_name == 'SGD':
    #     optimizer = torch.optim.SGD(model.parameters(), cfg.lr, momentum=cfg.momentum)
    # elif cfg.opt_name == 'Adam':
    #     optimizer = torch.optim.Adam(model.parameters(), cfg.lr)
    # else:
    #     print(f'ERROR: no appropriate optimizer in config ({cfg.opt_name})')
    #
    # criterion = torch.nn.CrossEntropyLoss()
    #
    # if cfg.sched_name == 'cos':
    #     scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, cfg.epochs, eta_min=cfg.sched_eta_min)
    # elif cfg.sched_name == 'plt':
    #     scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.1, patience=cfg.sched_patience, verbose=True)

    # ------------ T R A I N ------------------------
    # Train loop


if __name__=='__main__':
    # Set name of default config file in ./configs  folder
    yconf = YamlPyConfig('default_config')
    cfg = Dict(Fire(yconf.fit_config))

    # Run main
    main(cfg)
