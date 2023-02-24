## Public Introduction

#### What is it:

The simple data arrangement of similar products retrieval platform proposed in the paper:
"[Unified Vision-Language Representation Modeling for E-Commerce Same-Style Products Retrieval](https://arxiv.org/abs/2302.05093)". (Accepted in WWW2023 Industry track).

<p align="center">
  <img width="450" height="300" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/psp_demo.jpg">
</p>
<h5 align="center">
Similar products retrieval platform for search engine in alibaba.com
</h5>

#### Abstract:

Same-style products retrieval plays an important role in e-commerce platforms, aiming to identify the same products which may have different text descriptions or images. It can be used for similar products retrieval from different suppliers or duplicate products detection of one supplier. Here we propose a unified vision-language modeling method for e-commerce same-style products retrieval, which is designed to represent one product with its textual descriptions and visual contents. It contains one sampling skill to collect positive pairs from user click log with category and relevance constrained, and a novel contrastive loss unit to model the image, text, and image+text representations into one joint embedding space. 

It is capable of cross-modal product-to-product retrieval, as well as style transfer and user-interactive search. Offline evaluations on annotated data demonstrate its superior retrieval performance, and online testings show it can attract more clicks and conversions. Moreover, this model has already been deployed online for similar products retrieval for the `search`, `homepage recommender` and `you-shopping-history` modules in [alibaba.com](www.alibaba.com), the largest B2B e-commerce platform in the world.

<p align="center">
  <img width="500" height="171" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/model_structure.png">
</p>
<h5 align="center">
The overview of proposed contrastive loss unit. We mainly show the PPM construction method for brevity.
</h5>

#### Content in it:

1、10 pairs annotated testing data cases (random sampled from all 4196 pairs).

2、Key code implementations of loss function involved in the paper, and corresponding description of the training config.

3、More cross-modal testing results of offline experiments, which contains the image-to-image, image-to-text, image-to-(image+text), text-to-image, text-to-text, text-to-(image+text) and (image+text)-to-(image+text).

4、The application demo of proposed methods in alibaba.com (APP version).

#### As a side note:
All data, code implements may be released to public through [official repository](https://github.com/alibaba), as well as the adaptive testing results for modern dual-stream models like CLIP  and Align.

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

### Similar products retrieval demo

The overview of the similar products retrieval platform in alibaba.com, where "From more suppliers" means the same-style products from different suppliers.

<p align="center">
  <img width="450" height="300" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/psp_demo.jpg">
</p>
<h5 align="center">
Similar products retrieval platform for search engine in alibaba.com
</h5>

### User-interactive search demo

A mug with owl design + "3D frog" words can search the frog shape mugs, and a red dress + "white" get the white dresses.

<p align="center">
  <img width="450" height="170" src="https://github.com/benchen4395/esspr_alibaba.com/blob/main/model_implement_details/user_interactive_search_demo.jpg">
</p>
<h5 align="center">
User-interactive search cases with proposed model. 
</h5>


You can find the corresponding video demo of similar products retrieval at alibaba.com (APP version) at [Alibaba.com Similar Products Retrieval Demo](https://pan.baidu.com/s/1zozt_PRfG2ddxeYaw67dgA?pwd=276p).
