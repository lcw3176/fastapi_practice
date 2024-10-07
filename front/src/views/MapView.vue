<template>
  
</template>

<script>
import { useMapStore } from '@/store/map'
import '../assets/css/map.css'
import { ref } from 'vue'
import { useDisplay } from 'vuetify'

export default {
  name: 'MapView',

  setup () {
    const mapStore = useMapStore()

    return {
      mapStore
    }
  },

  data () {
    const display = ref(useDisplay())

    return {
      overlay: null,
      display
    }
  },

  mounted () {
    // this.mapStore.init()
    // this.mapStore.addListeners()

  },

  beforeUnmount () {
    // this.mapStore.removeListeners()
  },
}
</script>
