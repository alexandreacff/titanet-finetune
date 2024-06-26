import nemo
import nemo.collections.asr as nemo_asr
from omegaconf import OmegaConf
import sys
import os
import torch
import pytorch_lightning as pl
from nemo.utils.exp_manager import exp_manager

manifest_path = sys.argv[1]

train_manifest = os.path.join(manifest_path, 'train.json')
validation_manifest = os.path.join(manifest_path, 'dev.json')
test_manifest = os.path.join(manifest_path, 'test.json')

MODEL_CONFIG = 'conf/titanet-finetune.yaml'
finetune_config = OmegaConf.load(MODEL_CONFIG)
print(OmegaConf.to_yaml(finetune_config))

finetune_config.model.train_ds.manifest_filepath = train_manifest
finetune_config.model.validation_ds.manifest_filepath = validation_manifest

num_classes = sys.argv[2]
finetune_config.model.decoder.num_classes = int(num_classes)

accelerator = 'gpu' if torch.cuda.is_available() else 'cpu'
print(accelerator)

finetune_config.trainer.accelerator = accelerator

trainer = pl.Trainer(**finetune_config.trainer)

log_dir = exp_manager(trainer, finetune_config.get("exp_manager", None))
print(f"Experimento sendo salvo em: {log_dir}")

speaker_model = nemo_asr.models.EncDecSpeakerLabelModel(cfg=finetune_config.model, trainer=trainer)
trainer.fit(speaker_model)
