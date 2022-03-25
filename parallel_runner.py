import argparse
import os
import sys
import datetime
import behave_model

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_feature_files(working_directory, tags):
    feature_dir = ''
    feature_files = []

    for root, dirs, files in os.walk(working_directory):
        for dir in dirs:
            if dir == 'features':
                feature_dir = '{0}/{1}'.format(root, dir)
                break
    for root, dirs, files in os.walk(feature_dir):
        for dir in dirs:
            test_type_dir = '{0}/{1}'.format(root, dir)
            for test_root, test_dirs, test_files in os.walk(test_type_dir):
                for file in test_files:
                    if '.feature' in file[-8:]:
                        feature_files.append('{0}/{1}'.format(test_root, file))

    if tags:
        tagged_feature = []
        for feature in feature_files:
            for tag in tags.split(','):
                with open("{0}/{1}".format(ROOT_DIR, feature), encoding='utf-8') as f:
                    has_current_tag = False
                    for line in f.readlines():
                        if '@{}'.format(tag) in line:
                            has_current_tag = True
            if has_current_tag:
                tagged_feature.append(feature)
        feature_files = tagged_feature
    run_set = [file.replace('\\', '/') for file in feature_files]
    return run_set

# This is the starting position of the flow.
if __name__ == '__main__':
    date_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # Get all values passed from the CMD Line
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('-feature', help='feature file to run', default='All')
    parser.add_argument('-o', help='output location', default=None)
    parser.add_argument('-user', help='user name', default='local', choices={"jenkins", "local"})
    parser.add_argument('-path', help='path to behave project', default='Behave')
    parser.add_argument('-build', help='Define build number', default='0.0.0')
    parser.add_argument('-env', help='environment to run', default='qa')
    parser.add_argument('-tag', help='tags to be ran for behave', default=None)
    parser.add_argument('-zephyr', help='run with zephyr update or not', default='false')
    parser.add_argument('-run_failures', help='Run known failure', default=True)
    parser.add_argument('-folder', help='folder name for zephyr', default="test_folder")
    parser.add_argument('-limit', help='Semaphore limit', default='5')
    args = parser.parse_args()

    user = args.user
    tags = args.tag
    if user == 'jenkins':
        # implement arguments to incorporate allure report
        pass
    # This is to get the allure report in local runs
    if user == 'local':
        parser.add_argument('-o', help="Output location for the reports", default="reports/allure_report_{}".format(date_time))
        parser.add_argument('-f', help='Formatter arguments for allure report', default='allure_behave.formatter:AllureFormatter')
        args = parser.parse_args()
    args_dict = dict(vars(args))
    features = ['{0}.feature'.format(x) for x in args.feature.split(',')]
    print(features)

    working_directory = args.path
    limit = args.limit

    # Get all the feature file details that need to be run
    run_set = load_feature_files(working_directory, tags)
    print(run_set)
    threads = []
    # clear project directories
    main_dir = os.getcwd()
    features_dir = os.getcwd()

    # Add Env and User details for CMD arguments that to be passed to the runner file of Behave
    env = '-D env={0}'.format(args.env)
    user = '-D user={0}'.format(args.user)
    run_failures = '-D run_failures={0}'.format(args.run_failures)
    # print(args.o)
    # print(args.f)
    if tags is not None:
        tag_list = tags.split(',')
        for tag in tag_list:
            if tag[0] == '-':
                tag_list.remove(tag)
        tag_cmd = ['-t {}'.format(t) for t in tag_list]
        run_tag = ' '.join(tag_cmd)
    else:
        run_tag = None

    threads_status = []
    t = None
    for key, value in args_dict.items():
        print(key)
        print(value)
    # Limit the thread limiter, default is 5
    behave_model.BehaveModel.set_thread_limiter(limit)
    for i in range(0, len(run_set)):
        feature_filepath = '-D feature_filepath={0}'.format(run_set[i])
        cmd = []
        # cmd.append('-o {}'.format(args.o))
        # cmd.append('-f {}'.format(args.f))
        cmd.append('{0}'.format(run_set[i]))
        cmd.append(env)
        cmd.append(run_failures)
        cmd.append(feature_filepath)
        cmd.append(user)
        cmd.append('-k')
        if run_tag is not None:
            cmd.append(run_tag)
        print(cmd)
        cmd_line = ' '.join(cmd)
        print(cmd_line)
        # From here Behave is getting called through Threads
        t = behave_model.BehaveModel(cmd_line)
        t.setName('Thread {0}:'.format(i))
        threads.append(t)
        t.start()
    for i in range(0, len(run_set)):
        threads[i].join()
        threads_status.append(int(threads[i].status))
    if sum(threads_status) != 0:
        sys.exit('Got at least one thread failure')
    else:
        sys.exit(0)
