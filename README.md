# ULP : A Universal Log Parsing Tool
ULP is a highly accurate log parsing tool, the ability to extract templates from unstructured log data. ULP learns from sample log data to recognize future log events. It combines pattern matching and frequency analysis techniques. First, log events are organized into groups using a text processing method. Frequency analysis is then applied locally to instances of the same group to identify static and dynamic content of log events. When applied to 10 log datasets of the LogPai benchmark, ULP achieves an average accuracy of 89.2%, which outperforms the accuracy of four leading log parsing tools, namely Drain, Logram, SPELL and AEL. Additionally, ULP can parse up to four million log events in less than 3 minutes. ULP can be readily used by practitioners and researchers to parse effectively and efficiently large log files so as to support log analysis tasks.

## Citation:

If you use ULP, please cite the following paper: 

I. Sedki, A. Hamou-Lhadj, O. Ait-Mohamed, M. Shehab, "An Effective Approach for Parsing Large Log Files," in Proc. of the 38th IEEE International Conference on Software Maintenance and Evolution (ICSME'22), 2022.

The paper can be downloaded here:  https://users.encs.concordia.ca/~abdelw/papers/ICSME2022_ULP.pdf

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
``` python ULP_exec.py -dataset=HPC``` (you can change the dataset fi needed, just make sure the 2 input files are present in the input folder)

# Output
The result of parsing the log file will be a csv file under the output folder in additon to some evaluation reports on the accuracy of the parsing with comparison to the groundtruth.
