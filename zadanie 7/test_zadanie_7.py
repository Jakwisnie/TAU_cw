import pytest



  dzielenie = [
    (15, 3, 5),
    (20, 5, 4)
 ]

 @pytest.mark.parametrize("a,b,expected", dzielenie)
 def test_dzielenie_v0(a, b, expected):
       diff = a / b
       assert diff == expected
