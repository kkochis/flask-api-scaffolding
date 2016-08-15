# -*- coding: utf-8 -*-
from ....services import families


def test_get_all():
    actual = families.get_all()
    assert actual == ["ACANTHACEAE", "ACHARIACEAE"]
