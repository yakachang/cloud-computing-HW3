<template>
  <v-row class="ma-15">
    <v-col class="text-center">
      <blockquote class="blockquote text-h4">
        &#8220;Because cloud computing makes like easier&#8221;
        <!-- <footer>
          <small>
            <em class="text-h6">&mdash;Team 123&mdash;</em>
          </small>
        </footer> -->
      </blockquote>
      <img src="/v.png" alt="Vuetify.js" class="ma-15" />
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
}
</script>
