
import os
import angr
import logging
import subprocess
import claripy


self_dir = os.path.dirname(os.path.realpath(__file__))

flag_length = 32
flag_chars = [claripy.BVS(f"flag_chars{i}",8) for i in range(flag_length)]
flad = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')])


def test_java_crackme1():
    binary_path = os.path.join(self_dir, "VaultDoor1.jar")
    project = angr.Project(binary_path)
    state = project.factory.entry_state()
    simgr = project.factory.simulation_manager(state)
    simgr.expore()

    if(len(simgr.found)>0):
        for found in simgr.found:
            print(found.posix.dumps(0))
    

def test():
    test_java_crackme1()


if __name__ == "__main__":
    logging.getLogger("angr.engines.soot.engine").setLevel("DEBUG")
    logging.getLogger("angr.factory").setLevel("DEBUG")
    test()
