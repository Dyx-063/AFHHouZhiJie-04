---
library_name: peft
license: other
base_model: /root/autodl-tmp/code/model/Qwen/Qwen2.5-0.5B-Instruct
tags:
- base_model:adapter:/root/autodl-tmp/code/model/Qwen/Qwen2.5-0.5B-Instruct
- llama-factory
- lora
- transformers
pipeline_tag: text-generation
model-index:
- name: train_2026-06-26-14-48-35
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# train_2026-06-26-14-48-35

This model is a fine-tuned version of [/root/autodl-tmp/code/model/Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co//root/autodl-tmp/code/model/Qwen/Qwen2.5-0.5B-Instruct) on the medical_device_quote dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9145
- Num Input Tokens Seen: 245008

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 20
- num_epochs: 20.0

### Training results



### Framework versions

- PEFT 0.18.1
- Transformers 5.6.0
- Pytorch 2.12.1+cu130
- Datasets 4.0.0
- Tokenizers 0.22.2