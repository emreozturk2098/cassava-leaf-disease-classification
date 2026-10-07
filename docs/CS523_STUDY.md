# CS523 — model comparisons and augmentation
Emre Öztürk and Ali Baki Türköz carried out all stages jointly and equally, as confirmed by Emre. This Özyeğin University course study compares classical pixel-based baselines and pretrained deep models on the approximately 21,397-image Cassava Leaf Disease Classification benchmark.

## Data and motivation
The five source labels are CBB, CBSD, CGM, CMD and Healthy. The provided chart records counts 1,087 / 2,189 / 2,386 / 13,158 / 2,577. CMD is 61.49% of the images. Macro-F1 gives each class equal weight, so it is more informative than accuracy alone when a majority classifier can appear successful.

## Methods described in the final report
Classical baselines: 64×64 grayscale pixels, flattening, StandardScaler, PCA retaining 95% variance, then SGD classifier, logistic regression, Extra Trees or Random Forest. The report places the pipeline within each fold.

Deep models: full fine-tuning of ImageNet-pretrained ResNet-50, EfficientNet-B4 and ViT-B/16. CNN inputs are 224×224; ViT inputs are 384×384. Optuna searches model/training settings, optimizers, schedules, losses and class weighting. The report describes mixed precision, gradient clipping and validation-loss early stopping. Original training code and trial logs are absent from this workspace, so these are report-supported descriptions rather than independently executed verification.

## Augmentation and outcome
After selecting a ViT configuration, the study compares 15 augmentation policies. The `none` row reports macro-F1 0.7812±0.0096; `heavy_combo` reports 0.7921±0.0068, a saved change of +0.0109. Selected heavy_combo accuracy is 0.8855±0.0040. The minority CBB class shows the largest saved per-class F1 gain (+0.0282). [Tables](../results/), [figures](FIGURE_GALLERY.md).

## Protocol and interpretation
All reported comparisons use three-fold stratified cross-validation. There is no separate held-out test in this study. Hyperparameters, best checkpoints and augmentation selection use validation outcomes, so the selected scores are development comparisons. The CSVs/figures retain saved evidence; they do not prove unseen-field deployment performance. Input resolution differs between architectures; an apparent ViT advantage cannot be attributed solely to architecture. Results are single-seed and not a multi-seed stability assessment.

This is an academic computer-vision study. It is not presented as a published journal paper or deployed field diagnostic tool. Raw image data and the full training code are not uploaded. Five illustrative source-labelled images are shown in [image examples](IMAGE_EXAMPLES.md).
