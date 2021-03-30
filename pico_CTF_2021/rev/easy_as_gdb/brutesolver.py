import angr
import claripy


char_length = 30

success = 0x00010a72
fail = 0x00010a86
base_addr = 0x00010000

project = angr.Project('./brute_zdt', main_opts={"base_addr": base_addr})

input_chars = [claripy.BVS("char_{}".format(i), 8) for i in range(char_length)]

flag = claripy.Concat(*input_chars + [claripy.BVV(b'\n')])

state = project.factory.full_init_state(
    args=['./brute_zdt'],
    add_options=angr.options.unicorn,
    stdin=flag,
)


for k in input_chars:
    state.solver.add(k >= ord('!'))
    state.solver.add(k <= ord('~'))

sim_manager = project.factory.simulation_manager(state)

sim_manager.explore(find=success, avoid=fail)

if len(sim_manager.found) > 0:
    for found in sim_manager.found:
        print(found.posix.dumps(0))
