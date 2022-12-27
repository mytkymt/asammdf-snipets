import re

import asammdf

def display_signal_info(mdf_data:asammdf.MDF, regex_filter_name:str, ):
    for channel_name, (group_name, ids) in zip(mdf_data.channels_db.keys(), mdf_data.channels_db.items()):
        (group_id, channel_id) = ids[0]
        print(channel_name, group_name, group_id, channel_id)
