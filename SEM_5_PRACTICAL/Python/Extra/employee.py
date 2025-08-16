# employee.py

# to calculate dearness allowance
def da(basic):
    """da is 80% of basic salary"""
    da = basic * 80 / 100
    return da

# to calculate house rent allowance
def hra(basic):
    """hra is 15% of basic salary"""
    hra = basic * 15 / 100
    return hra

# to calculate provident fund amount
def pf(basic):
    """pf is 12% of basic salary"""
    pf = basic * 12 / 100
    return pf

# to calculate income tax payable by employee
def itax(gross):
    """tax is calculated at 10% on gross"""
    tax = gross * 0.1
    return tax
