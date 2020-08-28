from layout import input_cmd

#default values
num_atoms = 20
atom_radius = 1
kappa = 5
size_mul = 80
maxFrames=2000

arg_names=["Number of atoms", "Atom Radius", "Kappa", "Size multiplier", "Number of frames"]
args=[num_atoms, atom_radius, kappa, size_mul, maxFrames]

def get_args(): #Function for getting simulation arguments.
    if input_cmd:
        args_ret=get_args_cmd(arg_names)
    return args_ret

def get_args_cmd(names):
    for i in range(len(args)):
        try:
            args[i]=int(input(arg_names[i]+": "))
        except:
            print("Input not recognized or skipped, assuming deafult value", args[i])
    return args