/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',   // This will scan your HTML files in 'templates' directory
    './static/js/**/*.js',     // This will scan your JS files in 'static/js' directory
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}