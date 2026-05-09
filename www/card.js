// card.js
class AwningStatusCard extends HTMLElement {
  set hass(hass) {
    const card = document.createElement('ha-card');
    card.header = "Stato della Tenda";

    const div = document.createElement('div');
    div.style.padding = '10px';

    const conditions = [
      {
        label: 'Vento',
        state: hass.states['weather.forecast_home'].attributes.wind_speed,
        threshold: 10,
        color: 'green'
      },
      {
        label: 'Nuvolosità',
        state: hass.states['weather.forecast_home'].attributes.cloud_coverage,
        threshold: 44,
        color: 'green'
      },
      {
        label: 'Persone in casa',
        state: hass.states['zone.home'].state,
        threshold: 1,
        color: 'green'
      }
    ];

    conditions.forEach(condition => {
      const conditionDiv = document.createElement('div');
      conditionDiv.innerHTML = `
        <strong>${condition.label}:</strong> ${condition.state}
        <span style="color: ${condition.state > condition.threshold ? 'green' : 'red'};">${condition.state > condition.threshold ? 'OK' : 'NO'}</span>
      `;
      div.appendChild(conditionDiv);
    });

    card.appendChild(div);
    this.shadowRoot.appendChild(card);
  }

  setConfig(config) {
    this.config = config;
  }

  getCardSize() {
    return 1;
  }
}

customElements.define('awning-status-card', AwningStatusCard);