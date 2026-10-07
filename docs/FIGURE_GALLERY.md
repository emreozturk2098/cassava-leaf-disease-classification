# Saved figures: CS523 and EE470

Images are copied unchanged from supplied project files. They show archived experiments; no model was retrained for this repository. The two studies use different datasets and evaluation protocols.

## CS523: comparative models and augmentation

### Class imbalance

![Class imbalance](../assets/cs523/fig_class_distribution.png)

21,397 images, including 13,158 CMD examples. Counts refer to the CS523 benchmark, not EE470.

### Augmentation comparison

![Augmentation comparison](../assets/cs523/fig_aug_comparison.png)

Fifteen augmentation policies compared with the selected ViT configuration. The horizontal axis is truncated near 0.77; use the numerical values rather than relative bar lengths to judge the small differences.

### No-augmentation confusion matrix

![No-augmentation confusion matrix](../assets/cs523/fig_cm_aug_none.png)

Archived baseline validation/OOF classification counts and row-normalized values.

### Heavy-combination confusion matrix

![Heavy-combination confusion matrix](../assets/cs523/fig_cm_aug_heavy.png)

Archived selected heavy_combo validation/OOF results. The saved figure reports accuracy 0.8855 and macro-F1 0.7921 in its heading.

### Training with heavy augmentation

![Training with heavy augmentation](../assets/cs523/fig_curves_aug_heavy_combo.png)

Training/validation curves across three folds for the selected heavy_combo trial.

### Pre-augmentation learning curves

![Pre-augmentation learning curves](../assets/cs523/fig_curves_best_dl.png)

Archived selected pre-augmentation trial. The rapid training fit and rising validation loss motivate examining regularization and augmentation.

### Selected pre-augmentation trial

![Selected pre-augmentation trial](../assets/cs523/fig_cm_best_dl.png)

Archived pre-augmentation OOF confusion matrix; distinct from the subsequent augmentation ablation baseline.

### Per-class metrics before augmentation

![Per-class metrics before augmentation](../assets/cs523/fig_perclass_best_dl.png)

Training and validation metrics show why minority-class performance matters alongside overall accuracy.

### Per-class augmentation changes

![Per-class augmentation changes](../assets/cs523/fig_perclass_delta.png)

The saved comparison reports the largest F1 gain for the minority CBB class. Values are descriptive results from the selected development comparison.

## EE470: model summary

![EE470 model_summary.png](../assets/ee470/model_summary.png)

The presentation model summary shows 11,008,837 parameters.

## EE470: early trial curves

![EE470 early_trial_curves.png](../assets/ee470/early_trial_curves.png)

An earlier presentation trial shows a training–validation gap; this is not the instructor test result.

## EE470: adjusted trial curves

![EE470 adjusted_trial_curves.png](../assets/ee470/adjusted_trial_curves.png)

The presentation shows a later adjusted trial. Its learning curves are internal training/validation curves, not the separate 500-image instructor test.

