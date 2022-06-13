# Tools for Ligen autotuning

[`aMLLibrary`](https://github.com/aMLLibrary/aMLLibrary) is an open-source, high-level Python package that uses supervised Machine Learning (ML) techniques to train regression models on a given dataset.
It is included as a submodule in this repository.

The `ligen_aml_config_files` folder contains examples of text configuration files used for Ligen autotuning of `aMLLibrary`.

## Usage example
In order to run the library with a given configuration, please run the following command-line instruction inside the `aMLLibrary` folder:
```shell
python3 run.py -c <path/to/config_file.ini> -o output_my_example
```
You will also have to edit the configuration file accordingly, by writing the appropriate location of the used datasets, which are available under the `datasets` folder of this repository.
Alternatively, you can move the dataset to the `inputs` subfolder and use the configuration file as is.

## Docker container
If you experience errors or version mismatches, you might want to use the Docker container for `aMLLibrary`.
It is not strictly needed, but it ensures an environment in which dependencies have the correct version, and in which it is guaranteed that the library works correctly.
This Docker image can be built from the `Dockerfile` at the root folder of the `aMLLibrary` repository by typing:
```shell
sudo docker build -t amllibrary .
```
To run a container and mount a volume which includes the root folder of this repository, please use
```shell
sudo docker run --name aml --rm -v $(pwd):/aMLlibrary -it amllibrary
```
which defaults to a `bash` terminal unless a specific command is appended to the line.
In this terminal, you may run the same commands as in a regular terminal.

## Documentation
Please check out the [aMLLibrary](https://github.com/aMLLibrary/aMLLibrary) repository and documentation for more information.


# Plotting tools
This repository also contains some Python scripts which produce some plots to help visualize the Ligen datasets.
They can be executed as simply as:
```shell
python3 analysis.py
```
Produced plots will be saved in the `plots` folder of this repository.
