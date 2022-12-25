import asammdf
import get_signals

def save_shrinked_mf4(original_path: str, shrinked_path: str, channels: list[str], filter_path: str=None) -> None:
    mdf = asammdf.MDF(channels=channels)

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