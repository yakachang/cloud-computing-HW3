<template>
  <v-app>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-btn icon @click.stop="fixed = !fixed" small>
        <v-icon right>mdi-cloud</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <div class="flex-1-1-auto d-flex align-center justify-end">
        <v-btn
          v-for="(item, i) in items"
          :to="item.to"
          :key="i"
          class="text-capitalize text-subtitle-1"
          text
          nuxt
        >
          {{ item.title }}
        </v-btn>
        <v-btn
          text
          class="text-capitalize text-subtitle-1"
          @click="logout"
        >
          Logout
        </v-btn>
      </div>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      title: 'Cloud Computing',
      clipped: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-account-group',
          title: 'Home',
          to: '/',
        },
        {
          icon: 'mdi-file',
          title: 'Vocab',
          to: '/vocab/',
        },
        {
          icon: 'mdi-file',
          title: 'Q&A System',
          to: '/QAsystem/',
        },
      ]
    }
  },
  methods: {
    async logout() {
      await this.$fire.auth.signOut()
      this.$router.replace('/login')
    }
  }
}
</script>
