import pdb
from task4_mod1_hw import Actions

def test_multiply():
    # pdb.set_trace()
    action1 = Actions()
    action1.multiply(10, 3)
    assert action1.result == 30, 'Успешное умножение'
    
def test_divide():
    # pdb.set_trace()
    action2 = Actions()
    action2.divide(9, 3)
    assert action2.result == 3, 'Успешное деление'
    action2.divide(9, 0)
    assert action2.result == 1, 'Деление на 0 - ошибка!!!'


if __name__ == '__main__':
    pdb.set_trace()
    test_multiply()
    test_divide()
