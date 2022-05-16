from behave import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), r'..\..'))
import time


@when(u'a user inputs full name')
def step_impl(context):
    context.text_box.input_full_name('John Doe')


@when(u'a user inputs valid email')
def step_impl(context):
    context.text_box.input_email('test@test.tes')


@when(u'a user inputs current address')
def step_impl(context):
    context.text_box.input_current_address('Test 123')


@when(u'a user inputs permanent address')
def step_impl(context):
    context.text_box.input_permanent_address('Test 123')


@when(u'a user clicks on the submit button')
def step_impl(context):
    context.text_box.click_on_submit_btn()


@then(u'an entry will be added')
def step_impl(context):
    assert 'John Doe' in context.text_box.return_current_name()
    assert 'test@test.tes' in context.text_box.return_current_email()


@then(u'an entry will be added without name value')
def step_impl(context):
    assert 'test@test.tes' in context.text_box.return_current_email()
    assert not context.text_box.check_if_name_is_shown()


@then(u'an entry will be added without an email value')
def step_impl(context):
    assert 'John Doe' in context.text_box.return_current_name()
    assert not context.text_box.check_if_email_is_shown()


@when(u'a user inputs new full name value')
def step_impl(context):
    context.text_box.input_full_name('new John Doe')


@then(u'the new added value is shown')
def step_impl(context):
    assert 'new John Doe' in context.text_box.return_current_name()
