<template>
  <v-row>
    <v-col class="text-center mt-10">
      <v-form @submit.prevent="findAnswer">
        <v-container>
          <v-row>
            <v-col cols="2">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    fab
                    @click="randomQuestion"
                  >
                    <v-icon v-on="on">
                      mdi-chat-question
                    </v-icon>
                  </v-btn>
                </template>
                Random a question
              </v-tooltip>
            </v-col>
            <v-col cols="10">
              <v-text-field
                v-model="question"
                :append-outer-icon="question ? 'mdi-send' : ''"
                clear-icon="mdi-close-circle"
                solo
                clearable
                label="請輸入問題"
                type="text"
                class="text-h5"
                @click:append-outer="findAnswer"
                @click:clear="clearMessage"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <v-spacer />
      <img src="/v.png" alt="Vuetify.js" class="mt-10" />
    </v-col>
    <v-col class="text-center mt-10" cols="12">
      <blockquote class="blockquote text-h4" v-show="answer">
        &#8220;{{ answer }}&#8221;
        <!-- <footer>
          <small>
            <em>&mdash;Helsinki-NLP/opus-mt-zh-en</em>
          </small>
        </footer> -->
      </blockquote>
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
      questionList: [
        '清華大學最初叫什麼？',
        '清大何時成立？',
        '清華大學與哪間學校合併？',
        '清大全名是什麼？',
        '和清華大學合併的學校是？',
        '哪間學校有成功湖？'
      ],
    }
  },
  computed: {
    icon () {
      return this.icons[this.iconIndex]
    },
  },
  methods: {
    async findAnswer() {
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
    randomQuestion() {
      this.question = this.questionList[Math.floor(Math.random() * this.questionList.length)]
      this.findAnswer()
    },
    clearMessage () {
      this.question = ''
    },
  },
}
</script>
