from homeassistant.components.switch import SwitchEntity


async def async_setup_entry(hass, entry, async_add_entities):

    async_add_entities([
        SmartAwningAutomationSwitch()
    ])


class SmartAwningAutomationSwitch(SwitchEntity):

    _attr_name = "Smart Awning Automation"
    _attr_unique_id = "smart_awning_automation"

    def __init__(self):
        self._state = True

    @property
    def is_on(self):
        return self._state

    async def async_turn_on(self, **kwargs):
        self._state = True

    async def async_turn_off(self, **kwargs):
        self._state = False
