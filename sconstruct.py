#env = Environment(CC = '/usr/local/bin/gcc9' , CCFLAGS = '-Wall -pedantic -O2')
env = Environment()
env['CC']  = '/usr/local/bin/gcc9'
env['CCFLAGS'] = '-Wall -pedantic -O2'

srcs = Split('cfg_to_gdbm.c utils.c')
env.Program(target = 'cfg_to_gdbm',source = srcs)




