import pdb
import os
import sys


def set_trace():
    frame = sys._getframe().f_back  # pop the current stackframe off
    pdb.set_trace(frame=frame, Pdb=ForkablePdb)


class ForkablePdb(pdb.Pdb):
    """Pdb that works from a multiprocessing child"""

    def interaction(self, *args, **kwargs):
        original_stdin = sys.stdin
        try:
            sys.stdin = os.fdopen(0)  # 0 should be stdin's file descriptor
            pdb.Pdb.interaction(self, *args, **kwargs)
        finally:
            sys.stdin = original_stdin
            
# set_trace()
