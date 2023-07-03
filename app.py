# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iSHdfhvGEXAOREpXegvc1iUyNrAxFbco
"""

import gradio as gr
from fastai.vision.all import *

learn = load_learner('export.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Guitar Brand Classifier"
description = "A guitar brand classifier using fastai. Created as a demo for Gradio and HuggingFace Spaces."
examples = ["gibson.jpeg", "gg.jpeg","strat.jpeg"]
article = "Github repo at: https://github.com/orkunaran/guitar_brand_classifier_fast_ai"
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(512, 512)),
             outputs=gr.outputs.Label(num_top_classes=3),title=title,
             description=description,
             article=article,
             examples=examples,
             interpretation=interpretation,enable_queue=enable_queue).launch()

