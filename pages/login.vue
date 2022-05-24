<template>
  <v-container fluid class="my-10">
    <v-layout justify-center>
      <v-btn
        @click="signInWithGoogle"
        x-large
        tile
      >
        <v-img
          :src="require('~/assets/Google-icon.png')"
          max-height="35"
          max-width="35"
          class="mr-2"
        ></v-img>
        <v-spacer></v-spacer>
        Sign in with Google
      </v-btn>
    </v-layout>
  </v-container>
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