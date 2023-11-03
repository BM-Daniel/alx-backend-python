#!/usr/bin/python3

'''
Import async_generator from the previous task and then write a coroutine called
async_comprehension that takes no arguments.
'''

from importlib import import_module
from typing import List


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Corountine function
    '''
    return [number async for number in async_generator()]
