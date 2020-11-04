from behave import *


@given(u'open a browser')
def step_impl(context):
    print('browser opened')
