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
          100: "#F0F0F0",
          200: "#F8F8F8",
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