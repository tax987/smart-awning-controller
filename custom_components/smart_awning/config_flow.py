import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import selector

from .const import (
    DOMAIN,
    CONF_COVER,
    CONF_WIND_SENSOR,
    CONF_RAIN_SENSOR,
)


class SmartAwningConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(
                title="Smart Awning",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_COVER): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="cover"
                    )
                ),

                vol.Required(CONF_WIND_SENSOR): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="sensor"
                    )
                ),

                vol.Optional(CONF_RAIN_SENSOR): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="binary_sensor"
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
