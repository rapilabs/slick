<template>
  <div id="app">
    <sidebar v-if="isRegistered" v-bind:user="user" />
    <channel v-if="isRegistered" v-bind:user="user" />
    <registration v-if="!isRegistered" v-on:registered="handleRegistered" />
  </div>
</template>

<script>
import axios from 'axios';

import Sidebar from './components/Sidebar.vue';
import Channel from './components/Channel.vue';
import Registration from './components/Registration.vue';

export default {
  name: 'app',
  components: {
    Sidebar,
    Channel,
    Registration,
  },
  data() {
    return {
      isRegistered: false,
    };
  },
  methods: {
    handleRegistered(user) {
      this.user = user;
      this.isRegistered = true;
    },
  },
  beforeCreate() {
    axios.get('/whoami').then(response => {
      this.user = {
        username: response.data.username,
      };
      this.isRegistered = true;
    });
  },
  mounted() {
  },
};
</script>

<style>
#app {
 display: flex;
}
</style>
