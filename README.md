# Intro

Muliwai (pronounced: mu-lee-why, meaning river in Hawaiian) is a library that includes PII prpcessing functionality. This is a branch of the original muliwai text augmentation code which has been moved to https://github.com/ontocord/rio. This muliwai repo now has code for doing PII only. It is intended for experimentation with different ways to create a PII framework that can interoperate with other PII libraries such as Presidio. See also https://github.com/piisa/piisa/blob/main/docs/specs.md

# What is it
Muliwai was written in part to support the privacy data-tooling efforts of the BigScience workshop (https://github.com/bigscience-workshop/data_tooling) and the PII hackathon conducted by the AISC community (https://github.com/Aggregate-Intellect/bigscience_aisc_pii_detection), but has grown beyond this. There are several utilities for performing NER and assocaited augmentation and anonymization. In theory, Muliwai can do NER in most of the languages supported by XLMRoberta, however, we have not tested various languages beyond: ar, ur, bn, hi, eu, ca, vi, zh, fr, id, es, pt,  sw, yo. 


# Installing

Install the below which will enable spacy for other languages. You can also load a larger spacy model for more accuracy but more memory.
```
git clone https://github.com/ontocord/muliwai
pip install https://github.com/kpu/kenlm/archive/master.zip
pip install spacy==3.1.0 regex==2022.3.2 dateparser python-stdnum protobuf cdifflib transformers datasets langid faker sentencepiece fsspec tqdm sentence-transformers nltk tokenizers
python -m nltk.downloader punkt wordnet
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
python -m spacy download ca_core_news_sm
python -m spacy download pt_core_news_sm
python -m spacy download zh_core_web_sm

```

To experimental with adress detection, you should also insall libpostal:

```
sudo apt-get install curl autoconf automake libtool pkg-config
git clone https://github.com/openvenues/libpostal
cd libpostal
make distclean
./bootstrap.sh
./configure --datadir=/content/libpostal_data
make -j4
sudo make install
pip install postal
cp /usr/local/lib/libpostal.so /usr/lib/libpostal.so.1
```
 
# Disclaimer
While we have code to detect and anonymize PII in this library, this library is NOT intended as a production ready general PII protection engine. This is a WIP and for experimentation only.

# License
- The source code authored is licensed under Apache 2.0.

# Contributors
We welcome all contributions. Please feel free to send a PR. Please follow the code of conduct: https://github.com/ontocord/muliwai/blob/main/CODE_OF_CONDUCT.md 
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
