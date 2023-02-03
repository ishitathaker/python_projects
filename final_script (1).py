#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def custom_sort(data, sorting_col, N=1):
    import pandas as pd

    """
    Given a dataframe, a sorting column and number of required rows, return a dataframe that has been
    sorted in desending order by the mentioned column and number of required rows.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    sorting_col : str
        The column to sort the data on
    N : int64, optional
        The number of rows required after applying sort. The default is one row.
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe sorted decendingly by column and number of rows specified.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument sorting_col is not in the data columns
    
    Examples
    --------
    >>> custom_sort(release_year_group, 'total_gross', 5)
    release_year	total_gross	movie_count
    53	2016	2873393105	14
    52	2015	2495662696	11
    50	2013	1821352070	11
    40	2003	1564114393	19
    47	2010	1518975880	14
    """

    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # Tests that the the grouping column is in the dataframe
    assert (
        sorting_col in data.columns
    ), "The grouping column does not exist in the dataframe"

    # compute the groupby object
    result = data.sort_values(by=[sorting_col], ascending=False)[:N]
    # return the result
    return result
