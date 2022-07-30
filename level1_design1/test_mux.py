# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    s = 0b01101
    i = 0b01

    dut.sel.value = s
    dut.inp13.value = i

    await Timer(2, units='ns')

    assert dut.out.value == 0b01, f"mux result is incorrect: {dut.X.value} != 0b01"
        

@cocotb.test()
async def test_mux12(dut):
    """Test for mux2"""
    s = 0b11110
    i = 0b10

    dut.sel.value = s
    dut.inp30.value = i

    await Timer(2, units='ns')

    assert dut.out.value == 0b10, f"mux result is incorrect: {dut.X.value} != 0b10"

@cocotb.test()
async def test_mux123(dut):
    """Test for mux2"""
    s = 0b10011
    i = 0b10

    dut.sel.value = s
    dut.inp19.value = i

    await Timer(2, units='ns')

    assert dut.out.value == 0b10, f"mux result is incorrect: {dut.X.value} != 0b10"

    
