FILE_TO_RUN="two_tof_single_bus.py"
#FILE_TO_RUN="tof_test.py"
#FILE_TO_RUN="two_tof_multi_bus.py"
echo "Running ${FILE_TO_RUN}"
rshell 'cp *.py /pyboard'
#rshell 'repl ~ import sys ~'
#rshell 'repl ~ sys.exit() ~'
rshell 'repl ~ import' "${FILE_TO_RUN%.*}"

