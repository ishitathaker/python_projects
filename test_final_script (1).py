#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from final_script import custom_sort
import pandas as pd


def test_custom_sort():

    # Create helper data and write tests for the function
    raw_data = {
        "release_year": ["2013", "2003", "2010", "2016", "2015"],
        "total_gross": [1821352070, 1564114393, 1518975880, 2873393105, 2495662696],
        "movie_count": [11, 19, 14, 14, 11],
    }

    helper_df = pd.DataFrame.from_dict(raw_data)

    result = custom_sort(helper_df, "total_gross", 2)

    assert result.shape == (2, 3)
    assert list(res["movie_count"]) == [14, 11]
    assert list(res["total_gross"]) == [2873393105, 2495662696]
