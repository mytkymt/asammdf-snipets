import asammdf


def get_single_signal(mdf_data: asammdf.MDF, channel_name: str) -> asammdf.Signal:
    """
    Extract a single signal from a mdf data
    
    Parameters:
    - mdf_data (asammdf.MDF): A measurement data 
    - channel_name (str): A channel name to extract
    
    Returns:
    - asammdf.Signal: The extracted signal
    """

    signal = mdf_data.get(channel_name)

    return signal

def get_multiple_signals(mdf_data: asammdf.MDF, channel_names: list, filter_path:str=None) -> list:
    """
    Extract multiple signal from a mdf data
    
    Parameters:
    - mdf_data (asammdf.MDF): A measurement data 
    - channel_names (list): Channel names to extract
    - filter_path (str): A path name to filter
    
    Returns:
    - asammdf.Signal: The extracted signal
    """

    found_signals = mdf_data.select(channels=channel_names)

    out_signals = []
    if filter_path:
        for signal in found_signals:
            if signal.source.path == filter_path:
                out_signals.append(signal)

    else:
        out_signals = found_signals

    return out_signals


if __name__ == '__main__':
    import numpy as np
    import display_signal_info

    # create asammdf.Signal
    cycles = 100
    step = 0.01
    time_stamps = np.arange(0, cycles, step, dtype=np.float64)
    samples = np.cos(time_stamps)
    source = asammdf.Source(name='source', path='path', comment='comment', source_type=4, bus_type=0)
    signal = asammdf.Signal(
        samples=samples,
        timestamps=time_stamps,
        source=source,
        name='Cos',
        unit=''
    )

    # create asammdf.MDF object
    mdf = asammdf.MDF(version='4.10')
    mdf.append(signal)

    display_signal_info.display_signal_info(mdf, None)
    # signals = get_multiple_signals(mdf, ['Cos'])
    # 
    # from matplotlib import pyplot as plt
    # print(signals[0].source.path)
    # plt.plot(signals[0].timestamps, signals[0].samples)
    # plt.show()