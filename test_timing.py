import timing as timing_framework

def test_timing_result():
    timing_result = timing_framework.return_function_runtime(required_array_length = 5)
    assert type(timing_result) is float