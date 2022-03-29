import logging
from typing import Union, List
from decimal import Decimal, DecimalException
from django.db.models import QuerySet
from file_controls.models import Campaign, AdGroup, SearchTerm

logger = logging.getLogger('django')


def campaign_calculation(campaign_qs: Union[QuerySet, List[Campaign]], search_term_qs: Union[QuerySet,
                                                                                             List[SearchTerm]]) -> list:
    """
    Get queryset of Campaign and SearchTerm, calculate and sort depend on ROAS and return first 10
    Args:
        campaign_qs: Campaign Queryset
        search_term_qs: SearchTerm Querysey

    Returns:
        calc_result: First 10 search term depend on Campaign structure value sort by ROAS

    """
    calc_result = []
    exclude_list = set()
    for item in campaign_qs:
        if item.structure_value in exclude_list:
            continue
        search_result = search_term_qs.filter(campaign__structure_value=item.structure_value)
        exclude_list.add(item.structure_value)
        search_term_list, total_cost, total_conversion_value = calculation(search_result)
        try:
            calc_result.append([item.structure_value,
                                " ".join(search_term_list),
                                round(total_cost, 2),
                                round(total_conversion_value, 2),
                                int(round((total_conversion_value / total_cost), 0))
                                ])
        except DecimalException as e:
            logger.warning(f'{str(e)} for Campaign structure value {item.structure_value}')

    calc_result = sorted(calc_result, key=lambda sort_column: sort_column[4], reverse=True)
    return calc_result[:10]


def ad_group_calculation(ad_group_qs: Union[QuerySet, List[AdGroup]], search_term_qs: Union[QuerySet,
                                                                                            List[SearchTerm]]) -> list:
    """
    Get queryset of AdGroup and SearchTerm, calculate and sort depend on ROAS and return first 10
    Args:
        ad_group_qs: AdGroup Queryset
        search_term_qs: SearchTerm Queryset
    Returns:
        calc_result: First 10 search term depend on AdGroup alias sort by ROAS
    """
    calc_result = []
    exclude_list = set()
    for item in ad_group_qs:
        if item.alias in exclude_list:
            continue
        search_result = search_term_qs.filter(ad_group__alias=item.alias)
        exclude_list.add(item.alias)
        search_term_list, total_cost, total_conversion_value = calculation(search_result)
        try:
            calc_result.append([item.alias,
                                " ".join(search_term_list),
                                round(total_cost, 2),
                                round(total_conversion_value, 2),
                                round((total_conversion_value / total_cost), 1)
                                ])
        except DecimalException as e:
            logger.warning('{} for AdGroup alias {}'.format(str(e), item.alias))

    calc_result = sorted(calc_result, key=lambda sort_column: sort_column[4], reverse=True)
    return calc_result[:10]


def calculation(search_result):
    """
    Calculate total cost, total conversion_value and set of search term
    Args:
        search_result: Queryset of SearchTerm
    Returns:
        search_term_list: search term list as a set
        total_cost: total cost of costs
        total_conversion_value: total conversion value of conversion values
    """
    search_term_list = set()
    total_cost = Decimal(0.00)
    total_conversion_value = Decimal(0.00)
    for i in search_result:
        total_cost += i.cost
        total_conversion_value += i.conversion_value
        search_term_list.update(set(i.search_term.split(" ")))

    return search_term_list, total_cost, total_conversion_value
