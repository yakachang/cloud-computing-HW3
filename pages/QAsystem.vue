<template>
  <v-row>
    <v-col class="text-center mt-10">
      <v-form @submit.prevent="translate">
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="question"
                :append-outer-icon="question ? 'mdi-send' : ''"
                prepend-icon="mdi-translate"
                clear-icon="mdi-close-circle"
                solo
                clearable
                label="請輸入問題"
                type="text"
                class="text-h5"
                @click:append-outer="translate"
                @click:clear="clearMessage"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <blockquote class="blockquote" v-show="answer">
                &#8220;{{ answer }}&#8221;
                <!-- <footer>
                  <small>
                    <em>&mdash;Helsinki-NLP/opus-mt-zh-en</em>
                  </small>
                </footer> -->
              </blockquote>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <v-spacer />
      <img src="/v.png" alt="Vuetify.js" class="mt-10" />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'QAPage',
  middleware: 'auth',
  data() {
    return {
      answer: '',
      question: '',
    }
  },
  computed: {
    icon () {
      return this.icons[this.iconIndex]
    },
  },
  methods: {
    async translate() {
      const params = {
        question: this.question
      }
      const promise = this.$axios.$get(
        `/inference`, { params }
      ).then(response => {
        this.answer = response["answer"]
      }).catch(error => {
        console.log(error)
      })
      await promise
    },
    clearMessage () {
      this.question = ''
    },
  },
}
</script>
