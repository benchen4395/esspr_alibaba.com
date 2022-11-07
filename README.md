## Introduction
The simple data arrangement of similar products retrieval platform for the `search`, `homepage recommender` and `you-shopping-history` modules in alibaba.com (APP version). This function is based on an unified crossmodal (vision-language) model, and its implement details is showed in the paper:
"Unified Vision-Language Representation Modeling for E-Commerce Same-Style Products Retrieval".

<p align="center">
  <img width="500" height="171" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/model_structure.png">
</p>
<h5 align="center">
The overview of proposed contrastive loss unit. We mainly show the PPM construction method for brevity.
</h5>

Here we provide:

1、10 pairs annotated testing data cases (random sampled from all 4196 pairs).

2、Key code implementations of loss function involved in the paper, and corresponding description of the training config.

3、More cross-modal testing results of offline experiments, which contains the image-to-image, image-to-text, image-to-(image+text), text-to-image, text-to-text, text-to-(image+text) and (image+text)-to-(image+text).

4、The application demo of proposed methods in alibaba.com (APP version).

All data, code implements will be released to public through [official repository](https://github.com/alibaba), as well as the adaptive testing for modern dual-stream models like CLIP  and Align.

## Offiline cross-modal testing results
Beside the image-to-image, text-to-text, (image+text)-to-(image+text), we also provide the results of `image-to-text`, `text-to-image`, `image-to-(image+text)` and `text-to-(image+text)` cross-modal testings. **All data presented are the average values of the metrics for all testings.**

|Method|MRR|Recall@1|Recall@5|Recall@10|Recall@20|
|---|:---:|:---:|:---:|:---:|:---:|
|eSSPR i-i|0.9027|0.8784|0.9355|0.9511|0.9675|
|eSSPR i-t|0.-|0.-|0.-|0.-|0.-|
|eSSPR i-m|0.8409|0.7897|0.9065|0.9398|0.9596|
|eSSPR t-i|0.-|0.-|0.-|0.-|0.-|
|eSSPR t-t|0.6428|0.5597|0.7485|0.8174|0.8761|
|eSSPR t-m|0.5753|0.4823|0.6923|0.7771|0.8455|
|eSSPR m-m|**0.9197**|**0.8870**|**0.9619**|**0.9761**|**0.9879**|

## Application Demo
<p align="center">
  <img width="450" height="300" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/psp_demo.jpg">
</p>
<h5 align="center">
Similar products retrieval platform for search engine in alibaba.com
</h5>

You can find the corresponding video demo of similar products retrieval at alibaba.com (APP version) at [Alibaba.com Similar Products Retrieval Demo](https://pan.baidu.com/s/1zozt_PRfG2ddxeYaw67dgA?pwd=276p).
