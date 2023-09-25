/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    container: {
      center: true,
      padding: '3rem',
    },
    extend: {
      boxShadow: {
        'dashboard': 'inset 0 1px 0 0 #ffffff1a',
        'light': 'inset 0 1px 0 0 #fff3'
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
]
}

