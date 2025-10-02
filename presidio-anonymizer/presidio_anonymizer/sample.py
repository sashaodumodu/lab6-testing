from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def run_anonymizer(text: str, start: int, end: int, new_value: str = "BIP"):
    
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": new_value})},
    )
    return result


def _print_result_for_cli(result) -> None:
    print(f"text: {result.text}")
    print("items:")
    print("[")
    for item in result.items:
        entry = {
            "start": item.start,
            "end": item.end,
            "entity_type": item.entity_type,
            "text": item.text,
            "operator": item.operator,
        }
        print(f"    {entry}")
    print("]")


if __name__ == "__main__":
    res = run_anonymizer("My name is Bond.", 11, 15, new_value="BIP")
    _print_result_for_cli(res)
