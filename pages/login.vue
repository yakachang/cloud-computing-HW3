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
  computed: {
    isAuthenticated() {
      return this.$store.state.authUser
    },
    userIdToken() {
      return this.$store.state.authUser.uid
    }
  },
  watch: {
    async isAuthenticated(value) {
      if (value) {
        await this.$fire.firestore.collection('user').doc(this.userIdToken).get().then(doc => {
          if (!doc.exists) {
            this.$fire.firestore.collection('user').doc(this.userIdToken).set({
              A1: 0,
              A2: 0,
              B1: 0,
              B2: 0,
              C1: 0,
              C2: 0
            }).then(() => {
              console.log('Create user data successful')
            }).catch(error => {
              console.log(error)
            })
          }
        })
        this.$router.push("/")
      }
    },
  },
  methods: {
    async signInWithGoogle() {
      let provider = new this.$fireModule.auth.GoogleAuthProvider()
      let authData = await this.$fire.auth.signInWithPopup(provider)
      this.$nuxt.refresh()
      this.$router.push('/')
    },
  },
}
</script>