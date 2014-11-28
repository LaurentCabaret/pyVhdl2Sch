import nose
from vhdl_objects.wire import Wire

def test_wire_classic_downto():
    assert Wire('Name',13,"classic","IN","STD_LOGIC_VECTOR",31,0,True).serialized == "Wire_Name_classic_13_31_0_IN_STD_LOGIC_VECTOR_True"

def test_wire_classic_to():
    assert Wire('Name',13,"classic","IN","STD_LOGIC_VECTOR",31,0,False).serialized == "Wire_Name_classic_13_31_0_IN_STD_LOGIC_VECTOR_False"

def test_wire_clk_to():
    assert Wire('Name',1,"clk","OUT","STD_LOGIC_VECTOR",31,34,False).serialized == "Wire_Name_clk_1_31_34_OUT_STD_LOGIC_VECTOR_False"

def test1():
    assert True
