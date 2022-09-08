# ULP : A powerful log parsing approach for large log files
ULP is a highly accurate and efficient Unified Log Parsing tool. ULP combines string matching and local frequency analysis to parse large log files in an efficient manner. First, log events are organized into groups using a text processing method. Frequency analysis is then applied locally to instances of the same group to identify static and dynamic content of log events. When applied to 10 log datasets of the LogPai benchmark, ULP achieves an average accuracy of 89.2%, which outperforms the accuracy of four leading log parsing tools, namely Drain, Logram, SPELL and AEL. Additionally, ULP can parse up to four million log events in less than 3 minutes. ULP can be readily used by practitioners and researchers to parse effectively and efficiently large log files so as to support log analysis tasks.
Please cite our paper if you use our artefact:
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjChufMnIX6AhV-k4kEHf34BcwQFnoECBMQAQ&url=https%3A%2F%2Fusers.encs.concordia.ca%2F~abdelw%2Fpapers%2FICSME2022_ULP.pdf&usg=AOvVaw2_D3Xmmqtm2y1-PfQIwgVb

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
