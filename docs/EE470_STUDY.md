# EE470 — CNN from scratch

Undergraduate course research by Emre Öztürk and Ali Baki Türköz at Yeditepe University. Emre confirmed that all stages were conducted jointly and equally. This local portfolio draft explains image preparation, CNN development and the interpretation of saved results.

## Task and method
Classify RGB images into healthy Cassava and four disease categories: bacterial blight, brown streak disease, green mottle and mosaic disease. The presentation describes a 10,965-image collection, resizing to 256×256, batch size 32 and a CNN trained from scratch in TensorFlow/Keras. Experiments compared the full dataset, removal of irrelevant images and class balancing to 987 images per class.

The selected source defines convolution/pooling blocks, dropout, a dense classifier, rescaling and early stopping. Augmentation is discussed in the presentation and defined in parts of the source, but the inspected final training script does not insert its augmentation object into the model. This distinction is retained rather than silently rewriting the history.

## Latest available report outcome
| Source | Reported value | Scope |
|---|---:|---|
| Presentation, slide 16 | 92.04% | Training accuracy |
| Presentation, slide 19 | 59.80% | 500 test images |
| Report `_3`, conclusion | 55%; loss 1.6717 | 500 test images |

The main reported outcome uses the latest available numbered report (`_3`): **55% accuracy on 500 instructor-supplied test images**, with reported loss 1.6717. The report creation metadata is dated 20 May 2024; the presentation has an earlier creation date and no usable last-modified date. This supports selecting the latest available report version, but does not prove the chronology of every experimental run. The presentation's 59.80% is retained only as a different archived source statement, not the selected final score. These are historical source statements, not newly executed evaluations. Earlier notebook trials have other metrics and must not be merged with the final presentation. No saved `.h5` model was found, so the historic final model cannot currently be rerun. Emre clarified that the team did not initially have the external test set: the course instructor later sent it by email, and the team evaluated the model on it. This instructor-supplied 500-image set is separate in provenance from the internally described 80/10/10 split. Whether hyperparameters or model versions changed after inspecting its results is not documented, so it is not described as a verified untouched blind test. The currently supplied folders contain 10,972 Train JPEGs (presentation: 10,965) and 500 Test JPEGs, with 100 per Test class. No filename overlap was found across these folders; content-level or near-duplicate overlap was not checked. These current file counts do not prove the historic run used exactly the same files.

## Selected code and limitations
`../examples/ee470_architecture_excerpt.py` preserves selected original architecture definitions; full training orchestration, local paths, personal Colab links and complete image data are omitted. The source script was parsed statically, not executed or retrained. TensorFlow compatibility and original-result reproduction are unverified.

The original dataset partition helper shuffles a batched dataset and then creates separate take/skip branches, without freezing an immutable split manifest. This requires review for train/validation/test overlap before using the original split as a reliable independent test. A future cleaned implementation should create deterministic file-level split lists and verify non-overlap.

This study sits beside CS523 in the same private portfolio because they address the same task. The dataset and validation protocols remain separate. Student identifiers and complete source reports are excluded.

## Presentation evidence
[Saved model-summary and learning-curve images](FIGURE_GALLERY.md) were extracted from slides 15, 17 and 18. They do not independently establish the selected instructor-test score.
