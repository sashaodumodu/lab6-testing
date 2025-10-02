from presidio_anonymizer import sample as sample_mod

def test_sample_run_anonymizer():
    func = getattr(sample_mod, "sample_run_anonymizer", None) or getattr(sample_mod, "run_anonymizer", None) #had to change file
    assert func is not None, "Something went wrong"

    res = func("My name is Bond.", 11, 15)

    assert res.text == "My name is BIP."

    assert len(res.items) == 1
    item = res.items[0]
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
