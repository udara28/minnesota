
from _intf import SDRAM

class Winboad_W9812G6JH_75(SDRAM):
    
    freq = 10e6  # clock frequency in Hz
    timing = { # all timing parameters in ns
        'init' : 200000.0,   # min init interval
        'ras'  : 45.0,       # min interval between active precharge commands
        'rcd'  : 20.0,       # min interval between active R/W commands
        'ref'  : 64000000.0, # max refresh interval
        'rfc'  : 65.0,       # refresh operaiton duration
        'rp'   : 20.0,       # min precharge command duration
        'xsr'  : 75.0,       # exit self-refresh time
    }
    
    addr_width = 12   # SDRAM address width
    data_width = 16   # SDRAM data width
