from homeassistant.components.binary_sensor import BinarySensorEntity


async def async_setup_entry(hass, entry, async_add_entities):

    async_add_entities([
        SmartAwningSafeBinarySensor()
    ])


class SmartAwningSafeBinarySensor(BinarySensorEntity):

    _attr_name = "Smart Awning Safe"
    _attr_unique_id = "smart_awning_safe"

    @property
    def is_on(self):
        return True
