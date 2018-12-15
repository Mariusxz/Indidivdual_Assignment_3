# -*- coding: utf-8 -*-
#%%

#Exercise 1 Stock Handling - Tests

from stock_handling import recalculate_quality, Product
    
def test_recalculate_potato():
    poutine = Product("potato",7)
    recalculate_quality(poutine)
    assert poutine.quality == 6.5
    
def test_recalculate_cheese():
    cheddar = Product("cheese",5)
    recalculate_quality(cheddar)
    assert cheddar.quality == 3
    
def test_recalculate_veggie():
    cucumber = Product("vegetables",1)
    recalculate_quality(cucumber)
    assert cucumber.quality == -2
    
def test_recalculate_meat():
    chicken = Product("meat",1.5)
    recalculate_quality(chicken)
    assert chicken.quality == -1.5
    
def test_recalculate_fish():
    tuna = Product("fish",1.5)
    recalculate_quality(tuna)
    assert tuna.quality == -1.5