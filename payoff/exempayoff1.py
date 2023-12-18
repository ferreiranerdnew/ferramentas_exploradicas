# pip install opstrat

import opstrat as op

# op.single_plotter()


# op.single_plotter(spot=460, strike=460, op_type='p', tr_type='s', op_pr=12.5)

# op.multi_plotter()

# exemplo com petr4

op1={'op_type': 'c', 'strike': 36.77, 'tr_type': 's', 'op_pr': 0.76}
op2={'op_type': 'c', 'strike': 37.27, 'tr_type': 'b', 'op_pr': 0.60}
op3={'op_type': 'p', 'strike': 34.52, 'tr_type': 's', 'op_pr': 0.51}
op4={'op_type': 'p', 'strike': 34.02, 'tr_type': 'b', 'op_pr': 0.41}

op_list=[op1, op2, op3, op4]
op.multi_plotter(spot=36.08,spot_range=10, op_list=op_list)

