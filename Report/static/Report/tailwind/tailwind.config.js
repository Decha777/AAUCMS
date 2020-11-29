module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
      colors: {
        primary: {
          100: "#2c5282",
          200: "#2a4365",
          300: "#3774be",
        },
        secondary: {
          100: "#dd6b20",
          200: "#c05621",
        },
      },
    },
  },
  variants: {
    backgroundColor: ["responsive", "hover", "focus", "active"],
    fontSize: ["responsive", "hover"],
  },
  plugins: [require("@tailwindcss/custom-forms")],
};