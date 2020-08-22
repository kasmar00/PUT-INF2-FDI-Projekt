from layout import input_cmd

#default values
num_atoms = 20
atom_radius = 1
kappa = 5
size_mul = 80
maxFrames=2000

def get_args():
    """
    Function for getting simulation arguments.
    """
    args=[num_atoms, atom_radius, kappa, size_mul, maxFrames]
    names=["Number of atoms", "Atom Radius", "Kappa", "Size multiplier", "Number of frames"]
    if input_cmd:
        args=get_args_cmd(args, names)
    return args

def get_args_cmd(args, names):
    for i in range(len(args)):
        try:
            args[i]=int(input(names[i]+": "))
        except:
            print("You entered an invalid number, assuming deafult value", args[i])
    return args
