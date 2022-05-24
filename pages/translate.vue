<template>
  <v-row>
    <v-col class="text-center mt-10">
      <v-form @submit.prevent="translate">
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="message"
                :append-outer-icon="message ? 'mdi-send' : ''"
                prepend-icon="mdi-translate"
                clear-icon="mdi-close-circle"
                solo
                clearable
                label="請輸入中文"
                type="text"
                @click:append-outer="translate"
                @click:clear="clearMessage"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <blockquote class="blockquote" v-show="translatedText">
                &#8220;{{ translatedText }}&#8221;
                <footer>
                  <small>
                    <em>&mdash;Helsinki-NLP/opus-mt-zh-en</em>
                  </small>
                </footer>
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
  name: 'TranslatePage',
  middleware: 'auth',
  data() {
    return {
      translatedText: '',
    }
  },
  computed: {
    icon () {
      return this.icons[this.iconIndex]
    },
  },
  methods: {
    async translate() {
      const response = await this.$axios.$get(`/translate/${this.message}`)
      this.translatedText = response["text"]
    },
    clearMessage () {
      this.message = ''
    },
  },
}
</script>
