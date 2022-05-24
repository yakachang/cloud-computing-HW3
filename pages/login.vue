<template>
  <v-row>
    <v-col class="text-center">
      <v-btn @click="signInWithGoogle">Sign in with Google</v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'LoginPage',
  methods: {
    async signInWithGoogle() {
      var provider = new this.$fireModule.auth.GoogleAuthProvider();
      
      let authData = await this.$fire.auth.signInWithPopup(provider)
      this.$router.push('/')
    },
  },
}
</script>