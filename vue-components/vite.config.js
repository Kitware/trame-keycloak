import { defineConfig } from "vite";

export default defineConfig({
  base: "./",
  build: {
    lib: {
      entry: "./src/main.js",
      name: "trame_keycloak",
      formats: ["umd"],
      fileName: "trame-keycloak",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../trame_keycloak/module/serve",
    assetsDir: ".",
  },
});
