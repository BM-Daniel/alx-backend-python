#!/usr/bin/env python3

'''
Annotate the functions parameters and return value
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''The function used'''
    return [(i, len(i)) for i in lst]
