# coding=utf-8
"""
edited in 2022.11.07
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import tensorflow as tf

# Get the tensor shape list
def get_shape_list(tensor):
  static = tensor.shape.as_list()
  dynamic = tf.shape(tensor)
  shape_list = [dynamic[i] if s is None else s for i, s in enumerate(static)]
  return shape_list

# Product to product matching losses (PPM)
def hinge_batch_loss(trigger_emb, offer_emb, margin, batch_size):
    # normalize embeddings
    trigger_emb_norm = tf.maximum(1e-12, tf.norm(trigger_emb, axis=1))
    trigger_emb_repr = tf.div(tf.transpose(trigger_emb),trigger_emb_norm)
    offer_emb_norm = tf.maximum(1e-12, tf.norm(offer_emb, axis=1))
    offer_emb_repr = tf.div(tf.transpose(offer_emb),offer_emb_norm)

    # cosine similarity matrix
    dis = tf.matmul(tf.transpose(trigger_emb_repr), offer_emb_repr)
    positive_distance = tf.reshape(tf.diag_part(dis), [batch_size, 1])
    hingle_loss = tf.reduce_mean(
            tf.maximum(0.,-positive_distance+dis+margin*(1- tf.eye(batch_size)))
            , axis=1)
    return hingle_loss

# Product self-distinctiveness losses (PDC)
def self_distinctiveness_loss(trigger_emb, trigger_trans_emb, offer_emb, margin):
    # normalize embeddings
    trigger_emb_norm = tf.maximum(1e-12, tf.norm(trigger_emb, axis=1))
    trigger_emb_rep = tf.div(tf.transpose(trigger_emb), trigger_emb_norm)
    trigger_trans_emb_norm = tf.maximum(1e-12, tf.norm(trigger_trans_emb, axis=1))
    trigger_trans_emb_rep = tf.div(tf.transpose(trigger_trans_emb), trigger_trans_emb_norm)
    offer_emb_norm = tf.maximum(1e-12, tf.norm(offer_emb, axis=1))
    offer_emb_rep = tf.div(tf.transpose(offer_emb), offer_emb_norm)
    batch_size = get_shape_list(trigger_emb)[0]

    # cosine similarity matrix
    dis = tf.matmul(tf.transpose(trigger_trans_emb_rep), trigger_emb_rep)
    positive_distance = tf.reshape(tf.diag_part(dis), [batch_size, 1])
    self_distinct_loss = tf.reduce_mean(
        tf.maximum(0.,-positive_distance+dis+margin*(1- tf.eye(batch_size)))
        , axis=1)
    return self_distinct_loss

def locality_consistency_loss(trigger_emb, tirgger_trans_emb, offer_emb, margin):
    # normalize embeddings
    trigger_emb_norm = tf.maximum(1e-12, tf.norm(trigger_emb, axis=1))
    trigger_emb_repr = tf.div(tf.transpose(trigger_emb), trigger_emb_norm)
    tirgger_trans_emb_norm = tf.maximum(1e-12, tf.norm(tirgger_trans_emb, axis=1))
    tirgger_trans_emb_repr = tf.div(tf.transpose(tirgger_trans_emb), tirgger_trans_emb_norm)
    offer_emb_norm = tf.maximum(1e-12, tf.norm(offer_emb, axis=1))
    offer_emb_repr = tf.div(tf.transpose(offer_emb), offer_emb_norm)

    # cosine similarity matrix
    dis = tf.matmul(tf.transpose(trigger_emb_repr), offer_emb_repr)
    trans_dis = tf.matmul(tf.transpose(tirgger_trans_emb_repr), offer_emb_repr)

    # only get top10 similar products for compute economy
    batch_size = get_shape_list(trigger_emb_norm)[0]
    values, indices  = tf.math.top_k(dis, k=10)
    idx_flattened = tf.reshape(tf.reshape(tf.range(0, batch_size) * batch_size, [-1, 1]) + indices, [-1])
    gathered_values = tf.gather(tf.reshape(tf.math.square(dis - trans_dis), [-1]),
                idx_flattened)
    gathered_values = tf.reshape(gathered_values, [-1, 10])
    locality_consistency_loss = tf.reduce_mean(
        tf.maximum(0., gathered_values - margin)
        , axis=1)   
    return locality_consistency_loss
