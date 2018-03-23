<template>
    <div>
        <h1 style="float: left; padding-left: 30%;">Globekit Data Entry CMS</h1>
        <div class="row" style="width: 100%">
            <div class="col-6" v-if="events && !showGlobe">
                <h3>Events List</h3>
                <event_list :events="events"></event_list>
            </div>
            <div class="col-3" v-if="events && showGlobe">
                <h3>Events List</h3>
                <event_list :events="events"></event_list>
            </div>
            <div class="col-6" v-if="!events">
                Events loading...
            </div>
            <div class="col-6" v-if="!showGlobe">
                <h3>Create new event</h3>
                <entry_form :publishers="publishers" v-on:submit="submit"></entry_form>
                <button class="btn btn-primary" v-on:click="loadGlobe">Show Globe</button>
            </div>
            <div class="col-9" v-if="showGlobe">
                <div class="globe-container">Globe goes here</div>
                <button class="btn btn-primary" v-on:click="showForm">Show Form</button>
            </div>
        </div>
    </div>

</template>

<script>
  import EntryForm from './EntryForm.vue'
  import EventList from './EventList.vue'
  //import {GlobeData} from '../assets/js/GlobeData.js'
  //import {Site} from '../assets/js/Site.js'

  export default {
    name: 'Home',
    components: {
      entry_form: EntryForm,
      event_list: EventList
    },
    data () {
      return {
        b: 'Welcome to Your Vue.js App',
        events: null,
        publishers: [],
        showGlobe: false
      }
    },
    mounted: function() {
      var me = this
      let events_url = 'http://globekit-cms.appspot.com/globekit_data/'
//      let events_url = 'http://127.0.0.1:8000/globekit_data/'
      this.$http.get(events_url).then(response => {
        let data = response.body
        console.log(data)
        me.events = data.events
      })
      let publisher_url = 'http://globekit-cms.appspot.com/publishers/'
      this.$http.get(publisher_url).then(response => {
        let data = response.body
        console.log(data)
        me.publishers = data
      })
    },
    methods: {
      submit (e) {
        this.events = e
      },
      showForm () {
        this.showGlobe = false
      },
      loadGlobe () {
        this.showGlobe = true

      }
    }
  }
</script>

<style scoped>
    .btn {
        margin-top: 30px;
        display: inline-block;
    }
    .globe-container {
        display: inline-block;
        width: 100%;
        height: 1100px;
        border: 1px solid black;
    }
</style>