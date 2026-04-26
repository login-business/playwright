from utils.ai_helper import generate_test_cases

def test_ai_generation():

    feature = "Login Page"

    result = generate_test_cases(feature)

    print(result)

    assert result is not None