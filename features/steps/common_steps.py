from behave import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),r'..\..'))
from features.pages.text_box_page import TextBoxPage


@given(u'that a User is opened text box page')
def step_impl(context):
    context.selenium_driver.get(context.link)
    context.text_box = TextBoxPage(context.selenium_driver)
