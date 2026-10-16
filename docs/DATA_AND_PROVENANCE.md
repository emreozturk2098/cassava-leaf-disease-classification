# Data, evidence and sharing
This portfolio groups two course studies by task, while preserving their source distinctions:

| Study | Dataset evidence | Evaluation evidence |
|---|---|---|
| EE470 | Presentation: 10,965 training images; currently supplied Train folder: 10,972 JPEGs | Instructor later supplied 500 test images by email; report `_3` selected as main available version |
| CS523 | Supplied class chart and report: 21,397 training images | Three-fold stratified validation, no separate final test |

EE470's current Test folder contains 100 images per class. The current train folder has 10,972 files and 10,965 unique SHA256 contents; the 500-image test folder has no exact hash overlap with train. Near-duplicates have not been audited; the historic internal shuffled/batched split also needs review before treating it as independently verified. Current folders are not assumed to be an exact reconstruction of every historic run.

CS523 source examples and class labels come from the existing course materials. The source benchmark is the Kaggle Cassava Leaf Disease Classification competition, associated with Makerere University AI Lab. No source image collection is redistributed in bulk; only five report examples are included. This academic repository is public by user authorization. Source-specific dataset/image terms still apply; no blanket licence is assigned.

Figures are unchanged copies. EE470 images are extracted from original presentation media; original academic reports and slides are now included under reports/. The manifest records source filenames and checksums. Original reports and EE470 notebooks are now archived, retaining source authorship and machine-specific paths. Model weights and a full original CS523 pipeline are unavailable. Results were not recomputed. Code provenance is described in the examples README.

See [current folder-integrity audit](DATASET_ACCESS_AND_SPLITS.md) before using the other experiment folders as validation/test sets.
