# Intro

Muliwai (pronounced: mu-lee-why, meaning river in Hawaiian) is a library that includes PII prpcessing functionality. The original muliwai text augmentation code has been moved to https://github.com/ontocord/rio. The muliwai repo now has code only for doing PII only. It is intended for experimentation with different ways to create a PII framework that can interoperate with other PII libraries such as Presidio. See also https://github.com/piisa/piisa/blob/main/docs/specs.md

# What is it
Muliwai was written in part to support the privacy data-tooling efforts of the BigScience workshop (https://github.com/bigscience-workshop/data_tooling) and the PII hackathon conducted by the AISC community (https://github.com/Aggregate-Intellect/bigscience_aisc_pii_detection), but has grown beyond this. There are several utilities for performing NER and assocaited augmentation and anonymization. In theory, Muliwai can do NER in most of the languages supported by XLMRoberta, however, we have not tested various languages beyond: ar, ur, bn, hi, eu, ca, vi, zh, fr, id, es, pt,  sw, yo. 

# Disclaimer
While we have code to detect and anonymize PII in this library, this library is NOT intended as a production ready general PII protection engine. This is a WIP and for experimentation only.

# License
- The source code authored by Ontocord LLC and contributed by contributors of this project is licensed under Apache 2.0.
- The TurkuNLP sample data is based on OSCAR and mc4. See the information uder turkunlp_data for more details.

# Contributors
We welcome all contributions. Please feel free to send a PR. Please follow the code of conduct: https://github.com/ontocord/rio/blob/main/CODE_OF_CONDUCT.md 
Special thanks to these people not just for code contributions but for comments and reviews (in no particular order): 
- @dadelani
- @edugp 
- @vumichien
- @ianyu93
- @j-chim
- @justinphan3110
- @mapama247
- @paulovn
- @PierreColombo
- @piesauce
- @mmitchellai
- @shamikbose

# Acknowledgements

We heavily use the models trained by @dadelani and the excelent work by https://github.com/masakhane-io.
