# Compound PCFG Chunker

This repository contains code for using Compound PCFG for unsupervised chunking: 

[Compound Probabilistic Context-Free Grammars for Grammar Induction](https://arxiv.org/abs/1906.10225)  
Yoon Kim, Chris Dyer, Alexander Rush  
ACL 2019  


## Dependencies
The code was tested in `python 3.6` and `pytorch 1.0`. 

## Compound PCFG + Maximal left-branching heuristic
To retrieve sentences from CoNLL-2000 dataset, run

```
python create_conll.py 
```

To use 
- the Compound PCFG on retrieved sentences to produce parse trees and  
- generate chunk labels from output parse trees using maximal left-branching heuristic, run


```
python chunk.py --data_file PATH --tag_file PATH --model_file train/data_train_tags.pkl --out_file PATH- -use_mean 1 --gpu 0
```
  
We build this repo on top of [Compund PCFG](https://github.com/harvardnlp/compound-pcfg)


## Additional Acknowledgements
- [Recurrent Neural Network Grammars](https://github.com/clab/rnng)  
- [Parsing Reading Predict Network](https://github.com/yikangshen/PRPN)  
- [Ordered Neurons](https://github.com/yikangshen/Ordered-Neurons)  

