folders = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]
access = {'G'}

def build_access_map(folders):
    access_map = {}
    for child, parent in folders:
        if child not in access_map:
            access_map[child] = parent



def has_access(folder):
