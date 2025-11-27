import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://DaniFantasy.github.io',
  // base solo se usa en producción (GitHub Pages)
  // En desarrollo local, no uses base para que funcione en localhost
  base: import.meta.env.PROD ? '/Proyecto-ciencia-de-datos' : '/',
  output: 'static'
});

