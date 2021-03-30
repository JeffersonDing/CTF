import angr
import claripy


char_length = 41

success = 0x00139d78
fail = 0x00139dc8
base_addr = 0x00100000

project = angr.Project('./checkpass', main_opts={"base_addr": base_addr})

input_chars = [claripy.BVS("char_{}".format(i), 8) for i in range(char_length)]

flag = claripy.Concat(*input_chars)

state = project.factory.full_init_state(
    args=['./checkpass', flag],
    add_options=angr.options.unicorn
)

sim_manager = project.factory.simulation_manager(state)

sim_manager.explore(find=success, avoid=fail)

if len(sim_manager.found) > 0:
    for found in sim_manager.found:
        print(found)
