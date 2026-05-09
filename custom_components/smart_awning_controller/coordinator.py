from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class SmartAwningCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, entry):

        super().__init__(
            hass,
            logger=None,
            name="smart_awning",
            update_interval=timedelta(seconds=30),
        )

        self.entry = entry

    async def _async_update_data(self):

        return {
            "safe": True,
            "reason": "ok",
        }