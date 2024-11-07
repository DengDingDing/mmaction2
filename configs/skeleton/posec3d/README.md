# PoseC3D

[Revisiting Skeleton-based Action Recognition](https://arxiv.org/abs/2104.13586)

<!-- [ALGORITHM] -->

## Abstract

<!-- [ABSTRACT] -->


人体骨骼作为人类行为的紧凑表征，近年来受到越来越多的关注。许多基于骨架的动作识别方法采用图卷积网络（GCN）来提取人体骨架上的特征。尽管之前的工作取得了积极的成果，但基于 GCN 的方法在鲁棒性、互操作性和可扩展性方面仍受到限制。在这项工作中，我们提出了 PoseC3D，一种基于骨架的动作识别的新方法，它依赖 3D 热图堆栈而不是图形序列作为人体骨骼的基本表示。与基于 GCN 的方法相比，PoseC3D 在学习时空特征方面更有效，对姿态估计噪声更鲁棒，并且在跨数据集设置中具有更好的泛化能力。此外，PoseC3D可以处理多人场景，无需额外的计算成本，并且其功能可以在早期融合阶段轻松地与其他模式集成，这为进一步提升性能提供了巨大的设计空间。在四个具有挑战性的数据集上，单独用于骨骼以及与 RGB 模态结合使用时，PoseC3D 始终获得卓越的性能。

<!-- [IMAGE] -->

<div align=center>
<img src="https://user-images.githubusercontent.com/34324155/142995620-21b5536c-8cda-48cd-9cb9-50b70cab7a89.png" width="800"/>
</div>

<table>
<thead>
  <tr>
    <td>
<div align="center">
  <b> Pose Estimation Results </b>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116529341-6fc95080-a90f-11eb-8f0d-57fdb35d1ba4.gif" width="455"/>
  <br/>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116531676-04cd4900-a912-11eb-8db4-a93343bedd01.gif" width="455"/>
</div></td>
    <td>
<div align="center">
  <b> Keypoint Heatmap Volume Visualization </b>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116529336-6dff8d00-a90f-11eb-807e-4d9168997655.gif" width="256"/>
  <br/>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116531658-00a12b80-a912-11eb-957b-561c280a86da.gif" width="256"/>
</div></td>
    <td>
<div align="center">
  <b> Limb Heatmap Volume Visualization </b>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116529322-6a6c0600-a90f-11eb-81df-6fbb36230bd0.gif" width="256"/>
  <br/>
  <br/>
  <img src="https://user-images.githubusercontent.com/34324155/116531649-fed76800-a911-11eb-8ca9-0b4e58f43ad9.gif" width="256"/>
</div></td>
  </tr>
</thead>
</table>

## Results and Models

### FineGYM

| frame sampling strategy | pseudo heatmap | gpus |   backbone   | Mean Top-1 | testing protocol | FLOPs | params |                 config                 |                 ckpt                 |                 log                  |
| :---------------------: | :------------: | :--: | :----------: | :--------: | :--------------: | :---: | :----: | :------------------------------------: | :----------------------------------: | :----------------------------------: |
|       uniform 48        |    keypoint    |  8   | SlowOnly-R50 |    93.5    |     10 clips     | 20.6G |  2.0M  | [config](/configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-keypoint/slowonly_r50_8xb16-u48-240e_gym-keypoint_20220815-da338c58.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-keypoint/slowonly_r50_8xb16-u48-240e_gym-keypoint.log) |
|       uniform 48        |      limb      |  8   | SlowOnly-R50 |    93.6    |     10 clips     | 20.6G |  2.0M  | [config](/configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-limb.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-limb/slowonly_r50_8xb16-u48-240e_gym-limb_20220815-2e6e3c5c.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-limb/slowonly_r50_8xb16-u48-240e_gym-limb.log) |

### NTU60_XSub

| frame sampling strategy | pseudo heatmap | gpus |   backbone   | top1 acc | testing protocol | FLOPs | params |                 config                  |                 ckpt                  |                 log                  |
| :---------------------: | :------------: | :--: | :----------: | :------: | :--------------: | :---: | :----: | :-------------------------------------: | :-----------------------------------: | :----------------------------------: |
|       uniform 48        |    keypoint    |  8   | SlowOnly-R50 |   93.6   |     10 clips     | 20.6G |  2.0M  | [config](/configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint_20220815-38db104b.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint.log) |
|       uniform 48        |      limb      |  8   | SlowOnly-R50 |   93.5   |     10 clips     | 20.6G |  2.0M  | [config](/configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-limb/slowonly_r50_8xb16-u48-240e_ntu60-xsub-limb_20220815-af2f119a.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_ntu60-xsub-limb/slowonly_r50_8xb16-u48-240e_ntu60-xsub-limb.log) |
|                         |     Fusion     |      |              |   94.0   |                  |       |        |                                         |                                       |                                      |

### UCF101

| frame sampling strategy | pseudo heatmap | gpus |   backbone   | top1 acc | testing protocol | FLOPs | params |                 config                  |                 ckpt                  |                 log                  |
| :---------------------: | :------------: | :--: | :----------: | :------: | :--------------: | :---: | :----: | :-------------------------------------: | :-----------------------------------: | :----------------------------------: |
|       uniform 48        |    keypoint    |  8   | SlowOnly-R50 |   86.8   |     10 clips     | 14.6G |  3.1M  | [config](/configs/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_ucf101-split1-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_ucf101-split1-keypoint/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_ucf101-split1-keypoint_20220815-9972260d.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_ucf101-split1-keypoint/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_ucf101-split1-keypoint.log) |

### HMDB51

| frame sampling strategy | pseudo heatmap | gpus |   backbone   | top1 acc | testing protocol | FLOPs | params |                 config                  |                 ckpt                  |                 log                  |
| :---------------------: | :------------: | :--: | :----------: | :------: | :--------------: | :---: | :----: | :-------------------------------------: | :-----------------------------------: | :----------------------------------: |
|       uniform 48        |    keypoint    |  8   | SlowOnly-R50 |   69.6   |     10 clips     | 14.6G |  3.0M  | [config](/configs/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_hmdb51-split1-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_hmdb51-split1-keypoint/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_hmdb51-split1-keypoint_20220815-17eaa484.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_hmdb51-split1-keypoint/slowonly_kinetics400-pretrained-r50_8xb16-u48-120e_hmdb51-split1-keypoint.log) |

# Kinetics400

| frame sampling strategy | pseudo heatmap | gpus |   backbone   | top1 acc | testing protocol | FLOPs | params |                 config                  |                 ckpt                  |                 log                  |
| :---------------------: | :------------: | :--: | :----------: | :------: | :--------------: | :---: | :----: | :-------------------------------------: | :-----------------------------------: | :----------------------------------: |
|       uniform 48        |    keypoint    |  8   | SlowOnly-R50 |   47.4   |     10 clips     | 19.1G |  3.2M  | [config](/configs/skeleton/posec3d/slowonly_r50_8xb32-u48-240e_k400-keypoint.py) | [ckpt](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb32-u48-240e_k400-keypoint/slowonly_r50_8xb32-u48-240e_k400-keypoint_20230731-7f498b55.pth) | [log](https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/slowonly_r50_8xb32-u48-240e_k400-keypoint/slowonly_r50_8xb32-u48-240e_k400-keypoint.log) |

You can follow the guide in [Preparing Skeleton Dataset](/tools/data/skeleton/README.md) to obtain skeleton annotations used in the above configs.

## Train

You can use the following command to train a model.

```shell
python tools/train.py ${CONFIG_FILE} [optional arguments]
```

Example: train PoseC3D model on FineGYM dataset in a deterministic option.

```shell
python tools/train.py configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-keypoint.py \
    --seed=0 --deterministic
```

For training with your custom dataset, you can refer to [Custom Dataset Training](/configs/skeleton/posec3d/custom_dataset_training.md).

For more details, you can refer to the **Training** part in the [Training and Test Tutorial](/docs/en/user_guides/train_test.md).

## Test

You can use the following command to test a model.

```shell
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [optional arguments]
```

Example: test PoseC3D model on FineGYM dataset.

```shell
python tools/test.py configs/skeleton/posec3d/slowonly_r50_8xb16-u48-240e_gym-keypoint.py \
    checkpoints/SOME_CHECKPOINT.pth
```

For more details, you can refer to the **Test** part in the [Training and Test Tutorial](/docs/en/user_guides/train_test.md).

## Citation

```BibTeX
@misc{duan2021revisiting,
      title={Revisiting Skeleton-based Action Recognition},
      author={Haodong Duan and Yue Zhao and Kai Chen and Dian Shao and Dahua Lin and Bo Dai},
      year={2021},
      eprint={2104.13586},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
