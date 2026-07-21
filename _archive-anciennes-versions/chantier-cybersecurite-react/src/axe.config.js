// axe.config.js
module.exports = {
  rules: {
    'color-contrast': { enabled: true },
    'aria-valid': { enabled: true },
    'label': { enabled: true }
  },
  runOnly: {
    type: 'tag',
    values: ['wcag2a', 'wcag2aa']
  }
};