

import os
import time
import csv

from multiprocessing import Process
from evaluator import evaluate
from indepth_analysis import evaluate_template_level
from PA_calculator import calculate_parsing_accuracy

TIMEOUT = 3600  # log template identification timeout (sec)


def prepare_results(output_dir):
    if not os.path.exists(output_dir):
        # make output directory
        os.makedirs(output_dir)

    # make a new summary file
    result_file = 'summary_'
    with open(os.path.join(output_dir, result_file), 'w') as csv_file:
        fw = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fw.writerow(['Dataset', 'GA_time', 'PA_time', 'TA_time', 'parse_time', 'identified_templates',
                     'ground_templates', 'GA', 'PA', 'FTA', 'PTA', 'RTA', 'OG', 'UG', 'MX'])

    return result_file


def evaluator(
        dataset,
        input_dir,
        output_dir,
        log_file,
        LogParser,
        param_dict,
        result_file
):
    """
    Unit function to run the evaluation for a specific configuration.

    """

    print('\n=== Evaluation on %s ===' % dataset)
    indir= input_dir
    log_file_basename = os.path.basename(log_file)


    # identify templates using Drain
    start_time = time.time()
    parser = LogParser(**param_dict)
    p = Process(target=parser.parse, args=(log_file_basename,))
    p.start()
    p.join(timeout=TIMEOUT)
    if p.is_alive():
        print('*** TIMEOUT for Template Identification')
        p.terminate()
        return
    parse_time = time.time() - start_time  # end_time is the wall-clock time in seconds


    groundtruth = os.path.join(indir, log_file_basename + '_structured.csv')
    parsedresult = os.path.join(output_dir, log_file_basename + '_structured.csv')
    pp=parsedresult
    print("parsedresult",parsedresult)
    
    # calculate grouping accuracy
    start_time = time.time()
    _, GA = evaluate(
        groundtruth=groundtruth,
        parsedresult=pp
    )


    # calculate parsing accuracy
    start_time = time.time()
    PA = calculate_parsing_accuracy(
        groundtruth=groundtruth,
        parsedresult=parsedresult
    )


    # calculate template-level accuracy
    start_time = time.time()
    avg_accu, partial,tool_templates, ground_templates, FTA, PTA, RTA, OG, UG, SuccesInd = evaluate_template_level(
        dataset=dataset,
        groundtruth=groundtruth,
        parsedresult=parsedresult,
        output_dir=output_dir
    )
    TA_end_time = time.time() - start_time
    
    print('Number of template found Vs Groundtruth ', tool_templates, ground_templates)

    result = dataset + ',' + \
             str(tool_templates) + ',' + \
             str(ground_templates) + ',' + \
             str(avg_accu) + ',' + \
             str(GA) + ',' + \
             str(PA) + ',' + '\n'

    
    output_dir=output_dir
    with open(os.path.join(output_dir, result_file+'_ommission.csv'), 'a') as summary_file:
        summary_file.write(dataset)
        summary_file.write('\n')
        summary_file.write(str(SuccesInd))
        summary_file.write('\n')
        
    with open(os.path.join(output_dir, result_file+'_match.csv'), 'a') as summary_file:
        summary_file.write(dataset)
        summary_file.write('\n')
        summary_file.write(str(partial))
        summary_file.write('\n')
    
    with open(os.path.join(output_dir, result_file+'_accuracy.csv'), 'a') as summary_file:
        summary_file.write(dataset)
        summary_file.write(result)
        summary_file.write('\n')
