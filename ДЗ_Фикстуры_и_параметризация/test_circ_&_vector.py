import pytest
from circle import Circle
from vector import Vector

#__________________________________________________________________________________________________________________________________
#tests_vector

@pytest.mark.parametrize(
                         'x,y,z,expected',
                         [[1,2,3,True],
                          [1,-1,1,True],
                          [-1,8,1,True],
                          [5,4,-2,True],
                          [0,2,0,True],
                          [3.1234,-1.23455,6.87654,True],
                          [-2.45678,6.89765,-1.453111,True]
                          ]
                         )

def test_correct_date_for_create_vector(x,y,z,expected):
    vec = Vector(x,y,z)
    expected = True
    res = isinstance(vec, Vector)

    assert expected == res, f'Ожидали: {expected}, получили: {res}'


def test_uncorrect_valueerror_date_for_create_vector():
    with pytest.raises(ValueError):
        Vector(0,0,0)

@pytest.mark.parametrize(
    'x,y,z',
    [
     ['1','e','p'],
     ['e','d','балбес'],
     ['0','0',0],
     [1,'0', 2]
    ]
     )
def test_uncorrect_typeeeror_date_for_create_vector(x,y,z):
    with pytest.raises(TypeError): Vector(x,y,z)

@pytest.mark.parametrize(
                         'x,y,z,expected',
                         [[1,2,3,3.74],
                          [4,5,6,8.77]
                          ]
                         )
def test_calculation_len_vector(x,y,z,expected):
    v = Vector(x,y,z)
    result = v.length()
    assert expected == result, f'Ожидали: {expected}, получили: {result}'

@pytest.mark.parametrize(
                         'x,y,z,x1,y1,z1,expected',
                         [[1,2,3,4,5,6,(5.0,7.0,7.0)],
                          [6,5,4,3,2,1,(9.0,7.0,5.0)]
                          ]
                         )
def test_add_vector(x,y,z,x1,y1,z1,expected):
    result = Vector(x,y,z).add(Vector(x1,y1,z1))
    assert expected == expected, f'Ожидали: {expected}, получили: {result}'

@pytest.mark.parametrize(
                         'x,y,z,x1,y1,z1,expected',
                         [[1,2,3,4,5,6,(3.0,3.0,3.0)],
                          [6,5,4,3,2,1,(-3.0,-3.0,-3.0)]
                          ]
                         )
def test_sub_vector(x,y,z,x1,y1,z1,expected):
    result = Vector(x,y,z).sub(Vector(x1,y1,z1))
    assert expected == expected, f'Ожидали: {expected}, получили: {result}'

@pytest.mark.parametrize('x1,y1,z1,x2,y2,z2,expected',
                         [[1,2,3,4,5,6,32.0],
                          [6,5,4,3,2,1,32.0]
                          ])
def test_scalar(x1,y1,z1,x2,y2,z2,expected):
    result = Vector(x1,y1,z1).scalar_mul(Vector(x2,y2,z2))
    assert expected == result, f'Ожидали: {expected}, получили: {result}'

@pytest.mark.parametrize('x1,y1,z1,x2,y2,z2,expected',
                         [[1,2,3,4,5,6,0.22],
                          [6,5,4,3,2,1,0.22],
                          [-1.3,0,4.678,6.555,1,0.345,1.79]
                          ])
def test_angle_betwen_vectors(x1,y1,z1,x2,y2,z2,expected):
    result = Vector(x1, y1, z1).angle_between(Vector(x2, y2, z2))
    assert expected == result, f'Ожидали: {expected}, получили: {result}'

@pytest.mark.parametrize('min_d,max_d,expected',
                         [[1,9,True],
                          [-9,-1,True]
                          ])
def test_random_int_vector(min_d,max_d,expected):
    v = Vector.random_int(min_d,max_d)
    r = sum([isinstance(i, int) for i in [v.get_x(),v.get_y(),v.get_z()]]) == 3
    assert expected == r, f'Ожидали: {expected}, получили: {r}'


def test_random_int_vector_when_uncorret_range():
    with pytest.raises(ValueError):
        Vector.random_int(5,1)

@pytest.mark.parametrize('min_d,max_d,expected',
                         [[1.5,4.5,True],
                          [-3.6789,-1.123,True]
                          ])
def test_random_float_vector(min_d,max_d,expected):
    v = Vector.random_float(min_d,max_d)
    r = sum([isinstance(i, float) for i in [v.get_x(),v.get_y(),v.get_z()]]) == 3
    assert expected == r, f'Ожидали: {expected}, получили: {r}'

def test_random_float_vector_when_uncorret_range():
    with pytest.raises(ValueError):
        Vector.random_float(-1,-15)



#____________________________________________________________________________________________________________________________________
#test_cirle

@pytest.mark.parametrize(
    'r, expected',
    [[5, 5],
     [3.5, 3.5]
     ])
def test_correct_input_data_r(r, expected):
    r = Circle(r).get_r()
    assert Circle(r).get_r() == expected, f'Ожидалось:{expected}, получили:{r}'

@pytest.mark.parametrize(
    'r,new_r, expected',
    [[2,3, 3],
     [1,0.5, 0.5]
     ])
def test_correct_set_input_data_r(r,new_r, expected):
    r = Circle(r)
    r.set_r(new_r)
    assert r.get_r() == expected, f'Ожидалось:{expected}, получили:{r}'

@pytest.mark.parametrize(
    'r',
    [
     [0],
     [-5]
     ])
def test_uncorrect_input_data_r(r):
     with pytest.raises(ValueError): Circle(r)

@pytest.mark.parametrize(
    'r, expected',
    [
     [2, 12.56],
     [5.5, 94.98],
     [6.0, 113.04],
     [5.555555, 96.91]
    ]
    )
def test_calculation_area_circle(r, expected):
    res = Circle(r).area()

    assert expected == res, f'Ожидалось:{expected}, получили:{res}'

@pytest.mark.parametrize(
    'r, expected',
    [
     [4, 25.12],
     [5.5, 34.54],
     [0.23456789, 1.47]
    ]
    )

def test_calculation_circumference_circle(r, expected):
    res = Circle(r).circumference()

    assert expected == res, f'Ожидалось:{expected}, получили:{res}'

@pytest.mark.parametrize(
    'r, expected',
    [
     [3,6],
     [5.0, 10.0],
     [5.5,11.0]
    ]
    )

def test_calculation_diameter_circle(r, expected):
    res = Circle(r).diameter()

    assert expected == res, f'Ожидалось:{expected}, получили:{res}'

