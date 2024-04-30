# Tools for LiGen autotuning

## Parallel Asynchronous Bayesian Optimization-Machine Learning (PAMaliboo)
The [`PAMaliboo`](https://github.com/brunoguindani/PAMaliboo) submodule contains a library for parallel optimization via BO techniques hybridized with ML models, including classes specifically tailored for the LiGen optimization.

The `ligen_simulated_campaign.py` script is an example of statistically robust exploration campaign for finding the best LiGen configuration.


## aMLLibrary
[`aMLLibrary`](https://github.com/aMLLibrary/aMLLibrary) is an open-source, high-level Python package that uses supervised ML techniques to train regression models on a given dataset.
It is also included as a submodule in this repository.

The `ligen_aml_config_files` folder contains examples of text configuration files used for LiGen autotuning of `aMLLibrary`.


## Plotting tools
This repository also contains some Python scripts which produce some plots to help visualize the LiGen datasets.
They can be executed as simply as:
```shell
python3 analysis.py
```
Produced plots will be saved in the `plots` folder of this repository.
