class Room:
    def __init__(self, name, rn, rw, re, rs, closedDoors, interactions, n_info=None, w_info=None, s_info=None, e_info=None):
        self.name = name
        self.dn = True if rn != None else False
        self.dw = True if rw != None else False
        self.de = True if re != None else False
        self.ds = True if rs != None else False
        self.rn = rn
        self.rw = rw
        self.re = re
        self.rs = rs
        self.interactions = interactions    # [[Object], [...], ...]
        self.closedDoors = closedDoors      # [[Door, Key_to_open], [..., ...], ...]
        self.n_information = n_info
        self.w_information = w_info
        self.s_information = s_info
        self.e_information = e_info