/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',   // This will scan your HTML files in 'templates' directory
    './static/js/**/*.js',     // This will scan your JS files in 'static/js' directory
  ],
  theme: {
    extend: {
      colors: {
        uniqueGreen: '#1db954',
        uniqueBlack: '#121212',
        uniqueGrayBlack: '#212121',
        uniqueDarkGray: '#535353',
        uniqueLightGray: '#b3b3b3',
      },
    },
  },
  plugins: [],
}