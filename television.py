class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default power off, muted off, channel set to MIN_CHANNEL,
        and volume set to MIN_VOLUME.
        :return: None
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Turns the television power on or off.
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute state of the television. Muting stores the current volume and sets it to 0.
        Unmuting restores the stored volume.

        :return: None
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = 0
            else:
                self.__volume = self.__prev_volume
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel by one. Wraps to MIN_CHANNEL if at MAX_CHANNEL.
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by one. Wraps to MAX_CHANNEL if at MIN_CHANNEL.
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by one unit up to MAX_VOLUME.
        If muted, unmutes the TV and restores the previous volume before increasing.

        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__prev_volume = self.__volume

    def volume_down(self) -> None:
        """
        Decreases the volume by one unit down to MIN_VOLUME.
        If muted, unmutes the TV and restores the previous volume before decreasing.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__prev_volume = self.__volume

    def __str__(self) -> str:
        """
        Returns a string statement of the current state of the television,
        including power status, channel, and volume.
        :return: A string stating the TV's power, channel, and volume.
        :rtype: str
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
