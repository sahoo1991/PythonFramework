import logging
import sys
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from Behave.utils.behave_browser_controller import BrowserController

test_log = logging.getLogger('qa')


def before_all(context):
    # Data passed form the command line is stored at context.config.userdata
    context.env = context.config.userdata['env']
    context.user = context.config.userdata['user']

    # for datum in context.config.userdata_defines:
    #     key = datum[0]
    #     value = datum[1]
    #     print(key)
    #     print(value)
    # try:
    #     exec('context.{}'.format(key))
    # except NameError:
    #     exec('context.{} = {}'.format(key, value))
    # print(context.env)
    # print(context.user)
    # print(context.run_failures)
    # print(context.feature_filepath)


def before_feature(context, feature):
    # Logic to skip the feature
    for tag in feature.tags:
        if any(tag in feature.tags for tag in ['skip', 'repair', 'in_progress', 'obsolete']):
            feature.skip()
            sys.stdout.write('\nFeature skipped by the user ==> %s\n' % feature.name)


def before_scenario(context, scenario):
    # Logic to skip the Scenario
    for tag in scenario.tags:
        if any(tag in scenario.tags for tag in ['skip', 'repair', 'in_progress', 'obsolete']):
            scenario.skip()
            sys.stdout.write('\nScenario skipped by the user ==> %s\n' % scenario.name)
    if 'internet_explorer' in scenario.tags:
        logging.info("WE ARE RUNNING THIS TEST IN INTERNET EXPLORER")
        context.browser_name = 'IE11'
        context.browser = BrowserController(context=context, browser_type='ie11', use_grid=True)
    if 'chrome' in scenario.tags:
        context.browser = BrowserController(context=context, browser_type='chrome', use_grid=True)
    elif 'mobile' in scenario.tags:
        context.browser = BrowserController(context=context, browser_type='mobile', use_grid=True)


def after_step(context, step):
    if step.status == 'failed':
        tag_message = "Tags of Failed scenario:"
        for tag in context.scenario.tags:
            tag_message = tag_message + tag + ','
        for tag in context.feature.tags:
            tag_message = tag_message + tag + ','
        tag_message = tag_message[0:len(tag_message) - 1]
        step_message = 'Step : [{}]'.format(step.name)
        scenario_message = 'Scenario:[{}]'.format(context.scenario.name)
        feature_message = 'Feature:[{}]'.format(context.feature.name)
        test_log.warning(feature_message + ' ' + scenario_message + " " + step_message + " " + tag_message)

        allure.attach(context.browser.driver.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)
    else:
        print('Test passed')


def after_scenario(context, scenario):
    # Do the implementation as per your requirements
    pass


def after_feature(context, feature):
    # Do the implementations as per your requirements
    pass


def after_all(context):
    # Do the implementations for the total pass/failed count of test cases
    pass
