def set_page_bar_range(page_object, bar_range):
    start_num_page_bar = page_object.number - (page_object.number-1) % 5
    end_num_page_bar = start_num_page_bar + bar_range - 1
    return range(start_num_page_bar, end_num_page_bar + 1)