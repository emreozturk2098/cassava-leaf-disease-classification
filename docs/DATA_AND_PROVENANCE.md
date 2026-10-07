# Data, evidence and sharing
This portfolio groups two course studies by task, while preserving their source distinctions:

| Study | Dataset evidence | Evaluation evidence |
|---|---|---|
| EE470 | Presentation: 10,965 training images; currently supplied Train folder: 10,972 JPEGs | Instructor later supplied 500 test images by email; report `_3` selected as main available version |
| CS523 | Supplied class chart and report: 21,397 training images | Three-fold stratified validation, no separate final test |

EE470's current Test folder contains 100 images per class. Current Train/Test filenames do not overlap, but content hashes and near-duplicates have not been audited; the historic internal shuffled/batched split also needs review before treating it as independently verified. Current folders are not assumed to be an exact reconstruction of every historic run.

CS523 source examples and class labels come from the existing course materials. The source benchmark is the Kaggle Cassava Leaf Disease Classification competition, associated with Makerere University AI Lab. No source image collection is redistributed in bulk; only five report examples are included. Public release, image redistribution rights and code licensing require a separate decision. The repo remains private with no blanket licence assignment.

Figures are unchanged copies. EE470 images are extracted from original presentation media; complete slides/report with student identifiers are not uploaded. The manifest records source filenames and checksums. Full reports, private paths, emails, internal source notebooks and model weights are excluded from this package. Results were not recomputed. Code provenance is described in the examples README.
