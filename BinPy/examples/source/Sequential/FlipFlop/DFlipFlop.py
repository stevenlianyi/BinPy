# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example for DFlipFlop

# <codecell>

from __future__ import print_function
from BinPy.Sequential.sequential import DFlipFlop
from BinPy.tools.clock import Clock
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

# <codecell>

data = Connector(1)

p = Connector(0)
q = Connector(1)

# <codecell>

# Initialize the clock
clock = Clock(1, 5)
clock.start()
# A clock of 10 hertz frequency
clk_conn = clock.A

enable = Connector(1)

# <codecell>

# Initialize the D-FlipFlop
dff = DFlipFlop(data, enable, clk_conn, a=p, b=q)
# To connect different set of connectors use :
# dff.setInputs(conn1,enab,clk)
# To connect different outputs use s.setOutputs(op1,op2)
dff.setOutputs(A=p, B=q)

# <codecell>

# Initiating the oscilloscope
o = Oscilloscope((clk_conn, 'CLK'), (data, 'DATA'), (
    p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
o.start()
o.setScale(0.01)  # Set scale by trial and error.
o.setWidth(100)
o.unhold()

# <codecell>

print ("Data is 1")
data.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())

# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break

# <codecell>

print ("Data is 0")
data.state = 0
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())
# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break

# <codecell>

print ("Data is 1")
data.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        dff.trigger()
        break
print (dff.state())
# Sending a positive edge to dff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        dff.trigger()
        break

# <codecell>

# Display the oscilloscope
o.display()

# <codecell>

# Kill the oscilloscope and clock threads after usage
o.kill()
clock.kill()
