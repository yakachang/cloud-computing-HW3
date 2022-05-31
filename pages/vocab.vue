<template>
  <v-row class="mt-10">
    <v-col cols="4">
      <v-list shaped>
        <v-subheader class="text-h5 my-5">CEFR level</v-subheader>
        <v-list-item-group
          v-model="selectedItem"
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
                <v-card-title class="text-h4">apple</v-card-title>
                <v-card-text>
                  <div class="text-h6">
                    <p>(noun.)</p>
                    <p>Definition: a round fruit with firm, white flesh and a green or red skin</p>
                    <p>中文定義： 蘋果</p>
                    <p>Example: to peel an apple</p>
                    <p>中文翻譯： 削蘋果</p>
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
  data() {
    return {
      selectedItem: 1,
      items: [
        { text: 'A1', icon: 'mdi-flag' },
        { text: 'A2', icon: 'mdi-flag' },
        { text: 'B1', icon: 'mdi-flag' },
        { text: 'B2', icon: 'mdi-flag' },
        { text: 'C1', icon: 'mdi-flag' },
        { text: 'C2', icon: 'mdi-flag' },
      ],
      vocabs: [
        { headword: 'apple', 'pos': 'noun.', 'en_def': 'Definition: a round fruit with firm, white flesh and a green, red, or yellow skin' },
        { headword: 'banana', 'pos': 'noun.', 'en_def': '...' },
      ]
    }
  }
}
</script>
