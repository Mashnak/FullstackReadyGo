def uncheck_others(current_var, variables):
    for var in variables:
        if var is not current_var:
            var.set(0)
