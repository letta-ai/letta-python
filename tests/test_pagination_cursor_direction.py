from letta_client.pagination import _next_cursor_params


def test_next_cursor_params_asc_forward_uses_after() -> None:
    assert _next_cursor_params(params={"order": "asc"}, first_id="id-1", last_id="id-2") == {"after": "id-2"}


def test_next_cursor_params_desc_forward_uses_before() -> None:
    assert _next_cursor_params(params={"order": "desc"}, first_id="id-1", last_id="id-2") == {"before": "id-1"}


def test_next_cursor_params_backward_stays_before_even_with_asc() -> None:
    assert _next_cursor_params(
        params={"order": "asc", "before": "id-0"}, first_id="id-1", last_id="id-2"
    ) == {"before": "id-1"}


def test_next_cursor_params_default_order_assumes_asc() -> None:
    assert _next_cursor_params(params={}, first_id="id-1", last_id="id-2") == {"after": "id-2"}
