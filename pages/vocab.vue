<template>
  <v-row class="mt-10">
    <v-col cols="4">
      <v-list shaped>
        <v-subheader class="text-h5 my-5">CEFR level</v-subheader>
        <v-list-item-group
          v-model="selectedLevel"
          color="primary"
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title
                v-text="item.text"
                class="text-h6"
              ></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-col>
    <v-col cols="8">
      <v-card
        class="mx-auto"
      >
        <v-system-bar
          color="pink darken-2"
          dark
        >
          <v-spacer></v-spacer>
          <v-icon>mdi-window-minimize</v-icon>
          <v-icon>mdi-window-maximize</v-icon>
          <v-icon>mdi-close</v-icon>
        </v-system-bar>

        <v-app-bar
          dark
          color="pink"
        >
          <v-toolbar-title>Vocabularies</v-toolbar-title>
        </v-app-bar>

        <v-container>
          <v-row class="justify-center">
            <v-col cols="12">
              <v-card
                class="ma-5"
              >
                <v-card-title class="text-h4">{{ vocabs[0]['headword'] }}</v-card-title>
                <v-card-text>
                  <div class="text-subtitle-1">
                    <p>({{ vocabs[0]['pos'] }}.)</p>
                    <p>Definition: {{ vocabs[0]['en_def'] }}</p>
                    <p>中文定義： {{ vocabs[0]['ch_def'] }}</p>
                    <p>Example: {{ vocabs[0]['en_example'] }}</p>
                    <p>中文翻譯： {{ vocabs[0]['ch_example'] }}</p>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions class="justify-end">
          <v-btn text>
            Next Card
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'VocabPage',
  async asyncData({store, $fire}) {
    const userIdToken = store.state.authUser.uid
    console.log(userIdToken)
    
    let startIdxMapper = {}
    let startIdx = 0
    const startIdxPromise = $fire.firestore.collection('user').doc(userIdToken).get().then(doc => {
      startIdxMapper = doc.data()
      console.log(startIdxMapper)
      startIdx = startIdxMapper['A1']
    })

    let vocabs = {}
    const vocabsPromise = $fire.firestore.collection('A1').get().then(querySnapshot => {
      querySnapshot.forEach(doc => {
        vocabs[doc.id] = doc.data()
      })
    })

    await Promise.all([startIdxPromise, vocabsPromise])

    return {
      userIdToken,
      startIdxMapper,
      startIdx,
      vocabs
    }
  },
  data() {
    return {
      selectedLevel: 0,
      levelMapper: {
        0: 'A1',
        1: 'A2',
        2: 'B1',
        3: 'B2',
        4: 'C1',
        5: 'C2'
      },
      items: [
        { text: 'A1', icon: 'mdi-flag' },
        { text: 'A2', icon: 'mdi-flag' },
        { text: 'B1', icon: 'mdi-flag' },
        { text: 'B2', icon: 'mdi-flag' },
        { text: 'C1', icon: 'mdi-flag' },
        { text: 'C2', icon: 'mdi-flag' },
      ],
    }
  },
  computed: {
  },
  watch: {
    'selectedLevel'() {
      const level = this.levelMapper[this.selectedLevel]
      const startIdx = this.startIdxMapper[level]
      console.log(startIdx)
    }
  },
}
</script>
