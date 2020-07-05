class Settings:

    def __init__(setting, autoPlay=True, soundEffects=True):
        setting.autoPlay = autoPlay
        setting.soundEffects = soundEffects

    def showSettings(setting):
        settings = [setting.autoPlay, setting.soundEffects]
        return settings
