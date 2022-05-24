<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center">
        <NuxtLogo />
        <VuetifyLogo />
      </v-card>
      <v-card>
        <v-card-title class="headline">
          Welcome to the Vuetify + Nuxt.js template
        </v-card-title>
        <v-card-text>
          This is the content of card
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn @click="logout">Logout</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
  middleware: 'auth',
  mounted() {
    if (!this.isAuthenticated) {
      this.$router.replace("/login/")
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.authUser
    },
  },
  methods: {
    async logout() {
      await this.$fire.auth.signOut()
      this.$router.replace('/login')
    }
  }
}
</script>
