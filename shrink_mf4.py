import asammdf
import get_signals

def save_shrinked_mf4(original_path: str, shrinked_path: str, channels: list[str], filter_path: str=None) -> None:
    """
    Shrink the input mf4 by filtering 'channels' and 'filter_path'
    
    Parameters:
    - original_paht (str): Measurement data path 
    - shrinked_path (str): Output data path
    - channel_names (list): Channel names to extract
    - filter_path (str): Path name to filter
    
    Returns:
    - asammdf.Signal: The extracted signal
    """
    
    mdf = asammdf.MDF(original_path, channels=channels)

    if filter_path:
        filtered_channels = []
        # Iter over all channels
        for group_id, channel_id in mdf.channels_db().items():
            signal = mdf.select((None, group_id, channel_id))
            if signal.source.path == filter_path:
                filtered_channels.append((None, group_id, channel_id))
        # update mdf object
        mdf = mdf.filter(filtered_channels)
    
    mdf.save(shrinked_path)

def get_shrinked_mf4(original_path: str, shrinked_path: str, channels: list[str], filter_path: str=None) -> None:
    """
    Shrink the input mf4 by filtering 'channels' and 'filter_path'
    
    Parameters:
    - original_paht (str): Measurement data path 
    - shrinked_path (str): Output data path
    - channel_names (list): Channel names to extract
    - filter_path (str): Path name to filter
    
    Returns:
    - asammdf.Signal: The extracted signal
    """
    
    mdf = asammdf.MDF(original_path, channels=channels)

    if filter_path:
        filtered_channels = []
        # Iter over all channels
        for group_id, channel_id in mdf.channels_db().items():
            signal = mdf.select((None, group_id, channel_id))
            if signal.source.path == filter_path:
                filtered_channels.append((None, group_id, channel_id))
        # update mdf object
        mdf = mdf.filter(filtered_channels)
    
    return mdf