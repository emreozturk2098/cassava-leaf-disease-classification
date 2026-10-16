# Dataset access and current-folder integrity
## CS523
The supplied final course report identifies the Kaggle Cassava Leaf Disease Classification benchmark. Obtain it from its original competition source under the source terms; do not treat EE470 folders as a reconstruction of the CS523 split. The full original CS523 training pipeline is not recovered.

## EE470 local source folders
The repository contains metadata/checksums in data/ee470_inventory.csv, not a bulk image mirror. Use the corresponding original class-folder structure when adapting the archived training code. The instructor-supplied 500-image test set was delivered separately by email, as confirmed by Emre. It cannot be recreated by downloading a random split and calling it the same test.

A SHA256 audit of the current supplied folder files found:
- `train`: 10,972 JPEG files, **10,965 unique contents** (seven duplicate-file occurrences).
- `test`: 500 JPEG files, 500 unique contents; **zero exact content overlap with train**.
- `valid_deneme` (100), `test_200_veri` (150), and `Leaf_200_er_veri` (1,000) consist entirely of images also present in train. They are experiment subsets, **not independent validation/test evidence**.
- The unrelated Cat_Dog examples are excluded from this Cassava archive.

The overlap check is exact-content SHA256, not perceptual/near-duplicate analysis. It describes the current local folders, not every historical notebook run. For new experiments, deduplicate by content before creating train/validation partitions, fit preprocessing only on training data, and retain the instructor test set independently. Original archives and reported historical results have not been changed or retrained. The complete folder-pair audit is in data/ee470_exact_duplicate_audit.json.
