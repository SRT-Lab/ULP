# ULP : A powerful log parsing approach for large log files

## Requirements

* python 3.7+ 
* pandas
* numpy
* regex


## Directory Structure
- `main folder`: code of ULP and helpers libraries
- `input`: benchmark logs and groundtruth files (Provided by [Zhu et al.](https://dl.acm.org/doi/10.1109/ICSE-SEIP.2019.00021))
- `output` : result of the parsing including the csv file containing the templates detected and some analysis file in comparison to the groundtruth


# Installation:
 execute install.sh on your machine. 
 Note : It only works for Linux and MacOs systems
Simply use the following command:
```bash
bash install.sh
```
or
```sh
sh install.sh
```

# Execution script:
- got to your python code repository
- If you want to run all the techniques, use option `-dataset` as follows:
``` python ULP_exec.py -dataset=HPC (you can change the dataset)```

# Output
The result of parsing the log file will be a csv file under the output folder in additon to some evaluation reports on the accuracy of the parsing with comparison to the groundtruth.
