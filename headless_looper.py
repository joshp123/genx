import time
from my_headless_genx import *

# Mutation schemes implemented
#self.mutation_schemes = [self.best_1_bin, self.rand_1_bin,\
#    self.best_either_or, self.rand_either_or, self.jade_best, self.simplex_best_1_bin]

for x in xrange(0,10):
    genx = GenX()
    genx.optimize()
    with open('looperlog.txt', 'a') as log:
        log.write('run' + repr(time.clock())) # also log method and frequency and paramters idk





