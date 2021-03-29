import angr
import claripy


char_length = 32

success = 0x00010a72
fail = 0x00010a86
base_addr = 0x00010000

project = angr.Project('./brute', main_opts={"base_addr": base_addr})

input_chars = [claripy.BVS("char_{}".format(i), 8) for i in range(char_length)]

flag = claripy.Concat(*input_chars + [claripy.BVV(b'\n')])

state = project.factory.full_init_state(
    args=['./brute'],
    add_options=angr.options.unicorn,
    stdin=flag
)

sim_manager = project.factory.simulation_manager(state)

sim_manager.explore(find=success, avoid=fail)

if len(sim_manager.found) > 0:
    for found in sim_manager.found:
        print(found.posix.dumps(0))
