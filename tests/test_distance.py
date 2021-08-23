from first_project import distance

def test_haversine():
    assert distance.haversine(0,0,0,0) == 0