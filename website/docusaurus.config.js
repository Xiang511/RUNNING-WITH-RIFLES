// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'RUNNING-WITH-RIFLES',
  tagline: 'An ad-free wiki with a smooth user experience.',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },
  trailingSlash: false,
  // Set the production url of your site here
  url: 'https://xiang511.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/RUNNING-WITH-RIFLES/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Xiang511', // Usually your GitHub org/user name.
  projectName: 'RUNNING-WITH-RIFLES', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  plugins: [
    require.resolve('docusaurus-plugin-image-zoom')
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Xiang511/RUNNING-WITH-RIFLES/tree/main/website/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({

      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'RWR Wiki',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Tutorial',
          },
          {
            type: 'docSidebar',
            sidebarId: 'ResourceSidebar',
            position: 'left',
            label: 'Resources',
          },
           {
            type: 'docSidebar',
            sidebarId: 'OnlineSidebar',
            position: 'left',
            label: 'Onlines',
          },
           {
            type: 'docSidebar',
            sidebarId: 'ModdingSidebar',
            position: 'left',
            label: 'Modding',
          },
          {
            type: 'docSidebar',
            sidebarId: 'showcaseSidebar',
            position: 'left',
            label: 'Showcase',
          },

          { to: '/blog', label: 'Blog', position: 'left' },
          {
            href: 'https://github.com/Xiang511/RUNNING-WITH-RIFLES',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorial',
                to: '/docs/tutorial/intro',
              },
               {
                label: 'Resources',
                to: '/docs/resources/intro',
              },
               {
                label: 'Onlines',
                to: '/docs/onlines/intro',
              },
               {
                label: 'Modding',
                to: '/docs/modding/intro',
              },
              {
                label: 'Showcase',
                to: '/docs/showcase/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Facebook',
                href: 'https://www.facebook.com/RunningWithRifles/',
              },
              {
                label: 'Discord',
                href: 'https://discord.gg/BXeTySyFxA',
              },
              {
                label: 'TikTok',
                href: 'https://www.tiktok.com/@osumiagames',
              },

            ],
          },
          {
            title: 'Friendly links',
            items: [
              {
                label: 'WeaponStats comparison',
                href: 'https://xiang511.com/RWR_WiKi/',
              }
              , {
                label: 'Official Wiki',
                href: 'https://runningwithrifles.fandom.com/wiki/Running_with_Rifles_Wiki',
              },
              {
                label: 'RwRstats',
                href: 'https://rwrstats.com/',
              },

            ],
          },
          {
            title: 'More',
            items: [

              {
                label: 'GitHub',
                href: 'https://github.com/Xiang511/RUNNING-WITH-RIFLES',
              },
              {
                label: 'Blog',
                to: '/blog',
              },

            ],
          },
        ],

        copyright: `Copyright © ${new Date().getFullYear()} Xiang. Built with Docusaurus.`,
      },
      zoom: {
        selector: '.markdown :not(em) > img',
        background: {
          light: 'rgb(255, 255, 255)',
          dark: 'rgb(50, 50, 50)'
        },
        config: {
          // options you can specify via https://github.com/francoischalifour/medium-zoom#usage
        }
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
