from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(hass, entry, async_add_entities):

    async_add_entities([
        SmartAwningReasonSensor()
    ])


class SmartAwningReasonSensor(SensorEntity):

    _attr_name = "Smart Awning Reason"
    _attr_unique_id = "smart_awning_reason"

    @property
    def native_value(self):
        return "ok"
