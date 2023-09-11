# run a python script from a string
# input is a string containing the python script
# output is a string containing the output of the script

import sys
import io
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def run_python_script_from_string(input):
    with stdoutIO() as s:
        exec(input)
    return s.getvalue()

if __name__ == "__main__":
    input = """
bell_circuit = '''
version 1.0

qubits 2


.init
  prep_z q[0]
  prep_z q[1]

.entangle
  h q[0]
  cnot q[0],q[1]

.measurement
  measure q[0]
  measure q[1]
'''
print(bell_circuit)
"""
    print(run_python_script_from_string(input))
