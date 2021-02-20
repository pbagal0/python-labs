from assignment3 import *
import pytest

def test_func():
    assert ip("231.124.789") == [231,124,789]
    assert ip("256.142.676.359")==[256,142,676,359]

def test1_func():
    assert wave("ltts")==['Ltts','lTts','ltTs','lttS']
    assert wave("ctea")==['Ctea','cTea','ctEa','cteA']

def test2_func():
    assert time("1:71:61")=="2:12:1"
    assert time("8:20:78")=="8:21:18"

def test3_fun():
    assert date("45/8/2018")=="14/9/2018"
    assert date("32/11/2000")=="1/12/2000"

def test4_fun():
    assert isogram("machine")== True
    assert isogram("assert")== False

def test5_fun():
    assert Del_dig("312")==32
    assert Del_dig("146")==46

def test6_fun():
    assert largest_num(123)==321
    assert largest_num(786)==876

def test7_fun():
    assert accum("abcd")=='A-Bb-Ccc-Dddd'
    assert accum("term")=='T-Ee-Rrr-Mmmm'

def test8_fun():
    assert rgb_to_hex((255,0,255))=='ff00ff'

