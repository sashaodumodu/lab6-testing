from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    assert res.text == "My name is BIP."
    assert len(res.items) == 1

    item = res.items[0]
    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
